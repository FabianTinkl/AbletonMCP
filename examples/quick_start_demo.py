#!/usr/bin/env python3
"""
Quick Start Demo for AbletonMCP
Demonstrates basic usage of the MCP server components
"""

import asyncio
import logging

# Configure logging for demo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def demo_basic_operations():
    """Demonstrate basic Ableton Live operations."""
    print("🎵 AbletonMCP Quick Start Demo")
    print("=" * 40)
    
    try:
        from mcp_server.tools.ableton_tools import AbletonTools
        
        # Initialize connection to Ableton Live
        print("🔌 Connecting to Ableton Live...")
        tools = AbletonTools()
        connected = await tools.connect()
        
        if not connected:
            print("❌ Could not connect to Ableton Live!")
            print("Make sure Live is running with AbletonOSC enabled.")
            return
        
        print("✅ Connected to Ableton Live!")
        
        # Get Live info
        print("\n📊 Getting Live session info...")
        info = await tools.get_live_info()
        if info["status"] == "success":
            print(f"• Version: {info.get('live_version', 'Unknown')}")
            print(f"• Current Tempo: {info.get('current_tempo', 'Unknown')} BPM")
            print(f"• Track Count: {info.get('track_count', 'Unknown')}")
        
        # Set tempo for techno
        print("\n🥁 Setting tempo for techno...")
        result = await tools.set_tempo(132)
        print(f"• {result['message']}")
        
        # Create some tracks
        print("\n🎛️ Creating tracks...")
        tracks = [
            ("midi", "Kick"),
            ("midi", "Bass"),
            ("midi", "Lead"),
            ("audio", "Percussion"),
            ("return", "Reverb")
        ]
        
        for track_type, name in tracks:
            result = await tools.create_track(track_type, name)
            print(f"• {result['message']}")
            await asyncio.sleep(0.2)  # Small delay between operations
        
        print("\n🎵 Basic setup complete!")
        
        # Disconnect
        tools.disconnect()
        print("✅ Disconnected from Ableton Live")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run 'pip install -r requirements.txt' to install dependencies")
    except Exception as e:
        print(f"❌ Demo error: {e}")

async def demo_composition_ai():
    """Demonstrate AI composition capabilities."""
    print("\n🎼 AI Composition Demo")
    print("=" * 30)
    
    try:
        from mcp_server.handlers.composition import CompositionHandler
        from mcp_server.tools.ableton_tools import AbletonTools
        
        tools = AbletonTools()
        composer = CompositionHandler(tools)
        
        # Generate chord progression
        print("🎵 Generating industrial techno chord progression...")
        result = await composer.generate_chord_progression("Am", "industrial", 8)
        print("✅ Chord progression generated!")
        print(result[0]['text'][:200] + "...")  # Show preview
        
        # Generate drum pattern
        print("\n🥁 Creating industrial drum pattern...")
        result = await composer.create_drum_pattern("industrial", 4)
        print("✅ Drum pattern created!")
        
        print("\n🎶 AI composition demo complete!")
        
    except Exception as e:
        print(f"❌ Composition demo error: {e}")

def demo_knowledge_base():
    """Demonstrate the music theory knowledge base."""
    print("\n📚 Knowledge Base Demo")
    print("=" * 25)
    
    try:
        from knowledge_base.genres.techno import (
            TECHNO_PROGRESSIONS, 
            INDUSTRIAL_ELEMENTS,
            DRUM_PATTERNS,
            TECHNO_BPMS
        )
        
        print("🎼 Available techno chord progressions:")
        for key, progressions in TECHNO_PROGRESSIONS.items():
            print(f"• {key}: {len(progressions)} progressions")
            print(f"  Example: {' | '.join(progressions[0])}")
        
        print(f"\n🥁 Available drum patterns:")
        for pattern_type, patterns in DRUM_PATTERNS.items():
            print(f"• {pattern_type.title()}: {len(patterns)} variations")
        
        print(f"\n🎛️ Techno BPM ranges:")
        for style, (min_bpm, max_bpm) in TECHNO_BPMS.items():
            print(f"• {style.title()}: {min_bpm}-{max_bpm} BPM")
        
        print(f"\n🏭 Industrial elements:")
        for category, elements in INDUSTRIAL_ELEMENTS.items():
            print(f"• {category.title()}: {len(elements)} elements")
        
        print("\n✅ Knowledge base demo complete!")
        
    except ImportError as e:
        print(f"❌ Knowledge base import error: {e}")
    except Exception as e:
        print(f"❌ Knowledge base demo error: {e}")

async def main():
    """Run the full demo."""
    print("🚀 Starting AbletonMCP Demo Suite")
    print("This demo shows the core capabilities of the MCP server.\n")
    
    # Knowledge base demo (always works)
    demo_knowledge_base()
    
    # AI composition demo (doesn't need Live connection)
    await demo_composition_ai()
    
    # Basic operations demo (needs Live connection)
    await demo_basic_operations()
    
    print("\n" + "=" * 50)
    print("🎉 Demo Complete!")
    print("\n🔧 Next Steps:")
    print("1. Install AbletonOSC: python install_ableton_osc.py")
    print("2. Configure Ableton Live with AbletonOSC")
    print("3. Run the MCP server: python -m mcp_server.main")
    print("4. Configure Claude Desktop to use the server")
    print("5. Start creating music with natural language!")
    print("\n💡 Example Claude prompts:")
    print('• "Create a 64-bar industrial techno song at 132 BPM"')
    print('• "Generate a chord progression in Am for minimal techno"')
    print('• "Add a kick track and set the tempo to 128 BPM"')

if __name__ == "__main__":
    asyncio.run(main())