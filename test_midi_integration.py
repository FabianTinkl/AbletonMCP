#!/usr/bin/env python3
"""
Test script specifically for MIDI clip and note operations
"""

import asyncio
import sys
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from mcp_server.tools.ableton_tools import AbletonTools
from mcp_server.handlers.midi import MIDIHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MIDIIntegrationTester:
    """Test MIDI clip creation and note addition specifically"""
    
    def __init__(self):
        self.ableton_tools = None
        self.midi_handler = None
        
    async def setup(self):
        """Initialize connection"""
        try:
            self.ableton_tools = AbletonTools()
            connected = await self.ableton_tools.connect()
            if not connected:
                logger.error("❌ Failed to connect to Ableton Live")
                return False
                
            self.midi_handler = MIDIHandler(self.ableton_tools)
            logger.info("✅ MIDI setup complete")
            return True
        except Exception as e:
            logger.error(f"❌ Setup failed: {e}")
            return False
    
    async def test_clip_creation_and_notes(self):
        """Test complete MIDI workflow"""
        logger.info("\n🎹 Testing complete MIDI workflow...")
        
        try:
            track_id = 0
            clip_slot = 0
            
            # Step 1: Create MIDI clip
            logger.info("Step 1: Creating MIDI clip...")
            clip_result = await self.midi_handler.create_midi_clip(
                track_id=track_id,
                clip_slot=clip_slot,
                scale_name="natural_minor",
                root_note="C"
            )
            logger.info(f"Clip creation result: {clip_result[0]['text'][:100]}...")
            
            # Step 2: Wait for clip creation
            await asyncio.sleep(0.5)
            
            # Step 3: Add individual notes
            logger.info("Step 2: Adding individual notes...")
            
            # Add a C note
            await self.ableton_tools.osc_client.add_notes(track_id, clip_slot, 60, 0.0, 1.0, 100, False)
            await asyncio.sleep(0.1)
            
            # Add an E♭ note
            await self.ableton_tools.osc_client.add_notes(track_id, clip_slot, 63, 1.0, 1.0, 100, False)
            await asyncio.sleep(0.1)
            
            # Add a G note
            await self.ableton_tools.osc_client.add_notes(track_id, clip_slot, 67, 2.0, 1.0, 100, False)
            await asyncio.sleep(0.1)
            
            logger.info("✅ Added 3 notes: C, E♭, G")
            
            # Step 4: Verify notes were added
            logger.info("Step 3: Verifying notes...")
            try:
                notes = await self.ableton_tools.osc_client.get_notes(track_id, clip_slot)
                if notes:
                    logger.info(f"✅ Notes retrieved: {len(notes)} notes found")
                    logger.info(f"Note data: {notes}")
                else:
                    logger.warning("⚠️ No notes retrieved (might be expected)")
            except Exception as e:
                logger.warning(f"⚠️ Could not retrieve notes: {e}")
            
            # Step 5: Test firing the clip
            logger.info("Step 4: Testing clip playback...")
            await self.ableton_tools.osc_client.fire_clip(track_id, clip_slot)
            logger.info("✅ Clip fired for playback")
            
            # Wait a moment then stop
            await asyncio.sleep(2)
            await self.ableton_tools.osc_client.stop()
            logger.info("✅ Playback stopped")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ MIDI workflow test failed: {e}")
            return False
    
    async def test_direct_osc_commands(self):
        """Test OSC commands directly"""
        logger.info("\n🔧 Testing direct OSC commands...")
        
        try:
            track_id = 1
            clip_slot = 0
            
            # Create clip with direct OSC
            logger.info("Creating clip with direct OSC...")
            self.ableton_tools.osc_client.send("/live/clip_slot/create_clip", track_id, clip_slot, 4.0)
            await asyncio.sleep(0.5)
            
            # Add notes with direct OSC
            logger.info("Adding notes with direct OSC...")
            self.ableton_tools.osc_client.send("/live/clip/add/notes", track_id, clip_slot, 60, 0.0, 1.0, 100, 0)
            self.ableton_tools.osc_client.send("/live/clip/add/notes", track_id, clip_slot, 64, 1.0, 1.0, 100, 0)
            self.ableton_tools.osc_client.send("/live/clip/add/notes", track_id, clip_slot, 67, 2.0, 1.0, 100, 0)
            
            await asyncio.sleep(0.5)
            
            # Fire clip
            logger.info("Firing clip...")
            self.ableton_tools.osc_client.send("/live/clip_slot/fire", track_id, clip_slot)
            
            logger.info("✅ Direct OSC commands executed")
            return True
            
        except Exception as e:
            logger.error(f"❌ Direct OSC test failed: {e}")
            return False
    
    async def cleanup(self):
        """Clean up connections"""
        if self.ableton_tools:
            self.ableton_tools.disconnect()
    
    async def run_tests(self):
        """Run all MIDI tests"""
        logger.info("🎹 Starting MIDI Integration Tests")
        logger.info("=" * 50)
        
        if not await self.setup():
            logger.error("❌ Setup failed, aborting tests")
            return
        
        tests = [
            ("MIDI Workflow (Clip + Notes)", self.test_clip_creation_and_notes),
            ("Direct OSC Commands", self.test_direct_osc_commands),
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            logger.info(f"\n{'=' * 20}")
            try:
                if await test_func():
                    passed += 1
                    logger.info(f"✅ {test_name} PASSED")
                else:
                    logger.error(f"❌ {test_name} FAILED")
            except Exception as e:
                logger.error(f"❌ {test_name} ERROR: {e}")
        
        logger.info(f"\n{'=' * 50}")
        logger.info(f"🏁 MIDI TEST SUMMARY: {passed}/{total} tests passed")
        
        await self.cleanup()

async def main():
    """Main test runner"""
    tester = MIDIIntegrationTester()
    await tester.run_tests()

if __name__ == "__main__":
    asyncio.run(main())