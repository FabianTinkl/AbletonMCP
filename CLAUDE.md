# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AbletonMCP is a Model Context Protocol (MCP) server that enables Claude Desktop to control Ableton Live for AI-powered music production. The project specializes in techno and industrial music generation through natural language prompts.

## Architecture

### Core Components
- **MCP Server** (`mcp_server/`): Implements MCP protocol with FastMCP framework
- **Ableton Control** (`ableton_control/`): OSC client for Live communication via AbletonOSC
- **Music AI** (`music_ai/`): AI composition and generation engine using music21
- **Audio Processing** (`audio_processing/`): Audio analysis and processing utilities
- **Knowledge Base** (`knowledge_base/`): Music theory and genre-specific data

### Communication Flow
1. Claude Desktop → MCP Server (stdio/JSON-RPC)
2. MCP Server → Ableton Live (OSC messages via AbletonOSC, ports 11000/11001)
3. Music AI Engine → Chord/rhythm generation → OSC commands → Live tracks/clips

## Development Setup

### Prerequisites
- Python 3.10+
- Ableton Live 11+
- Claude Desktop

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install AbletonOSC remote script
python install_ableton_osc.py

# Test the setup
python test_server.py

# Run the server
python -m mcp_server.main
```

### Ableton Live Configuration
1. Install AbletonOSC in Live's Remote Scripts folder
2. Enable "AbletonOSC" in Live's MIDI preferences
3. Restart Live

## Common Commands

### Development
- `python test_server.py` - Run test suite
- `python setup.py` - Set up development environment
- `python install_ableton_osc.py` - Install AbletonOSC helper
- `python -m mcp_server.main` - Start MCP server

### Music Production via Claude
- "Create a 64-bar techno song at 132 BPM in Am with industrial elements"
- "Generate a chord progression for minimal techno in Dm"
- "Add a kick track with industrial drum pattern"
- "Set tempo to 128 BPM and start playback"

## Key MCP Tools

### Transport Control
- `play` - Start Ableton Live playback
- `stop` - Stop playback  
- `set_tempo` - Set BPM (60-200)

### Track Management  
- `create_track` - Create audio/MIDI/return tracks
- `create_clip` - Add clips to tracks
- `load_device` - Load instruments/effects

### AI Composition
- `generate_chord_progression` - Create chord progressions by genre/key
- `create_techno_song` - Generate complete song structures
- `create_drum_pattern` - Generate rhythmic patterns

## Music Theory Integration

The system uses:
- **music21** for music theory operations and MIDI generation
- **Genre Knowledge Base** with techno/industrial chord progressions, BPMs, and patterns
- **AI Composition Engine** for intelligent music generation
- **Scale and Harmony Systems** for coherent musical output

## Important Notes

### OSC Communication
- Uses AbletonOSC remote script for comprehensive Live API access  
- Default ports: 11000 (to Live), 11001 (from Live)
- Requires AbletonOSC to be properly installed and configured

### Music Generation
- Specializes in techno genres (minimal, industrial, peak-time, underground)
- Follows musical theory rules for coherent compositions
- Supports BPM ranges: 120-150 (genre-appropriate)
- Uses minor keys and industrial sound design principles

### Error Handling
- Graceful degradation when Live is not connected
- Comprehensive logging for debugging OSC communication
- Timeout handling for OSC message responses

## Testing

Run the full test suite to verify:
- Project structure integrity
- OSC connection to Ableton Live
- MCP tool functionality  
- Music AI composition engine

The test suite provides detailed feedback on connection status and suggests fixes for common issues.