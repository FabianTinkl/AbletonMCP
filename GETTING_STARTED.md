# Getting Started with AbletonMCP

Welcome to AbletonMCP! This guide will help you set up and start using the AI music assistant for Ableton Live.

## What is AbletonMCP?

AbletonMCP is a Model Context Protocol (MCP) server that enables Claude Desktop to control Ableton Live through natural language commands. You can create entire techno and industrial music tracks just by describing what you want!

**Example prompts:**
- "Create a 64-bar industrial techno song at 132 BPM in A minor"
- "Generate a chord progression for minimal techno"
- "Add a kick track with an industrial drum pattern"

## Prerequisites

Before starting, make sure you have:

- **Python 3.10 or higher** installed
- **Ableton Live 11 or higher** (Standard or Suite recommended)
- **Claude Desktop** application
- A computer with sufficient RAM for audio production

## Step-by-Step Setup

### 1. Install Python Dependencies

```bash
# Clone or download this repository
cd AbletonMCP

# Install required packages
pip install -r requirements.txt
```

### 2. Install AbletonOSC

AbletonOSC is a remote script that allows external applications to control Ableton Live via OSC (Open Sound Control).

```bash
# Run the automated installer
python install_ableton_osc.py
```

**Manual Installation (if automated fails):**
1. Download AbletonOSC from: https://github.com/ideoforms/AbletonOSC
2. Extract to your Ableton Live Remote Scripts folder:
   - **macOS**: `~/Music/Ableton/User Library/Remote Scripts/`
   - **Windows**: `~/Documents/Ableton/User Library/Remote Scripts/`
3. Restart Ableton Live

### 3. Configure Ableton Live

1. Open Ableton Live
2. Go to **Preferences** → **Link/Tempo/MIDI**
3. In the **Control Surface** section:
   - Set dropdown to **"AbletonOSC"**
   - Leave Input and Output as **"None"**
4. Click **OK** and restart Live

### 4. Test Your Setup

```bash
# Run the comprehensive test suite
python test_server.py

# Or try the interactive demo
python examples/quick_start_demo.py
```

The tests will verify:
- ✅ Project structure
- ✅ OSC connection to Ableton Live  
- ✅ MCP tools functionality
- ✅ AI composition engine

### 5. Start the MCP Server

```bash
python -m mcp_server.main
```

You should see output like:
```
🎵 Starting AbletonMCP Server...
✅ AbletonTools connected successfully
INFO: MCP Server listening on stdio...
```

### 6. Configure Claude Desktop

Add the AbletonMCP server to your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/config.json`  
**Windows**: `%APPDATA%/Claude/config.json`

```json
{
  "mcpServers": {
    "ableton-mcp": {
      "command": "python",
      "args": ["-m", "mcp_server.main"],
      "cwd": "/path/to/your/AbletonMCP"
    }
  }
}
```

Replace `/path/to/your/AbletonMCP` with the actual path to this project.

### 7. Start Creating Music!

1. Restart Claude Desktop
2. Open a new conversation
3. Verify the MCP server is connected (you should see "AbletonMCP" in the server list)
4. Start making music with natural language!

## Example Usage

Here are some example prompts to get you started:

### Basic Transport Control
- "Set the tempo to 132 BPM"
- "Start playback"
- "Stop the music"

### Track Creation
- "Create a MIDI track called 'Bass'"
- "Add an audio track for percussion"
- "Create a return track for reverb"

### AI Music Generation
- "Create a techno song that's 64 bars long at 132 BPM with an industrial mood like Berghain"
- "Generate a chord progression in D minor for minimal techno"
- "Create an industrial drum pattern for 4 bars"

### Advanced Composition
- "Build a complete techno arrangement with intro, buildup, drop, and breakdown sections"
- "Add atmospheric pads using dark minor chord progressions"
- "Create a bassline that follows the current harmony"

## Troubleshooting

### "Could not connect to Ableton Live"
- ✅ Check that Ableton Live is running
- ✅ Verify AbletonOSC is installed and enabled in Live's preferences
- ✅ Restart both Live and the MCP server
- ✅ Check firewall settings aren't blocking ports 11000/11001

### "MCP Server not found in Claude Desktop"
- ✅ Verify the config.json path is correct
- ✅ Check that the "cwd" path points to this project directory
- ✅ Restart Claude Desktop after configuration changes
- ✅ Check the console for error messages

### "Import errors when running"
- ✅ Run `pip install -r requirements.txt`
- ✅ Verify Python 3.10+ is being used
- ✅ Consider using a virtual environment

### "Music generation doesn't sound right"
- ✅ This is Phase 1 - advanced AI music generation comes in later phases
- ✅ Try different musical keys and styles
- ✅ Experiment with different BPM ranges (120-150 for techno)

## What's Included in Phase 1

✅ **Core Infrastructure**
- MCP server with FastMCP framework
- OSC communication with Ableton Live
- Basic transport and track control
- Project management tools

✅ **AI Composition Engine**  
- Chord progression generation
- Genre-specific patterns (techno, industrial, minimal)
- Music theory knowledge base
- Basic song structure creation

✅ **Developer Tools**
- Comprehensive test suite
- Installation helpers
- Documentation and examples
- Error handling and logging

## Coming in Future Phases

🔄 **Phase 2**: Enhanced Music Production
- MIDI clip generation and editing
- Sample loading and management
- Advanced device control
- Real-time parameter automation

🔄 **Phase 3**: Advanced AI Features
- Melody and bassline generation
- Intelligent mixing and effects
- Style transfer and learning
- Complex arrangement tools

🔄 **Phase 4**: Professional Features
- Audio analysis and feedback
- Advanced music theory operations
- Custom sample libraries
- Integration with other DAWs

## Support

If you encounter issues:

1. **Run the test suite**: `python test_server.py`
2. **Check the logs** in the MCP server output
3. **Verify Ableton Live connection** with the demo: `python examples/quick_start_demo.py`
4. **Review this guide** for common solutions

## Contributing

This is an open-source project! Contributions are welcome for:
- Additional music genres and styles
- Improved AI composition algorithms  
- Better error handling and user experience
- Documentation and examples

---

🎵 **Happy Music Making!** 🎵

Start with simple commands and work your way up to complex compositions. The AI is designed to understand natural language, so describe what you want to hear and let AbletonMCP bring your musical ideas to life!