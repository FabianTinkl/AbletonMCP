"""
Ableton Tools - High-level wrapper for Ableton Live operations
"""

import asyncio
import logging
from typing import Optional, Dict, Any, List

from ableton_control.osc_client.client import AbletonOSCClient

logger = logging.getLogger(__name__)

class AbletonTools:
    """High-level interface for Ableton Live operations."""
    
    def __init__(self, host: str = "127.0.0.1", send_port: int = 11000, receive_port: int = 11001):
        """Initialize Ableton tools with OSC client."""
        self.osc_client = AbletonOSCClient(host, send_port, receive_port)
        self.connected = False
        
    async def connect(self) -> bool:
        """Connect to Ableton Live."""
        if not self.connected:
            self.connected = await self.osc_client.connect()
            if self.connected:
                logger.info("🎵 AbletonTools connected successfully")
            else:
                logger.error("❌ Failed to connect AbletonTools")
        return self.connected
    
    def disconnect(self):
        """Disconnect from Ableton Live."""
        if self.connected:
            self.osc_client.disconnect()
            self.connected = False
            logger.info("AbletonTools disconnected")
    
    async def ensure_connected(self):
        """Ensure we have a connection to Ableton Live."""
        if not self.connected:
            await self.connect()
        if not self.connected:
            raise ConnectionError("Cannot connect to Ableton Live. Make sure Live is running with AbletonOSC enabled.")
    
    # Transport Operations
    async def play(self) -> Dict[str, Any]:
        """Start playback in Ableton Live."""
        await self.ensure_connected()
        await self.osc_client.play()
        return {"status": "success", "message": "Playback started"}
    
    async def stop(self) -> Dict[str, Any]:
        """Stop playback in Ableton Live."""
        await self.ensure_connected()
        await self.osc_client.stop()
        return {"status": "success", "message": "Playback stopped"}
    
    async def set_tempo(self, bpm: float) -> Dict[str, Any]:
        """Set the tempo of the Live set."""
        await self.ensure_connected()
        
        if not 60 <= bpm <= 200:
            return {"status": "error", "message": f"BPM {bpm} is out of valid range (60-200)"}
        
        await self.osc_client.set_tempo(bpm)
        return {"status": "success", "message": f"Tempo set to {bpm} BPM"}
    
    async def get_tempo(self) -> Optional[float]:
        """Get the current tempo."""
        await self.ensure_connected()
        return await self.osc_client.get_tempo()
    
    # Track Operations  
    async def create_track(self, track_type: str, name: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new track in Ableton Live.
        
        Args:
            track_type: Type of track ("audio", "midi", "return")
            name: Optional name for the track
        """
        await self.ensure_connected()
        
        try:
            if track_type == "audio":
                await self.osc_client.create_audio_track(name)
            elif track_type == "midi":
                await self.osc_client.create_midi_track(name)
            elif track_type == "return":
                await self.osc_client.create_return_track(name)
            else:
                return {"status": "error", "message": f"Unknown track type: {track_type}"}
            
            track_name = name or f"New {track_type.title()} Track"
            return {
                "status": "success", 
                "message": f"Created {track_type} track: {track_name}",
                "track_type": track_type,
                "track_name": track_name
            }
            
        except Exception as e:
            logger.error(f"Failed to create track: {e}")
            return {"status": "error", "message": f"Failed to create track: {str(e)}"}
    
    async def get_track_count(self) -> Optional[int]:
        """Get the current number of tracks."""
        await self.ensure_connected()
        return await self.osc_client.get_track_count()
    
    # Clip Operations
    async def create_clip(self, track_idx: int, clip_slot_idx: int, length: float = 4.0) -> Dict[str, Any]:
        """Create a new clip."""
        await self.ensure_connected()
        
        try:
            await self.osc_client.create_clip(track_idx, clip_slot_idx, length)
            return {
                "status": "success",
                "message": f"Created {length}-bar clip in track {track_idx}, slot {clip_slot_idx}",
                "track_index": track_idx,
                "clip_slot_index": clip_slot_idx,
                "length_bars": length
            }
        except Exception as e:
            logger.error(f"Failed to create clip: {e}")
            return {"status": "error", "message": f"Failed to create clip: {str(e)}"}
    
    async def fire_clip(self, track_idx: int, clip_slot_idx: int) -> Dict[str, Any]:
        """Fire a clip to start playback."""
        await self.ensure_connected()
        
        try:
            await self.osc_client.fire_clip(track_idx, clip_slot_idx)
            return {
                "status": "success",
                "message": f"Fired clip at track {track_idx}, slot {clip_slot_idx}"
            }
        except Exception as e:
            logger.error(f"Failed to fire clip: {e}")
            return {"status": "error", "message": f"Failed to fire clip: {str(e)}"}
    
    # Device Operations
    async def load_device(self, track_idx: int, device_name: str) -> Dict[str, Any]:
        """Load a device onto a track."""
        await self.ensure_connected()
        
        try:
            await self.osc_client.load_device(track_idx, device_name)
            return {
                "status": "success",
                "message": f"Loaded {device_name} on track {track_idx}",
                "track_index": track_idx,
                "device_name": device_name
            }
        except Exception as e:
            logger.error(f"Failed to load device: {e}")
            return {"status": "error", "message": f"Failed to load device: {str(e)}"}
    
    async def set_device_parameter(self, track_idx: int, device_idx: int, parameter_idx: int, value: float) -> Dict[str, Any]:
        """Set a device parameter value."""
        await self.ensure_connected()
        
        if not 0.0 <= value <= 1.0:
            return {"status": "error", "message": "Parameter value must be between 0.0 and 1.0"}
        
        try:
            await self.osc_client.set_device_parameter(track_idx, device_idx, parameter_idx, value)
            return {
                "status": "success",
                "message": f"Set parameter {parameter_idx} on device {device_idx} (track {track_idx}) to {value}",
                "track_index": track_idx,
                "device_index": device_idx,
                "parameter_index": parameter_idx,
                "value": value
            }
        except Exception as e:
            logger.error(f"Failed to set device parameter: {e}")
            return {"status": "error", "message": f"Failed to set device parameter: {str(e)}"}
    
    # Project Operations
    async def new_project(self) -> Dict[str, Any]:
        """Create a new Live set."""
        await self.ensure_connected()
        
        try:
            await self.osc_client.new_live_set()
            return {"status": "success", "message": "Created new Live set"}
        except Exception as e:
            logger.error(f"Failed to create new project: {e}")
            return {"status": "error", "message": f"Failed to create new project: {str(e)}"}
    
    async def save_project(self) -> Dict[str, Any]:
        """Save the current Live set."""
        await self.ensure_connected()
        
        try:
            await self.osc_client.save_live_set()
            return {"status": "success", "message": "Live set saved"}
        except Exception as e:
            logger.error(f"Failed to save project: {e}")
            return {"status": "error", "message": f"Failed to save project: {str(e)}"}
    
    # Utility Methods
    async def get_live_info(self) -> Dict[str, Any]:
        """Get information about the current Live session."""
        await self.ensure_connected()
        
        try:
            version = await self.osc_client.get_live_version()
            tempo = await self.get_tempo()
            track_count = await self.get_track_count()
            
            return {
                "status": "success",
                "live_version": version,
                "current_tempo": tempo,
                "track_count": track_count,
                "connected": self.connected
            }
        except Exception as e:
            logger.error(f"Failed to get Live info: {e}")
            return {"status": "error", "message": f"Failed to get Live info: {str(e)}"}
    
    async def ping(self) -> Dict[str, Any]:
        """Ping Ableton Live to test connection."""
        try:
            await self.ensure_connected()
            version = await self.osc_client.get_live_version()
            if version:
                return {
                    "status": "success", 
                    "message": f"Connected to Ableton Live {version}",
                    "version": version
                }
            else:
                return {"status": "error", "message": "No response from Ableton Live"}
        except Exception as e:
            return {"status": "error", "message": f"Connection failed: {str(e)}"}

    # MIDI Operations
    async def add_notes_to_clip(self, track_idx: int, clip_idx: int, notes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Add MIDI notes to a clip.
        
        Args:
            track_idx: Track index
            clip_idx: Clip index  
            notes: List of note dictionaries with keys: pitch, start_time, duration, velocity
            
        Returns:
            Status dict with success/error message
        """
        await self.ensure_connected()
        
        try:
            for note in notes:
                await self.osc_client.add_notes(
                    track_idx, 
                    clip_idx,
                    note["pitch"],
                    note["start_time"], 
                    note["duration"],
                    note["velocity"],
                    note.get("mute", False)
                )
                
            return {
                "status": "success",
                "message": f"Added {len(notes)} MIDI notes to track {track_idx}, clip {clip_idx}",
                "track_index": track_idx,
                "clip_index": clip_idx,
                "notes_count": len(notes)
            }
            
        except Exception as e:
            logger.error(f"Failed to add notes to clip: {e}")
            return {"status": "error", "message": f"Failed to add notes: {str(e)}"}