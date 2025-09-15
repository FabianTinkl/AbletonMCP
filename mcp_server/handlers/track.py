"""
Track Handler - Manages track operations in Ableton Live
"""

import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class TrackHandler:
    """Handles track-related MCP tool calls."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
    
    async def create_track(self, track_type: str, name: Optional[str] = None) -> List[Dict[str, Any]]:
        """Create a new track in Ableton Live."""
        logger.info(f"🎛️ Creating {track_type} track: {name or 'Unnamed'}")
        
        try:
            result = await self.ableton_tools.create_track(track_type, name)
            
            if result["status"] == "success":
                track_emoji = {
                    "audio": "🎵",
                    "midi": "🎹", 
                    "return": "🔄"
                }.get(track_type, "🎛️")
                
                return [{"type": "text", "text": f"{track_emoji} {result['message']}"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to create track: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error creating track: {e}")
            return [{"type": "text", "text": f"❌ Error creating track: {str(e)}"}]
    
    async def get_track_count(self) -> List[Dict[str, Any]]:
        """Get the current number of tracks."""
        logger.info("🔢 Getting track count")
        
        try:
            count = await self.ableton_tools.get_track_count()
            
            if count is not None:
                return [{"type": "text", "text": f"🎛️ Current track count: {count}"}]
            else:
                return [{"type": "text", "text": "❌ Could not retrieve track count"}]
                
        except Exception as e:
            logger.error(f"Error getting track count: {e}")
            return [{"type": "text", "text": f"❌ Error getting track count: {str(e)}"}]
    
    async def create_clip(self, track_idx: int, clip_slot_idx: int, length: float = 4.0) -> List[Dict[str, Any]]:
        """Create a new clip in the specified track and slot."""
        logger.info(f"🎵 Creating {length}-bar clip in track {track_idx}, slot {clip_slot_idx}")
        
        try:
            result = await self.ableton_tools.create_clip(track_idx, clip_slot_idx, length)
            
            if result["status"] == "success":
                return [{"type": "text", "text": f"🎵 {result['message']}"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to create clip: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error creating clip: {e}")
            return [{"type": "text", "text": f"❌ Error creating clip: {str(e)}"}]
    
    async def fire_clip(self, track_idx: int, clip_slot_idx: int) -> List[Dict[str, Any]]:
        """Fire a clip to start playback."""
        logger.info(f"▶️ Firing clip at track {track_idx}, slot {clip_slot_idx}")
        
        try:
            result = await self.ableton_tools.fire_clip(track_idx, clip_slot_idx)
            
            if result["status"] == "success":
                return [{"type": "text", "text": f"▶️ {result['message']}"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to fire clip: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error firing clip: {e}")
            return [{"type": "text", "text": f"❌ Error firing clip: {str(e)}"}]
    
    async def load_device(self, track_idx: int, device_name: str) -> List[Dict[str, Any]]:
        """Load a device onto a track."""
        logger.info(f"🔧 Loading {device_name} on track {track_idx}")
        
        try:
            result = await self.ableton_tools.load_device(track_idx, device_name)
            
            if result["status"] == "success":
                return [{"type": "text", "text": f"🔧 {result['message']}"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to load device: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error loading device: {e}")
            return [{"type": "text", "text": f"❌ Error loading device: {str(e)}"}]
    
    async def set_device_parameter(self, track_idx: int, device_idx: int, parameter_idx: int, value: float) -> List[Dict[str, Any]]:
        """Set a device parameter value."""
        logger.info(f"🎛️ Setting parameter {parameter_idx} on device {device_idx} (track {track_idx}) to {value}")
        
        try:
            result = await self.ableton_tools.set_device_parameter(track_idx, device_idx, parameter_idx, value)
            
            if result["status"] == "success":
                return [{"type": "text", "text": f"🎛️ {result['message']}"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to set parameter: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error setting device parameter: {e}")
            return [{"type": "text", "text": f"❌ Error setting device parameter: {str(e)}"}]