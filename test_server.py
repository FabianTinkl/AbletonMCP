#!/usr/bin/env python3
"""
Test script for AbletonMCP Server
"""

import asyncio
import logging
import json
import sys
from pathlib import Path

# Add the project root to the path to fix imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_osc_connection():
    """Test the OSC connection to Ableton Live."""
    print("🔍 Testing OSC connection...")
    
    try:
        from ableton_control.osc_client.client import AbletonOSCClient
        
        client = AbletonOSCClient()
        connected = await client.connect()
        
        if connected:
            print("✅ OSC connection successful")
            
            # Test basic operations
            print("🎵 Testing basic operations...")
            
            # Get Live version
            version = await client.get_live_version()
            if version:
                print(f"📱 Ableton Live version: {version}")
            else:
                print("⚠️ Could not get Live version")
            
            # Get tempo
            tempo = await client.get_tempo()
            if tempo:
                print(f"🥁 Current tempo: {tempo} BPM")
            else:
                print("⚠️ Could not get tempo")
            
            client.disconnect()
            return True
        else:
            print("❌ OSC connection failed")
            print("📋 This is expected if Ableton Live is not running")
            print("💡 To test OSC connection:")
            print("   1. Open Ableton Live 11 Suite")
            print("   2. Make sure AbletonOSC is enabled in MIDI preferences") 
            print("   3. Run this test again")
            return False
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run 'pip install -r requirements.txt' to install dependencies")
        return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

async def test_mcp_tools():
    """Test MCP tools without actually running the server."""
    print("🔧 Testing MCP tools...")
    
    try:
        from mcp_server.tools.ableton_tools import AbletonTools
        
        tools = AbletonTools()
        
        # Test connection
        connected = await tools.connect()
        if connected:
            print("✅ AbletonTools connected")
            
            # Test ping
            result = await tools.ping()
            print(f"🏓 Ping result: {result['message']}")
            
            # Test get info
            info = await tools.get_live_info()
            if info["status"] == "success":
                print(f"📊 Live info: {info}")
            
            tools.disconnect()
            return True
        else:
            print("❌ AbletonTools connection failed")
            return False
            
    except Exception as e:
        print(f"❌ MCP tools test error: {e}")
        return False

async def test_composition_handler():
    """Test the composition handler."""
    print("🎼 Testing composition handler...")
    
    try:
        from mcp_server.tools.ableton_tools import AbletonTools
        from mcp_server.handlers.composition import CompositionHandler
        
        tools = AbletonTools()
        handler = CompositionHandler(tools)
        
        print("🎵 Testing chord progression generation...")
        # Test chord progression generation (doesn't require Live connection)
        result = await handler.generate_chord_progression("Am", "industrial", 8)
        if result and len(result) > 0:
            print("✅ Chord progression generated")
            print(f"📝 Result preview: {result[0]['text'][:100]}...")
        else:
            print("⚠️ Chord progression generation returned empty result")
        
        print("🥁 Testing drum pattern generation...")
        # Test drum pattern creation
        result = await handler.create_drum_pattern("industrial", 4)
        if result:
            print("✅ Drum pattern generated")
        else:
            print("⚠️ Drum pattern generation returned empty result")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run 'pip install -r requirements.txt' to install dependencies")
        return False
    except Exception as e:
        print(f"❌ Composition handler test error: {e}")
        return False

def test_project_structure():
    """Test that the project structure is correct."""
    print("📁 Testing project structure...")
    
    required_files = [
        "mcp_server/__init__.py",
        "mcp_server/main.py", 
        "mcp_server/tools/ableton_tools.py",
        "mcp_server/handlers/transport.py",
        "mcp_server/handlers/composition.py",
        "ableton_control/osc_client/client.py",
        "requirements.txt",
        "README.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ Project structure is correct")
        return True

async def run_tests():
    """Run all tests."""
    print("🧪 AbletonMCP Server Test Suite")
    print("=" * 40)
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Composition Handler", test_composition_handler),
        ("OSC Connection", test_osc_connection),
        ("MCP Tools", test_mcp_tools)
    ]
    
    results = {}
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name} test...")
        try:
            if asyncio.iscoroutinefunction(test_func):
                result = await test_func()
            else:
                result = test_func()
            results[test_name] = result
        except Exception as e:
            print(f"❌ Test {test_name} failed with error: {e}")
            results[test_name] = False
    
    # Print summary
    print("\n" + "=" * 40)
    print("📊 Test Summary:")
    
    passed = 0
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! The server should work correctly.")
        print("\n🚀 Next steps:")
        print("1. Install AbletonOSC: python install_ableton_osc.py")
        print("2. Configure Ableton Live with AbletonOSC") 
        print("3. Run the server: python -m mcp_server.main")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    asyncio.run(run_tests())