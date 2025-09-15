# AbletonMCP - AI Music Assistant for Ableton Live

A powerful MCP (Model Context Protocol) server that enables Claude Desktop to control Ableton Live for automated music production, specializing in techno and industrial music generation.

## Features

- **Natural Language Music Production**: Create complete tracks from text prompts
- **Genre-Specific AI**: Specialized in techno and industrial music styles
- **Real-time Ableton Control**: Full integration with Ableton Live via OSC
- **Intelligent Composition**: AI-powered melody, harmony, and rhythm generation
- **Professional Transport Control**: Play, stop, tempo control, and project management

## Prerequisites

- **Python 3.10 or higher**
- **Ableton Live 11 Suite** (or higher)
- **Claude Desktop** application
- At least 4GB RAM for music production

## Step-by-Step Setup Guide

### Step 1: Install Python Dependencies

```bash
# Navigate to the project directory
cd AbletonMCP

# Install required packages
pip install -r requirements.txt
```

### Step 2: Install AbletonOSC Remote Script

Run the automated installer:

```bash
python install_ableton_osc.py
```

**If the automated installer fails, install manually:**
1. Download AbletonOSC: https://github.com/ideoforms/AbletonOSC/archive/refs/heads/main.zip
2. Extract the ZIP file
3. Copy the `AbletonOSC-main` folder to your Ableton Remote Scripts directory:
   - **macOS**: `~/Music/Ableton/User Library/Remote Scripts/`
   - **Windows**: `%USERPROFILE%/Documents/Ableton/User Library/Remote Scripts/`
   - **Linux**: `~/ableton/User Library/Remote Scripts/`
4. Rename the folder from `AbletonOSC-main` to `AbletonOSC`

### Step 3: Configure Ableton Live 11 Suite

1. **Open Ableton Live 11 Suite**
2. Go to **Live → Preferences** (macOS) or **Options → Preferences** (Windows)
3. Click on the **Link/Tempo/MIDI** tab
4. In the **Control Surface** section:
   - Set the first dropdown to **"AbletonOSC"**
   - Leave **Input** and **Output** set to **"None"**
5. Click **OK** to save settings
6. **Restart Ableton Live** completely

### Step 4: Test Your Setup

**Test AI Composition (No Live Required):**
```bash
# Test the AI composition engine offline
python examples/offline_demo.py
```

**Test Full System (Requires Live Running):**
```bash
# Run the comprehensive test suite  
python test_server.py
```

You should see:
- ✅ Project Structure test passed
- ✅ Composition Handler test passed
- ✅ OSC Connection test passed (requires Live to be running)
- ✅ MCP Tools test passed

**If OSC tests fail:**
- Make sure Ableton Live 11 Suite is running
- Verify AbletonOSC is selected in Live's MIDI preferences
- Check that ports 11000/11001 aren't blocked by firewall
- The offline demo should still work perfectly!

### Step 5: Start the MCP Server

```bash
python -m mcp_server.main
```

You should see output like:
```
🎵 Starting AbletonMCP Server...
✅ AbletonTools connected successfully
INFO: MCP Server listening on stdio...
```

**Keep this terminal window open** - the server needs to run continuously.

### Step 6: Configure Claude Desktop

1. **Quit Claude Desktop** completely if it's running
2. Open your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

3. **Find your Python executable path**:
```bash
which python
```
This will show the full path to your Python installation (e.g., `/Users/yourname/anaconda3/bin/python` or `/opt/homebrew/bin/python3`).

4. **Create or edit the claude_desktop_config.json file** with this content:

```json
{
  "mcpServers": {
    "ableton-mcp": {
      "command": "/full/path/to/your/python",
      "args": ["-m", "mcp_server.main"],
      "cwd": "/full/path/to/your/AbletonMCP",
      "env": {
        "PYTHONPATH": "/full/path/to/your/AbletonMCP"
      }
    }
  }
}
```

**Important**: 
- Replace `/full/path/to/your/python` with the result from `which python` command
- Replace `/full/path/to/your/AbletonMCP` with the actual full path to your AbletonMCP project directory (appears twice)
- The `PYTHONPATH` environment variable is crucial for Python to find the mcp_server module
- Use absolute paths, not relative paths like `python` or `~/`

5. **Save the file** and **restart Claude Desktop**

