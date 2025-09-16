#!/usr/bin/env python3
"""
AbletonMCP Server - FastMCP Simple Implementation
"""

import sys
import logging
from typing import Dict, Any, List, Optional

from mcp.server.fastmcp import FastMCP

from .handlers.transport import TransportHandler  
from .handlers.project import ProjectHandler
from .handlers.track import TrackHandler
from .handlers.composition import CompositionHandler
from .handlers.midi import MIDIHandler
from .handlers.instruments import InstrumentsHandler
from .handlers.effects import EffectsHandler
from .handlers.samples import SamplesHandler
from .tools.ableton_tools import AbletonTools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("ableton-mcp")

# Global server state - will be initialized at startup
ableton_tools: Optional[AbletonTools] = None
handlers: Dict[str, Any] = {}

async def init_server():
    """Initialize server components."""
    global ableton_tools, handlers
    
    print("🎵 Initializing AbletonMCP components...", file=sys.stderr)
    
    try:
        # Initialize AbletonTools
        ableton_tools = AbletonTools()
        print("✅ AbletonTools created", file=sys.stderr)
        
        # Initialize handlers
        handlers = {
            "transport": TransportHandler(ableton_tools),
            "project": ProjectHandler(ableton_tools),
            "track": TrackHandler(ableton_tools),
            "composition": CompositionHandler(ableton_tools),
            "midi": MIDIHandler(ableton_tools),
            "instruments": InstrumentsHandler(ableton_tools),
            "effects": EffectsHandler(ableton_tools),
            "samples": SamplesHandler(ableton_tools),
        }
        print("✅ All handlers initialized", file=sys.stderr)
        
        # Connect to Ableton Live
        print("🔌 Connecting to Ableton Live...", file=sys.stderr)
        try:
            await ableton_tools.connect()
            print("✅ Connected to Ableton Live", file=sys.stderr)
        except Exception as e:
            print(f"⚠️ Warning: Could not connect to Ableton Live: {e}", file=sys.stderr)
            print("Server will continue with limited functionality", file=sys.stderr)
        
        print("🚀 AbletonMCP server ready!", file=sys.stderr)
        
    except Exception as e:
        print(f"❌ Error during initialization: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise

# Transport Tools
@mcp.tool()
async def play() -> str:
    """Start playback in Ableton Live."""
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["transport"].play()
        return result[0]["text"] if result and "text" in result[0] else "Playback started"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def stop() -> str:
    """Stop playback in Ableton Live."""
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["transport"].stop()
        return result[0]["text"] if result and "text" in result[0] else "Playback stopped"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def set_tempo(bpm: float) -> str:
    """Set the tempo (BPM) of the current Live set.
    
    Args:
        bpm: Tempo in beats per minute (60-200)
    """
    if not 60 <= bpm <= 200:
        return "Error: BPM must be between 60 and 200"
    
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["transport"].set_tempo(bpm)
        return result[0]["text"] if result and "text" in result[0] else f"Tempo set to {bpm} BPM"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def ping() -> str:
    """Test connection to Ableton Live."""
    try:
        await ensure_initialized_async()
        if not ableton_tools:
            return "Error: Server initialization failed"
        result = await ableton_tools.ping()
        return result.get("message", "Ping completed")
    except Exception as e:
        return f"Error: {str(e)}"

# Track Management Tools
@mcp.tool()
async def create_track(track_type: str, name: Optional[str] = None) -> str:
    """Create a new track in Ableton Live.
    
    Args:
        track_type: Type of track to create (audio, midi, return)
        name: Optional name for the track
    """
    if track_type not in ["audio", "midi", "return"]:
        return "Error: track_type must be 'audio', 'midi', or 'return'"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["track"].create_track(track_type, name)
        return result[0]["text"] if result and "text" in result[0] else f"Created {track_type} track"
    except Exception as e:
        return f"Error: {str(e)}"

# Composition Tools
@mcp.tool()
async def generate_chord_progression(key: str, genre: str, length: int = 8) -> str:
    """Generate a chord progression for a specific genre and key.
    
    Args:
        key: Musical key (e.g., 'C', 'Am', 'F#')
        genre: Genre style (techno, industrial, house, minimal)
        length: Number of bars for the progression (4-64)
    """
    if genre not in ["techno", "industrial", "house", "minimal"]:
        return "Error: genre must be one of: techno, industrial, house, minimal"
    
    if not 4 <= length <= 64:
        return "Error: length must be between 4 and 64 bars"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["composition"].generate_chord_progression(key, genre, length)
        return result[0]["text"] if result and "text" in result[0] else f"Generated {length}-bar chord progression in {key} {genre}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def create_techno_song(bpm: float = 132, bars: int = 64, style: str = "industrial", key: str = "Am") -> str:
    """Create a complete techno song structure.
    
    Args:
        bpm: Tempo in BPM (120-150)
        bars: Total length in bars (32-128)  
        style: Techno substyle (industrial, minimal, peak_time, underground)
        key: Musical key (e.g., 'Am', 'Dm')
    """
    if not 120 <= bpm <= 150:
        return "Error: BPM must be between 120 and 150"
        
    if not 32 <= bars <= 128:
        return "Error: bars must be between 32 and 128"
        
    if style not in ["industrial", "minimal", "peak_time", "underground"]:
        return "Error: style must be one of: industrial, minimal, peak_time, underground"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["composition"].create_techno_song(bpm, bars, style, key)
        return result[0]["text"] if result and "text" in result[0] else f"Created {bars}-bar {style} techno song at {bpm} BPM in {key}"
    except Exception as e:
        return f"Error: {str(e)}"

# MIDI Tools
@mcp.tool()
async def create_midi_clip(track_id: int, clip_slot: int, scale_name: str = "natural_minor", 
                          root_note: str = "A", length_bars: int = 4, genre: str = "techno") -> str:
    """Create a MIDI clip with scale constraints and music theory integration.
    
    Args:
        track_id: Target track index
        clip_slot: Clip slot index
        scale_name: Musical scale (default: natural_minor)
        root_note: Root note (default: A)
        length_bars: Clip length in bars (default: 4)
        genre: Genre for style (default: techno)
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["midi"].create_midi_clip(
            track_id, clip_slot, scale_name, root_note, length_bars, genre
        )
        return result[0]["text"] if result and "text" in result[0] else f"Created MIDI clip in {root_note} {scale_name}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def generate_melody(track_id: int, clip_id: int, scale_name: str = "natural_minor",
                         root_note: str = "A", length_bars: int = 4, 
                         note_density: str = "medium", genre: str = "techno") -> str:
    """Generate AI-powered melody within scale constraints.
    
    Args:
        track_id: Target track index
        clip_id: Target clip index
        scale_name: Musical scale (default: natural_minor)
        root_note: Root note (default: A)
        length_bars: Length in bars (default: 4)
        note_density: Density level (sparse, medium, dense)
        genre: Genre style (default: techno)
    """
    if note_density not in ["sparse", "medium", "dense"]:
        return "Error: note_density must be 'sparse', 'medium', or 'dense'"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["midi"].generate_melody(
            track_id, clip_id, scale_name, root_note, length_bars, note_density, genre
        )
        return result[0]["text"] if result and "text" in result[0] else f"Generated {note_density} melody in {root_note} {scale_name}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def generate_drum_pattern(track_id: int, clip_id: int, pattern_style: str = "four_on_the_floor",
                               length_bars: int = 4, complexity: str = "medium", 
                               genre: str = "techno", swing: float = 0.0) -> str:
    """Generate complex drum patterns as MIDI notes with authentic drum mapping.
    
    Args:
        track_id: Target track index
        clip_id: Target clip index
        pattern_style: Drum pattern style (four_on_the_floor, breakbeat, latin, funk, industrial, jungle)
        length_bars: Pattern length in bars (default: 4)
        complexity: Pattern complexity (simple, medium, complex)
        genre: Musical genre for style adaptation (default: techno)
        swing: Swing timing 0.0-0.5 (0.0 = straight, 0.5 = max swing)
    """
    # Validate pattern style
    valid_patterns = ["four_on_the_floor", "breakbeat", "latin", "funk", "industrial", "jungle"]
    if pattern_style not in valid_patterns:
        return f"Error: pattern_style must be one of {', '.join(valid_patterns)}"
    
    # Validate complexity
    if complexity not in ["simple", "medium", "complex"]:
        return "Error: complexity must be 'simple', 'medium', or 'complex'"
    
    # Validate swing
    if not 0.0 <= swing <= 0.5:
        return "Error: swing must be between 0.0 (straight) and 0.5 (max swing)"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["midi"].drum_pattern(
            track_id, clip_id, pattern_style, length_bars, complexity, genre, swing
        )
        return result[0]["text"] if result and "text" in result[0] else f"Generated {complexity} {pattern_style} drum pattern ({length_bars} bars)"
    except Exception as e:
        return f"Error: {str(e)}"

# Instruments Tools
@mcp.tool()
async def list_instruments(category: Optional[str] = None, search_term: Optional[str] = None) -> str:
    """Browse available Ableton Live Suite instruments.
    
    Args:
        category: Filter by category (optional)
        search_term: Search for instruments containing this term (optional)
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["instruments"].list_instruments(category, search_term)
        return result[0]["text"] if result and "text" in result[0] else "Instruments listed"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def load_instrument(track_id: int, instrument_name: str, preset_name: Optional[str] = None) -> str:
    """Load an instrument with optional preset onto a track.
    
    Args:
        track_id: Target track index
        instrument_name: Name of the instrument to load
        preset_name: Optional preset name
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["instruments"].load_instrument(track_id, instrument_name, preset_name)
        return result[0]["text"] if result and "text" in result[0] else f"Loaded {instrument_name} on track {track_id}"
    except Exception as e:
        return f"Error: {str(e)}"

# Effects Tools
@mcp.tool()
async def list_effects(category: Optional[str] = None, search_term: Optional[str] = None) -> str:
    """Browse available Ableton Live effects by category.
    
    Args:
        category: Filter by category (optional)
        search_term: Search for effects containing this term (optional)
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["effects"].list_effects(category, search_term)
        return result[0]["text"] if result and "text" in result[0] else "Effects listed"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def load_effect(track_id: int, effect_name: str, preset_name: Optional[str] = None) -> str:
    """Load an effect onto a track with intelligent positioning.
    
    Args:
        track_id: Target track index
        effect_name: Name of the effect to load
        preset_name: Optional preset name
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["effects"].load_effect(track_id, effect_name, preset_name)
        return result[0]["text"] if result and "text" in result[0] else f"Loaded {effect_name} on track {track_id}"
    except Exception as e:
        return f"Error: {str(e)}"

# Samples Tools
@mcp.tool()
async def browse_samples(category: Optional[str] = None, genre: Optional[str] = None, 
                        characteristics: Optional[List[str]] = None) -> str:
    """Browse sample library with intelligent filtering.
    
    Args:
        category: Sample category (drums, bass, melodic, vocals, fx)
        genre: Musical genre filter
        characteristics: Desired characteristics
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        # Convert to format expected by handler
        bpm_range = None  # Could be added as parameter later
        result = await handlers["samples"].browse_samples(category, genre, None, bpm_range)
        return result[0]["text"] if result and "text" in result[0] else "Samples browsed"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def load_sample(track_id: int, clip_slot: int, sample_path: str, 
                     warp_mode: str = "beats", auto_warp: bool = True) -> str:
    """Load an audio sample with intelligent warp settings.
    
    Args:
        track_id: Target track index
        clip_slot: Clip slot index
        sample_path: Path or identifier for the sample
        warp_mode: Warp mode (beats, tones, texture, repitch, complex, complex_pro)
        auto_warp: Auto-detect optimal warp settings
    """
    valid_warp_modes = ["beats", "tones", "texture", "repitch", "complex", "complex_pro"]
    if warp_mode not in valid_warp_modes:
        return f"Error: warp_mode must be one of: {', '.join(valid_warp_modes)}"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["samples"].load_sample(track_id, clip_slot, sample_path, auto_warp)
        return result[0]["text"] if result and "text" in result[0] else f"Loaded sample {sample_path}"
    except Exception as e:
        return f"Error: {str(e)}"

# Lazy initialization approach
def ensure_initialized():
    """Ensure components are initialized (sync version for initial checks)."""
    global ableton_tools, handlers
    if not ableton_tools:
        print("⚠️ Server components not initialized yet", file=sys.stderr)
        return False
    return True

async def ensure_initialized_async():
    """Ensure components are initialized (async version for tool calls)."""
    global ableton_tools, handlers
    if not ableton_tools or not handlers:
        print("🔄 Lazy initializing components...", file=sys.stderr)
        await init_server()
    return True

# Update tool functions to use lazy initialization
# (This replaces the need for module-level async initialization)

if __name__ == "__main__":
    print("🎵 AbletonMCP FastMCP starting up...", file=sys.stderr)
    try:
        # FastMCP handles the asyncio.run() internally
        mcp.run()
    except Exception as e:
        print(f"💥 Fatal startup error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)