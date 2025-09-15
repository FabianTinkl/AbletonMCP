"""
Transport Handler - Controls playback and tempo in Ableton Live
"""

import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class TransportHandler:
    """Handles transport-related MCP tool calls."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
    
    async def play(self) -> List[Dict[str, Any]]:
        """Start playback in Ableton Live."""
        logger.info("🎵 Starting playback")
        
        try:
            result = await self.ableton_tools.play()
            
            if result["status"] == "success":
                return [{"type": "text", "text": "▶️ Playback started"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to start playback: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error starting playback: {e}")
            return [{"type": "text", "text": f"❌ Error starting playback: {str(e)}"}]
    
    async def stop(self) -> List[Dict[str, Any]]:
        """Stop playback in Ableton Live."""
        logger.info("⏹️ Stopping playback")
        
        try:
            result = await self.ableton_tools.stop()
            
            if result["status"] == "success":
                return [{"type": "text", "text": "⏹️ Playback stopped"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to stop playback: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error stopping playback: {e}")
            return [{"type": "text", "text": f"❌ Error stopping playback: {str(e)}"}]
    
    async def set_tempo(self, bpm: float) -> List[Dict[str, Any]]:
        """Set the tempo of the Live set."""
        logger.info(f"🥁 Setting tempo to {bpm} BPM")
        
        try:
            result = await self.ableton_tools.set_tempo(bpm)
            
            if result["status"] == "success":
                return [{"type": "text", "text": f"🥁 Tempo set to {bpm} BPM"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to set tempo: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error setting tempo: {e}")
            return [{"type": "text", "text": f"❌ Error setting tempo: {str(e)}"}]
    
    async def get_tempo(self) -> List[Dict[str, Any]]:
        """Get the current tempo."""
        logger.info("🔍 Getting current tempo")
        
        try:
            tempo = await self.ableton_tools.get_tempo()
            
            if tempo is not None:
                return [{"type": "text", "text": f"🎵 Current tempo: {tempo} BPM"}]
            else:
                return [{"type": "text", "text": "❌ Could not retrieve current tempo"}]
                
        except Exception as e:
            logger.error(f"Error getting tempo: {e}")
            return [{"type": "text", "text": f"❌ Error getting tempo: {str(e)}"}]