### Step 7: Verify Connection in Claude Desktop

1. Open Claude Desktop
2. Start a new conversation
3. You should see **"AbletonMCP"** listed in the server connections at the bottom
4. If it shows as connected, you're ready to make music!

## Example Prompts - Test All Features

### Basic Transport Control

Try these prompts in Claude Desktop:

**1. Test Connection**
```
Ping Ableton Live to test the connection
```

**2. Tempo Control**
```
Set the tempo to 132 BPM
```

**3. Transport Control**
```
Start playback
```
```
Stop playback after 8 seconds
```

### Track Management

**4. Create Basic Tracks**
```
Create a MIDI track called "Kick Drum"
```
```
Create a MIDI track called "Bass Synth" 
```
```
Create an audio track called "Percussion"
```
```
Create a return track called "Industrial Reverb"
```

### AI Music Generation

**5. Generate Chord Progressions**
```
Generate a chord progression in A minor for industrial techno, 8 bars long
```
```
Generate a chord progression in D minor for minimal techno, 4 bars
```

**6. Create Drum Patterns**
```
Create an industrial drum pattern for 4 bars
```

**7. Complete Song Generation**
```
Create a 64-bar industrial techno song at 132 BPM in A minor
```

### Advanced Features

**8. Project Information**
```
Get information about the current Ableton Live session
```

**9. Tempo Variations**
```
Set tempo to 128 BPM for underground techno
```
```
Set tempo to 140 BPM for hard techno
```

### Complex Compositions

**10. Full Production Workflow**
```
Create a complete techno track: Set tempo to 132 BPM, create kick, bass, lead, and percussion tracks, then generate an industrial techno song structure for 64 bars in A minor. Add atmospheric elements and start playback to preview.
```

## Expected Results in Ableton Live

When you run these prompts, you should see:

1. **Transport changes**: BPM adjustments, play/stop states
2. **New tracks appearing**: Named tracks in the Session View
3. **MIDI clips generated**: Containing chord progressions and patterns
4. **Console feedback**: Success messages in both Claude and the MCP server terminal

## Troubleshooting

### "Could not connect to Ableton Live"
- ✅ Ensure Ableton Live is running
- ✅ Verify AbletonOSC is installed and enabled
- ✅ Check Live's MIDI preferences show "AbletonOSC" selected
- ✅ Restart both Live and the MCP server

### "MCP Server not found in Claude Desktop"
- ✅ Check the config.json path is correct for your OS
- ✅ Verify the "cwd" path points to your AbletonMCP directory
- ✅ Make sure to restart Claude Desktop after config changes
- ✅ Check Claude Desktop's console for error messages

### "Permission denied" or import errors
- ✅ Run `pip install -r requirements.txt` 
- ✅ Use Python 3.10 or higher
- ✅ Consider using a virtual environment

### Music generation not working as expected
- ✅ This is Phase 1 - basic functionality
- ✅ Try different musical keys (Am, Dm, Em, Gm)
- ✅ Experiment with different BPM ranges (120-150)
- ✅ Use genre keywords: "industrial", "minimal", "underground"

## Next Steps

Once everything is working:

1. **Experiment** with different musical styles and BPMs
2. **Combine prompts** for complex arrangements
3. **Use Live's tools** to further refine the AI-generated content
4. **Save your projects** in Ableton Live as usual

## What's Working in Phase 1

✅ **Transport Control** - Play/stop, tempo setting  
✅ **Track Creation** - MIDI, audio, and return tracks  
✅ **AI Chord Progressions** - Genre-specific harmony generation  
✅ **Basic Song Structures** - Multi-section arrangements  
✅ **OSC Communication** - Real-time Live control  
✅ **Music Theory Integration** - Coherent musical output

## Project Structure

- `mcp_server/` - MCP server implementation
- `ableton_control/` - OSC and Ableton Live API wrapper  
- `music_ai/` - AI composition and generation engine
- `audio_processing/` - Audio analysis and processing tools
- `knowledge_base/` - Music theory and genre-specific data
- `samples/` - Audio content library
- `tests/` - Test suite

## Development

Install development dependencies:
```bash
pip install -r requirements.txt
```

Run tests:
```bash
pytest
```

Format code:
```bash
black . && isort .
```

## License

MIT License - see LICENSE file for details.