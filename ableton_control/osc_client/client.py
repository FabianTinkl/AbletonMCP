"""
OSC Client for Ableton Live Communication
"""

import asyncio
import logging
from typing import Any, Optional, Dict, List, Callable
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import threading
import time

logger = logging.getLogger(__name__)

class AbletonOSCClient:
    """OSC client for communicating with Ableton Live via AbletonOSC."""
    
    def __init__(self, host: str = "127.0.0.1", send_port: int = 11000, receive_port: int = 11001):
        """
        Initialize the OSC client.
        
        Args:
            host: IP address of Ableton Live (usually localhost)
            send_port: Port to send OSC messages to AbletonOSC (default 11000)
            receive_port: Port to receive OSC messages from AbletonOSC (default 11001)
        """
        self.host = host
        self.send_port = send_port
        self.receive_port = receive_port
        
        # OSC client for sending messages
        self.client = SimpleUDPClient(host, send_port)
        
        # OSC server for receiving messages
        self.dispatcher = Dispatcher()
        self.server = None
        self.server_thread = None
        
        # Response handling
        self.response_handlers: Dict[str, Callable] = {}
        self.pending_responses: Dict[str, Any] = {}
        
        self._setup_handlers()
        
    def _setup_handlers(self):
        """Set up default OSC message handlers."""
        # General response handler
        self.dispatcher.map("/live/*", self._handle_live_response)
        
    def _handle_live_response(self, address: str, *args):
        """Handle incoming OSC messages from Ableton Live."""
        logger.debug(f"Received OSC: {address} {args}")
        
        # Store response for pending requests
        self.pending_responses[address] = args
        
        # Call custom handlers if registered
        if address in self.response_handlers:
            self.response_handlers[address](args)
    
    async def connect(self) -> bool:
        """
        Connect to Ableton Live and start the OSC server.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Start OSC server for receiving messages
            self.server = BlockingOSCUDPServer((self.host, self.receive_port), self.dispatcher)
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            
            logger.info(f"OSC server listening on {self.host}:{self.receive_port}")
            
            # Test connection by getting Live version
            test_result = await self.get_live_version()
            if test_result:
                logger.info("✅ Successfully connected to Ableton Live")
                return True
            else:
                logger.error("❌ Failed to connect to Ableton Live")
                return False
                
        except Exception as e:
            logger.error(f"Failed to start OSC client: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from Ableton Live."""
        if self.server:
            self.server.shutdown()
        if self.server_thread:
            self.server_thread.join(timeout=1.0)
        logger.info("Disconnected from Ableton Live")
    
    def send(self, address: str, *args):
        """
        Send an OSC message to Ableton Live.
        
        Args:
            address: OSC address (e.g., "/live/song/set/tempo")
            *args: Arguments to send with the message
        """
        try:
            self.client.send_message(address, args if len(args) > 1 else (args[0] if args else []))
            logger.debug(f"Sent OSC: {address} {args}")
        except Exception as e:
            logger.error(f"Failed to send OSC message {address}: {e}")
    
    async def send_and_wait(self, address: str, response_address: str, *args, timeout: float = 2.0) -> Optional[Any]:
        """
        Send an OSC message and wait for a response.
        
        Args:
            address: OSC address to send to
            response_address: OSC address to wait for response on
            *args: Arguments to send
            timeout: Timeout in seconds
            
        Returns:
            Response data or None if timeout
        """
        # Clear any existing response
        self.pending_responses.pop(response_address, None)
        
        # Send the message
        self.send(address, *args)
        
        # Wait for response
        start_time = time.time()
        while time.time() - start_time < timeout:
            if response_address in self.pending_responses:
                response = self.pending_responses.pop(response_address)
                return response
            await asyncio.sleep(0.01)  # Small delay to prevent busy waiting
        
        logger.warning(f"Timeout waiting for response to {address}")
        return None
    
    # Transport Control Methods
    async def play(self):
        """Start playback."""
        self.send("/live/song/start_playing")
        
    async def stop(self):
        """Stop playback."""  
        self.send("/live/song/stop_playing")
        
    async def set_tempo(self, bpm: float):
        """Set the tempo."""
        self.send("/live/song/set/tempo", bpm)
        
    async def get_tempo(self) -> Optional[float]:
        """Get the current tempo."""
        response = await self.send_and_wait(
            "/live/song/get/tempo",
            "/live/song/get/tempo"
        )
        return response[0] if response else None
    
    async def get_live_version(self) -> Optional[str]:
        """Get Ableton Live version to test connection."""
        response = await self.send_and_wait(
            "/live/application/get/version",
            "/live/application/get/version"
        )
        return response[0] if response else None
    
    # Track Management Methods
    async def create_audio_track(self, name: Optional[str] = None):
        """Create a new audio track."""
        # Get current track count to know the index of the new track
        track_count = await self.get_track_count() or 0
        self.send("/live/song/create_audio_track", -1)  # -1 means end of list
        if name:
            await asyncio.sleep(0.2)  # Longer delay for track creation
            self.send("/live/track/set/name", track_count, name)
    
    async def create_midi_track(self, name: Optional[str] = None):
        """Create a new MIDI track."""
        # Get current track count to know the index of the new track
        track_count = await self.get_track_count() or 0
        self.send("/live/song/create_midi_track", -1)  # -1 means end of list
        if name:
            await asyncio.sleep(0.2)  # Longer delay for track creation
            self.send("/live/track/set/name", track_count, name)
    
    async def create_return_track(self, name: Optional[str] = None):
        """Create a new return track."""
        self.send("/live/song/create_return_track")
        if name:
            await asyncio.sleep(0.1)
            self.send("/live/return_track/set/name", -1, name)
    
    # Clip Management Methods
    async def create_clip(self, track_idx: int, clip_slot_idx: int, length: float = 4.0):
        """
        Create a new clip in the specified clip slot.
        
        Args:
            track_idx: Track index
            clip_slot_idx: Clip slot index
            length: Clip length in bars
        """
        # Create clip with length directly according to AbletonOSC API
        self.send("/live/clip_slot/create_clip", track_idx, clip_slot_idx, length)
    
    async def fire_clip(self, track_idx: int, clip_slot_idx: int):
        """Fire a clip."""
        self.send("/live/clip_slot/fire", track_idx, clip_slot_idx)
    
    async def stop_clip(self, track_idx: int):
        """Stop all clips on a track."""
        self.send("/live/track/stop_all_clips", track_idx)
    
    # Device and Parameter Control
    async def load_device(self, track_idx: int, device_name: str):
        """
        NOTE: AbletonOSC cannot dynamically load devices. 
        This method is kept for compatibility but will not actually load devices.
        Users must manually load devices in Ableton Live first.
        
        Args:
            track_idx: Track index
            device_name: Name of the device to load (for reference only)
        """
        logger.warning(f"⚠️ Cannot load device '{device_name}' on track {track_idx}")
        logger.warning("💡 AbletonOSC doesn't support dynamic device loading")
        logger.info("🔧 Please manually load devices in Ableton Live, then use device control commands")
    
    async def set_device_parameter(self, track_idx: int, device_idx: int, parameter_idx: int, value: float):
        """
        Set a device parameter value.
        
        Args:
            track_idx: Track index
            device_idx: Device index on the track
            parameter_idx: Parameter index on the device
            value: Parameter value (0.0 - 1.0)
        """
        self.send("/live/device/set/parameter/value", track_idx, device_idx, parameter_idx, value)
    
    # Project Management
    async def new_live_set(self):
        """Create a new Live set."""
        # Note: This command may not be available in AbletonOSC
        # Using song-level command instead
        self.send("/live/song/create_scene")  # Create a new scene as fallback
    
    async def save_live_set(self):
        """Save the current Live set."""
        # Note: Save functionality may not be available via OSC
        # This is a placeholder - manual save required
        logger.warning("Save functionality not available via AbletonOSC - please save manually in Live")
    
    async def get_track_count(self) -> Optional[int]:
        """Get the number of tracks in the current Live set."""
        response = await self.send_and_wait(
            "/live/song/get/num_tracks",
            "/live/song/get/num_tracks"
        )
        return response[0] if response else None
    
    async def get_live_version(self) -> Optional[str]:
        """Get Ableton Live version - basic connectivity test."""
        try:
            # Try to get tempo as a simple connectivity test
            response = await self.send_and_wait("/live/song/get/tempo", "/live/song/get/tempo", timeout=2.0)
            if response is not None:
                return "Ableton Live (connected via AbletonOSC)"
            return None
        except Exception as e:
            logger.error(f"Failed to get Live version: {e}")
            return None
    
    async def ping(self) -> bool:
        """Simple ping test to verify connection with Ableton Live."""
        try:
            # Use tempo query as ping test
            response = await self.send_and_wait("/live/song/get/tempo", "/live/song/get/tempo", timeout=2.0)
            return response is not None
        except Exception as e:
            logger.error(f"Ping failed: {e}")
            return False
    
    # Advanced MIDI Operations
    async def add_notes(self, track_idx: int, clip_idx: int, pitch: int, start_time: float, 
                       duration: float, velocity: int, mute: bool = False):
        """Add notes to a MIDI clip."""
        self.send("/live/clip/add/notes", track_idx, clip_idx, pitch, start_time, duration, velocity, int(mute))
    
    async def remove_notes(self, track_idx: int, clip_idx: int, pitch: int, start_time: float, duration: float):
        """Remove notes from a MIDI clip."""
        self.send("/live/clip/remove/notes", track_idx, clip_idx, pitch, start_time, duration)
    
    async def get_notes(self, track_idx: int, clip_idx: int, 
                       start_time: Optional[float] = None, time_span: Optional[float] = None,
                       start_pitch: Optional[int] = None, pitch_span: Optional[int] = None):
        """Get notes from a MIDI clip."""
        if start_time is not None and time_span is not None and start_pitch is not None and pitch_span is not None:
            return await self.send_and_wait(
                "/live/clip/get/notes",
                "/live/clip/get/notes",
                track_idx, clip_idx, start_time, time_span, start_pitch, pitch_span
            )
        else:
            return await self.send_and_wait(
                "/live/clip/get/notes",
                "/live/clip/get/notes", 
                track_idx, clip_idx
            )
    
    async def clear_all_notes(self, track_idx: int, clip_idx: int):
        """Clear all notes from a MIDI clip."""
        # According to AbletonOSC docs: If no ranges specified, all notes are removed
        self.send("/live/clip/remove/notes", track_idx, clip_idx)
    
    async def set_clip_name(self, track_idx: int, clip_idx: int, name: str):
        """Set clip name."""
        self.send("/live/clip/set/name", track_idx, clip_idx, name)
    
    async def get_clip_name(self, track_idx: int, clip_idx: int):
        """Get clip name."""
        return await self.send_and_wait("/live/clip/get/name", "/live/clip/get/name", track_idx, clip_idx)
    
    async def set_clip_color(self, track_idx: int, clip_idx: int, color_index: int):
        """Set clip color."""
        self.send("/live/clip/set/color", track_idx, clip_idx, color_index)
    
    async def get_clip_length(self, track_idx: int, clip_idx: int):
        """Get clip length in bars."""
        return await self.send_and_wait("/live/clip/get/length", "/live/clip/get/length", track_idx, clip_idx)
    
    async def set_loop_start(self, track_idx: int, clip_idx: int, start: float):
        """Set clip loop start position."""
        self.send("/live/clip/set/loop_start", track_idx, clip_idx, start)
    
    async def set_clip_gain(self, track_idx: int, clip_idx: int, gain: float):
        """Set clip gain level."""
        self.send("/live/clip/set/gain", track_idx, clip_idx, gain)
    
    # Advanced Device Operations
    async def get_device_name(self, track_idx: int, device_idx: int):
        """Get device name."""
        return await self.send_and_wait("/live/device/get/name", "/live/device/get/name", track_idx, device_idx)
    
    async def get_device_class_name(self, track_idx: int, device_idx: int):
        """Get device class name.""" 
        return await self.send_and_wait("/live/device/get/class_name", "/live/device/get/class_name", track_idx, device_idx)
    
    async def get_device_parameters_name(self, track_idx: int, device_idx: int):
        """Get all parameter names for a device."""
        return await self.send_and_wait(
            "/live/device/get/parameters/name", 
            "/live/device/get/parameters/name",
            track_idx, device_idx
        )
    
    async def get_device_parameters_value(self, track_idx: int, device_idx: int):
        """Get all parameter values for a device."""
        return await self.send_and_wait(
            "/live/device/get/parameters/value",
            "/live/device/get/parameters/value",
            track_idx, device_idx
        )
    
    async def get_devices_name(self, track_idx: int):
        """Get all device names on a track."""
        return await self.send_and_wait("/live/track/get/devices/name", "/live/track/get/devices/name", track_idx)
    
    async def get_num_devices(self, track_idx: int):
        """Get number of devices on a track."""
        return await self.send_and_wait("/live/track/get/num_devices", "/live/track/get/num_devices", track_idx)
    
    # Track Operations
    async def set_track_name(self, track_idx: int, name: str):
        """Set track name."""
        self.send("/live/track/set/name", track_idx, name)
    
    async def get_track_name(self, track_idx: int):
        """Get track name."""
        return await self.send_and_wait("/live/track/get/name", "/live/track/get/name", track_idx)
    
    async def set_track_volume(self, track_idx: int, volume: float):
        """Set track volume (0.0-1.0)."""
        self.send("/live/track/set/volume", track_idx, volume)
    
    async def get_track_volume(self, track_idx: int):
        """Get track volume."""
        return await self.send_and_wait("/live/track/get/volume", "/live/track/get/volume", track_idx)
    
    async def set_track_mute(self, track_idx: int, mute: bool):
        """Set track mute state."""
        self.send("/live/track/set/mute", track_idx, int(mute))
    
    async def set_track_solo(self, track_idx: int, solo: bool):
        """Set track solo state."""
        self.send("/live/track/set/solo", track_idx, int(solo))
    
    async def set_track_arm(self, track_idx: int, arm: bool):
        """Set track record arm state."""
        self.send("/live/track/set/arm", track_idx, int(arm))
    
    async def set_track_panning(self, track_idx: int, pan: float):
        """Set track panning (-1.0 to 1.0)."""
        self.send("/live/track/set/panning", track_idx, pan)
    
    async def stop_track_clips(self, track_idx: int):
        """Stop all clips on a track."""
        self.send("/live/track/stop_all_clips", track_idx)
    
    # Scene Operations
    async def fire_scene(self, scene_idx: int):
        """Fire a scene."""
        self.send("/live/scene/fire", scene_idx)
    
    async def create_scene(self, index: Optional[int] = None):
        """Create a new scene."""
        if index is not None:
            self.send("/live/song/create_scene", index)
        else:
            self.send("/live/song/create_scene")
    
    async def delete_scene(self, scene_idx: int):
        """Delete a scene."""
        self.send("/live/song/delete_scene", scene_idx)
    
    async def get_scene_name(self, scene_idx: int):
        """Get scene name."""
        return await self.send_and_wait("/live/scene/get/name", "/live/scene/get/name", scene_idx)
    
    async def set_scene_name(self, scene_idx: int, name: str):
        """Set scene name."""
        self.send("/live/scene/set/name", scene_idx, name)
    
    # Song Operations
    async def get_current_song_time(self):
        """Get current playback position."""
        return await self.send_and_wait("/live/song/get/current_song_time", "/live/song/get/current_song_time")
    
    async def set_current_song_time(self, time: float):
        """Set playback position."""
        self.send("/live/song/set/current_song_time", time)
    
    async def get_song_name(self):
        """Get song/project name."""
        return await self.send_and_wait("/live/song/get/name", "/live/song/get/name")
    
    async def undo(self):
        """Undo last action."""
        self.send("/live/song/undo")
    
    async def redo(self):
        """Redo last undone action."""
        self.send("/live/song/redo")
    
    # Audio Clip Operations
    async def set_warp_mode(self, track_idx: int, clip_idx: int, warp_mode: str):
        """Set audio clip warp mode."""
        self.send("/live/clip/set/warp_mode", track_idx, clip_idx, warp_mode)
    
    async def get_clip_file_path(self, track_idx: int, clip_idx: int):
        """Get audio clip file path."""
        return await self.send_and_wait("/live/clip/get/file_path", "/live/clip/get/file_path", track_idx, clip_idx)
    
    async def set_start_marker(self, track_idx: int, clip_idx: int, start: float):
        """Set audio clip start marker."""
        self.send("/live/clip/set/start_marker", track_idx, clip_idx, start)
    
    async def set_end_marker(self, track_idx: int, clip_idx: int, end: float):
        """Set audio clip end marker."""
        self.send("/live/clip/set/end_marker", track_idx, clip_idx, end)
    
    async def get_clip_is_playing(self, track_idx: int, clip_idx: int):
        """Check if clip is playing."""
        return await self.send_and_wait("/live/clip/get/is_playing", "/live/clip/get/is_playing", track_idx, clip_idx)
    
    # Real-time Listening
    async def start_listen_beat(self):
        """Start listening for beat events."""
        self.send("/live/song/start_listen/beat")
    
    async def stop_listen_beat(self):
        """Stop listening for beat events."""
        self.send("/live/song/stop_listen/beat")
    
    async def start_listen_playing_position(self, track_idx: int, clip_idx: int):
        """Start listening for clip playing position."""
        self.send("/live/clip/start_listen/playing_position", track_idx, clip_idx)
    
    async def start_listen_parameter_value(self, track_idx: int, device_idx: int, param_idx: int):
        """Start listening for parameter value changes."""
        self.send("/live/device/start_listen/parameter/value", track_idx, device_idx, param_idx)
    
    # Bulk Data Queries
    async def get_track_data(self, start_track: int, num_tracks: int, properties: List[str]):
        """Get bulk track data."""
        return await self.send_and_wait(
            "/live/song/get/track_data",
            "/live/song/get/track_data",
            start_track, num_tracks, *properties
        )
    
    async def get_track_names(self):
        """Get all track names."""
        return await self.send_and_wait("/live/song/get/track_names", "/live/song/get/track_names")