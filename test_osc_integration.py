#!/usr/bin/env python3
"""
Test script to validate OSC integration with Ableton Live
Tests the actual communication between handlers and AbletonOSC
"""

import asyncio
import sys
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from ableton_control.osc_client.client import AbletonOSCClient
from mcp_server.tools.ableton_tools import AbletonTools
from mcp_server.handlers.transport import TransportHandler
from mcp_server.handlers.track import TrackHandler
from mcp_server.handlers.midi import MIDIHandler
from mcp_server.handlers.instruments import InstrumentsHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OSCIntegrationTester:
    """Test the OSC integration with actual Ableton Live communication"""
    
    def __init__(self):
        self.osc_client = None
        self.ableton_tools = None
        self.handlers = {}
        
    async def setup(self):
        """Initialize OSC connection and handlers"""
        try:
            # Initialize AbletonTools (which includes the OSC client)
            self.ableton_tools = AbletonTools()
            logger.info("🔌 Connecting to Ableton Live...")
            
            connected = await self.ableton_tools.connect()
            if not connected:
                logger.error("❌ Failed to connect to Ableton Live")
                logger.error("Make sure Ableton Live is running with AbletonOSC enabled")
                return False
                
            # Get reference to the OSC client from AbletonTools
            self.osc_client = self.ableton_tools.osc_client
            
            # Initialize handlers with shared AbletonTools instance
            self.handlers = {
                "transport": TransportHandler(self.ableton_tools),
                "track": TrackHandler(self.ableton_tools),
                "midi": MIDIHandler(self.ableton_tools),
                "instruments": InstrumentsHandler(self.ableton_tools)
            }
            
            logger.info("✅ Setup complete")
            return True
            
        except Exception as e:
            logger.error(f"❌ Setup failed: {e}")
            return False
    
    async def test_basic_connection(self):
        """Test basic OSC connection and Live version retrieval"""
        logger.info("\n🧪 Testing basic connection...")
        
        try:
            version = await self.osc_client.get_live_version()
            if version:
                logger.info(f"✅ Connected to Ableton Live {version}")
                return True
            else:
                logger.error("❌ No version response from Live")
                return False
        except Exception as e:
            logger.error(f"❌ Connection test failed: {e}")
            return False
    
    async def test_transport_operations(self):
        """Test transport control (play/stop)"""
        logger.info("\n🧪 Testing transport operations...")
        
        try:
            # Test play
            result = await self.handlers["transport"].play()
            logger.info(f"Play result: {result}")
            
            await asyncio.sleep(2)  # Let it play for 2 seconds
            
            # Test stop
            result = await self.handlers["transport"].stop()
            logger.info(f"Stop result: {result}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Transport test failed: {e}")
            return False
    
    async def test_track_creation(self):
        """Test track creation"""
        logger.info("\n🧪 Testing track creation...")
        
        try:
            # Get initial track count
            initial_count = await self.osc_client.get_track_count()
            logger.info(f"Initial track count: {initial_count}")
            
            # Create MIDI track
            result = await self.handlers["track"].create_track("midi", "Test MIDI Track")
            logger.info(f"Create track result: {result}")
            
            # Wait and check track count
            await asyncio.sleep(1)
            new_count = await self.osc_client.get_track_count()
            logger.info(f"New track count: {new_count}")
            
            if new_count and initial_count and new_count > initial_count:
                logger.info("✅ Track creation verified")
                return True
            else:
                logger.error("❌ Track creation not verified")
                return False
                
        except Exception as e:
            logger.error(f"❌ Track creation test failed: {e}")
            return False
    
    async def test_clip_creation(self):
        """Test MIDI clip creation and note addition"""
        logger.info("\n🧪 Testing clip creation...")
        
        try:
            # Create a clip on track 0
            result = await self.handlers["midi"].create_midi_clip(
                track_id=0, 
                clip_slot=0, 
                scale_name="natural_minor",
                root_note="C"
            )
            logger.info(f"Create clip result: {result}")
            
            # Small delay to let clip creation complete
            await asyncio.sleep(0.5)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Clip creation test failed: {e}")
            return False
    
    async def test_instrument_loading(self):
        """Test instrument loading"""
        logger.info("\n🧪 Testing instrument loading...")
        
        try:
            # Try to load a basic Live instrument
            result = await self.handlers["instruments"].load_instrument(
                track_id=0,
                instrument_name="Bass",  # Common Live instrument
                preset_name=None
            )
            logger.info(f"Load instrument result: {result}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Instrument loading test failed: {e}")
            return False
    
    async def test_tempo_operations(self):
        """Test tempo getting and setting"""
        logger.info("\n🧪 Testing tempo operations...")
        
        try:
            # Get current tempo
            current_tempo = await self.osc_client.get_tempo()
            logger.info(f"Current tempo: {current_tempo} BPM")
            
            # Set new tempo
            new_tempo = 128.0
            await self.osc_client.set_tempo(new_tempo)
            
            # Wait and verify
            await asyncio.sleep(0.5)
            verified_tempo = await self.osc_client.get_tempo()
            logger.info(f"Tempo after setting to {new_tempo}: {verified_tempo}")
            
            if verified_tempo and abs(verified_tempo - new_tempo) < 0.1:
                logger.info("✅ Tempo change verified")
                return True
            else:
                logger.error("❌ Tempo change not verified")
                return False
                
        except Exception as e:
            logger.error(f"❌ Tempo test failed: {e}")
            return False
    
    async def cleanup(self):
        """Clean up connections"""
        if self.osc_client:
            self.osc_client.disconnect()
        if self.ableton_tools:
            self.ableton_tools.disconnect()
    
    async def run_all_tests(self):
        """Run all integration tests"""
        logger.info("🚀 Starting OSC Integration Tests")
        logger.info("=" * 50)
        
        # Setup
        if not await self.setup():
            logger.error("❌ Setup failed, aborting tests")
            return
        
        # Run tests
        tests = [
            ("Basic Connection", self.test_basic_connection),
            ("Transport Operations", self.test_transport_operations),
            ("Track Creation", self.test_track_creation),
            ("Clip Creation", self.test_clip_creation),
            ("Instrument Loading", self.test_instrument_loading),
            ("Tempo Operations", self.test_tempo_operations),
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
        
        # Summary
        logger.info(f"\n{'=' * 50}")
        logger.info(f"🏁 TEST SUMMARY: {passed}/{total} tests passed")
        
        if passed == total:
            logger.info("🎉 All tests passed! OSC integration is working correctly")
        else:
            logger.error(f"⚠️  {total - passed} tests failed. OSC integration needs fixes")
        
        await self.cleanup()

async def main():
    """Main test runner"""
    tester = OSCIntegrationTester()
    await tester.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main())