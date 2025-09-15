#!/usr/bin/env python3
"""
Offline Demo for AbletonMCP - Test without Ableton Live
Shows AI composition capabilities without requiring Live to be running
"""

import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

async def demo_ai_composition():
    """Demonstrate AI composition without Ableton Live."""
    print("🎵 AbletonMCP Offline Demo")
    print("=" * 40)
    print("This demo shows AI composition capabilities without requiring Ableton Live.\n")
    
    try:
        from mcp_server.tools.ableton_tools import AbletonTools
        from mcp_server.handlers.composition import CompositionHandler
        
        # Initialize tools (no connection needed for composition)
        tools = AbletonTools()
        composer = CompositionHandler(tools)
        
        print("🎼 **Generating Chord Progressions**\n")
        
        # Test different genres and keys
        test_cases = [
            ("Am", "industrial", 8),
            ("Dm", "minimal", 4),  
            ("Em", "underground", 6),
            ("Gm", "peak_time", 8)
        ]
        
        for key, genre, bars in test_cases:
            print(f"🎵 Generating {genre} progression in {key} ({bars} bars)...")
            result = await composer.generate_chord_progression(key, genre, bars)
            if result and len(result) > 0:
                print(result[0]['text'])
            else:
                print("   ⚠️ No result generated")
            print()
        
        print("🥁 **Generating Drum Patterns**\n")
        
        # Test different drum patterns
        drum_styles = ["industrial", "minimal", "peak_time", "underground"]
        
        for style in drum_styles:
            print(f"🥁 Creating {style} drum pattern (4 bars)...")
            result = await composer.create_drum_pattern(style, 4)
            if result:
                print("   ✅ Pattern generated successfully")
            else:
                print("   ⚠️ No pattern generated")
            print()
        
        print("🎶 **Music Theory Knowledge Base**\n")
        
        # Show knowledge base info
        from knowledge_base.genres.techno import (
            TECHNO_PROGRESSIONS, 
            TECHNO_BPMS,
            DRUM_PATTERNS,
            INDUSTRIAL_ELEMENTS
        )
        
        print("📊 Available chord progressions:")
        for key, progressions in TECHNO_PROGRESSIONS.items():
            print(f"   • {key}: {len(progressions)} variations")
            print(f"     Example: {' → '.join(progressions[0])}")
        
        print(f"\n🎛️ BPM ranges by style:")
        for style, (min_bpm, max_bpm) in TECHNO_BPMS.items():
            print(f"   • {style.title()}: {min_bpm}-{max_bpm} BPM")
        
        print(f"\n🥁 Drum pattern types:")
        for pattern_type, patterns in DRUM_PATTERNS.items():
            print(f"   • {pattern_type.title()}: {len(patterns)} variations")
        
        print(f"\n🏭 Industrial elements:")
        for category, elements in INDUSTRIAL_ELEMENTS.items():
            print(f"   • {category.title()}: {len(elements)} options")
        
        print("\n" + "=" * 50)
        print("✅ **Offline Demo Complete!**")
        print("\n🔧 **Next Steps:**")
        print("1. Install AbletonOSC: python install_ableton_osc.py")
        print("2. Configure Ableton Live 11 Suite with AbletonOSC")
        print("3. Run full test: python test_server.py (with Live running)")
        print("4. Start MCP server: python -m mcp_server.main")
        print("5. Configure Claude Desktop and start creating music!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run 'pip install -r requirements.txt' to install dependencies")
    except Exception as e:
        print(f"❌ Demo error: {e}")

if __name__ == "__main__":
    asyncio.run(demo_ai_composition())