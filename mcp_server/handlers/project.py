"""
Project Handler - Manages Live set operations
"""

import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class ProjectHandler:
    """Handles project-related MCP tool calls."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
    
    async def new_project(self) -> List[Dict[str, Any]]:
        """Create a new Live set."""
        logger.info("📄 Creating new Live set")
        
        try:
            result = await self.ableton_tools.new_project()
            
            if result["status"] == "success":
                return [{"type": "text", "text": "📄 New Live set created"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to create new Live set: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error creating new project: {e}")
            return [{"type": "text", "text": f"❌ Error creating new project: {str(e)}"}]
    
    async def save_project(self) -> List[Dict[str, Any]]:
        """Save the current Live set."""
        logger.info("💾 Saving Live set")
        
        try:
            result = await self.ableton_tools.save_project()
            
            if result["status"] == "success":
                return [{"type": "text", "text": "💾 Live set saved successfully"}]
            else:
                return [{"type": "text", "text": f"❌ Failed to save Live set: {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error saving project: {e}")
            return [{"type": "text", "text": f"❌ Error saving project: {str(e)}"}]
    
    async def get_project_info(self) -> List[Dict[str, Any]]:
        """Get information about the current Live session."""
        logger.info("ℹ️ Getting Live session info")
        
        try:
            info = await self.ableton_tools.get_live_info()
            
            if info["status"] == "success":
                info_text = f"""📊 **Live Session Info:**
• Version: {info.get('live_version', 'Unknown')}
• Tempo: {info.get('current_tempo', 'Unknown')} BPM
• Tracks: {info.get('track_count', 'Unknown')}
• Connected: {'✅' if info.get('connected') else '❌'}"""
                
                return [{"type": "text", "text": info_text}]
            else:
                return [{"type": "text", "text": f"❌ Failed to get project info: {info['message']}"}]
                
        except Exception as e:
            logger.error(f"Error getting project info: {e}")
            return [{"type": "text", "text": f"❌ Error getting project info: {str(e)}"}]
    
    async def ping_live(self) -> List[Dict[str, Any]]:
        """Test connection to Ableton Live."""
        logger.info("🔄 Pinging Ableton Live")
        
        try:
            result = await self.ableton_tools.ping()
            
            if result["status"] == "success":
                return [{"type": "text", "text": f"✅ {result['message']}"}]
            else:
                return [{"type": "text", "text": f"❌ {result['message']}"}]
                
        except Exception as e:
            logger.error(f"Error pinging Live: {e}")
            return [{"type": "text", "text": f"❌ Error pinging Live: {str(e)}"}]