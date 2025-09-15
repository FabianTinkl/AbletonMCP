#!/usr/bin/env python3
"""
AbletonMCP Server - Main Entry Point
"""

import asyncio
import logging
from typing import Dict, Any

from mcp.server import Server
from mcp.types import Tool
import mcp.server.stdio

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

class AbletonMCPServer:
    """Main MCP server for Ableton Live control."""
    
    def __init__(self):
        self.server = Server("ableton-mcp")
        self.ableton_tools = AbletonTools()
        self.handlers = {
            "transport": TransportHandler(self.ableton_tools),
            "project": ProjectHandler(self.ableton_tools),
            "track": TrackHandler(self.ableton_tools),
            "composition": CompositionHandler(self.ableton_tools),
            "midi": MIDIHandler(self.ableton_tools),
            "instruments": InstrumentsHandler(self.ableton_tools),
            "effects": EffectsHandler(self.ableton_tools),
            "samples": SamplesHandler(self.ableton_tools),
        }
        
        self._register_tools()
    
    def _register_tools(self):
        """Register all MCP tools."""
        logger.info("Registering MCP tools...")
        
        # Register tools using decorators
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            return await self._list_tools()
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> list[Dict[str, Any]]:
            return await self._call_tool(name, arguments)
        
        logger.info("✅ All tools registered successfully")
    
    async def _list_tools(self) -> list[Tool]:
        """List all available tools."""
        tools = []
        
        # Transport tools
        tools.extend([
            Tool(
                name="play",
                description="Start playback in Ableton Live",
                inputSchema={
                    "type": "object",
                    "properties": {},
                }
            ),
            Tool(
                name="stop", 
                description="Stop playback in Ableton Live",
                inputSchema={
                    "type": "object",
                    "properties": {},
                }
            ),
            Tool(
                name="set_tempo",
                description="Set the tempo (BPM) of the current Live set",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "bpm": {
                            "type": "number",
                            "description": "Tempo in beats per minute (60-200)",
                            "minimum": 60,
                            "maximum": 200
                        }
                    },
                    "required": ["bpm"]
                }
            ),
            Tool(
                name="create_track",
                description="Create a new track in Ableton Live",
                inputSchema={
                    "type": "object", 
                    "properties": {
                        "track_type": {
                            "type": "string",
                            "enum": ["audio", "midi", "return"],
                            "description": "Type of track to create"
                        },
                        "name": {
                            "type": "string",
                            "description": "Optional name for the track"
                        }
                    },
                    "required": ["track_type"]
                }
            ),
            Tool(
                name="generate_chord_progression",
                description="Generate a chord progression for a specific genre and key",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string", 
                            "description": "Musical key (e.g., 'C', 'Am', 'F#')"
                        },
                        "genre": {
                            "type": "string",
                            "enum": ["techno", "industrial", "house", "minimal"],
                            "description": "Genre style for the progression"
                        },
                        "length": {
                            "type": "integer",
                            "description": "Number of bars for the progression",
                            "minimum": 4,
                            "maximum": 64,
                            "default": 8
                        }
                    },
                    "required": ["key", "genre"]
                }
            ),
            Tool(
                name="create_techno_song",
                description="Create a complete techno song structure",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "bpm": {
                            "type": "number",
                            "description": "Tempo in BPM",
                            "minimum": 120,
                            "maximum": 150,
                            "default": 132
                        },
                        "bars": {
                            "type": "integer", 
                            "description": "Total length in bars",
                            "minimum": 32,
                            "maximum": 128,
                            "default": 64
                        },
                        "style": {
                            "type": "string",
                            "enum": ["industrial", "minimal", "peak_time", "underground"],
                            "description": "Techno substyle",
                            "default": "industrial"
                        },
                        "key": {
                            "type": "string",
                            "description": "Musical key (e.g., 'Am', 'Dm')",
                            "default": "Am"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="ping",
                description="Test connection to Ableton Live",
                inputSchema={
                    "type": "object",
                    "properties": {},
                }
            ),
            # MIDI Tools
            Tool(
                name="create_midi_clip",
                description="Create a MIDI clip with scale constraints and music theory integration",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "clip_slot": {"type": "integer", "description": "Clip slot index"},
                        "scale_name": {"type": "string", "description": "Musical scale", "default": "natural_minor"},
                        "root_note": {"type": "string", "description": "Root note", "default": "A"},
                        "length_bars": {"type": "integer", "description": "Clip length in bars", "default": 4},
                        "genre": {"type": "string", "description": "Genre for style", "default": "techno"}
                    },
                    "required": ["track_id", "clip_slot"]
                }
            ),
            Tool(
                name="add_notes",
                description="Add multiple notes to a MIDI clip with full parameter control",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "clip_id": {"type": "integer", "description": "Target clip index"},
                        "notes_data": {
                            "type": "array",
                            "description": "Array of note objects with pitch, start_time, duration, velocity",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "pitch": {"type": "integer", "minimum": 0, "maximum": 127},
                                    "start_time": {"type": "number", "minimum": 0},
                                    "duration": {"type": "number", "minimum": 0},
                                    "velocity": {"type": "integer", "minimum": 1, "maximum": 127}
                                }
                            }
                        }
                    },
                    "required": ["track_id", "clip_id", "notes_data"]
                }
            ),
            Tool(
                name="generate_melody",
                description="Generate AI-powered melody within scale constraints",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "clip_id": {"type": "integer", "description": "Target clip index"},
                        "scale_name": {"type": "string", "description": "Musical scale", "default": "natural_minor"},
                        "root_note": {"type": "string", "description": "Root note", "default": "A"},
                        "length_bars": {"type": "integer", "description": "Length in bars", "default": 4},
                        "note_density": {"type": "string", "enum": ["sparse", "medium", "dense"], "default": "medium"},
                        "genre": {"type": "string", "description": "Genre style", "default": "techno"}
                    },
                    "required": ["track_id", "clip_id"]
                }
            ),
            # Instruments Tools
            Tool(
                name="list_instruments",
                description="Browse available Ableton Live Suite instruments",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Filter by category (synths, drums, keys, world)"},
                        "search_term": {"type": "string", "description": "Search for instruments containing this term"}
                    },
                    "required": []
                }
            ),
            Tool(
                name="load_instrument",
                description="Load an instrument with optional preset onto a track",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "instrument_name": {"type": "string", "description": "Name of the instrument to load"},
                        "preset_name": {"type": "string", "description": "Optional preset name"},
                        "device_position": {"type": "integer", "description": "Position in device chain", "default": 0}
                    },
                    "required": ["track_id", "instrument_name"]
                }
            ),
            Tool(
                name="get_instrument_parameters",
                description="Get all controllable parameters for an instrument",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "device_id": {"type": "integer", "description": "Device index", "default": 0}
                    },
                    "required": ["track_id"]
                }
            ),
            Tool(
                name="set_instrument_parameter",
                description="Set a specific instrument parameter value",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "device_id": {"type": "integer", "description": "Device index"},
                        "parameter": {"description": "Parameter index (int) or name (str)"},
                        "value": {"type": "number", "minimum": 0.0, "maximum": 1.0, "description": "Parameter value"}
                    },
                    "required": ["track_id", "device_id", "parameter", "value"]
                }
            ),
            Tool(
                name="recommend_instruments",
                description="Get AI-powered instrument recommendations for genre and role",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "genre": {"type": "string", "description": "Musical genre"},
                        "role": {"type": "string", "description": "Instrument role", "default": "lead", "enum": ["lead", "bass", "pad", "drums"]}
                    },
                    "required": ["genre"]
                }
            ),
            # Effects Tools
            Tool(
                name="list_effects",
                description="Browse available Ableton Live effects by category",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Filter by category (dynamics, eq, reverb, delay, etc.)"},
                        "search_term": {"type": "string", "description": "Search for effects containing this term"}
                    },
                    "required": []
                }
            ),
            Tool(
                name="load_effect",
                description="Load an effect onto a track with intelligent positioning",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "effect_name": {"type": "string", "description": "Name of the effect to load"},
                        "preset_name": {"type": "string", "description": "Optional preset name"},
                        "chain_position": {"type": "integer", "description": "Position in effect chain"}
                    },
                    "required": ["track_id", "effect_name"]
                }
            ),
            Tool(
                name="set_effect_parameter",
                description="Set a specific effect parameter value",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "device_id": {"type": "integer", "description": "Device index"},
                        "parameter": {"description": "Parameter index (int) or name (str)"},
                        "value": {"type": "number", "minimum": 0.0, "maximum": 1.0, "description": "Parameter value"}
                    },
                    "required": ["track_id", "device_id", "parameter", "value"]
                }
            ),
            Tool(
                name="manage_effect_chain",
                description="Manage effect chain order and operations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "operation": {"type": "string", "enum": ["optimize", "remove", "reorder"], "description": "Operation type"},
                        "device_id": {"type": "integer", "description": "Device to operate on"},
                        "new_position": {"type": "integer", "description": "New position for reorder"}
                    },
                    "required": ["track_id", "operation"]
                }
            ),
            # Samples Tools  
            Tool(
                name="browse_samples",
                description="Browse sample library with intelligent filtering",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Sample category (drums, bass, melodic, vocals, fx)"},
                        "genre": {"type": "string", "description": "Musical genre filter"},
                        "bpm_range": {
                            "type": "array", 
                            "items": {"type": "integer"},
                            "minItems": 2,
                            "maxItems": 2,
                            "description": "BPM range [min, max]"
                        },
                        "characteristics": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Desired characteristics"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="load_sample",
                description="Load an audio sample with intelligent warp settings",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "clip_slot": {"type": "integer", "description": "Clip slot index"},
                        "sample_path": {"type": "string", "description": "Path or identifier for the sample"},
                        "warp_mode": {"type": "string", "enum": ["beats", "tones", "texture", "repitch", "complex", "complex_pro"], "default": "beats"},
                        "auto_warp": {"type": "boolean", "description": "Auto-detect optimal warp settings", "default": true}
                    },
                    "required": ["track_id", "clip_slot", "sample_path"]
                }
            ),
            Tool(
                name="set_warp_mode",
                description="Set warp mode and time-stretching settings for audio clip",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "track_id": {"type": "integer", "description": "Target track index"},
                        "clip_id": {"type": "integer", "description": "Target clip index"},
                        "warp_mode": {"type": "string", "enum": ["beats", "tones", "texture", "repitch", "complex", "complex_pro"]},
                        "preserve_formants": {"type": "boolean", "description": "Preserve formants during pitch shifting", "default": false}
                    },
                    "required": ["track_id", "clip_id", "warp_mode"]
                }
            ),
            Tool(
                name="recommend_samples",
                description="Get AI-powered sample recommendations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "genre": {"type": "string", "description": "Musical genre"},
                        "mood": {"type": "string", "enum": ["energetic", "chill", "dark", "uplifting"], "default": "energetic"},
                        "bpm": {"type": "integer", "description": "Target BPM for tempo matching"},
                        "key": {"type": "string", "description": "Musical key for harmonic matching"}
                    },
                    "required": ["genre"]
                }
            )
        ])
        
        return tools
    
    async def _call_tool(self, name: str, arguments: Dict[str, Any]) -> list[Dict[str, Any]]:
        """Call a specific tool."""
        logger.info(f"Calling tool: {name} with arguments: {arguments}")
        
        try:
            if name == "play":
                return await self.handlers["transport"].play()
            elif name == "stop":
                return await self.handlers["transport"].stop()
            elif name == "set_tempo":
                return await self.handlers["transport"].set_tempo(arguments["bpm"])
            elif name == "create_track":
                return await self.handlers["track"].create_track(
                    arguments["track_type"], 
                    arguments.get("name")
                )
            elif name == "generate_chord_progression":
                return await self.handlers["composition"].generate_chord_progression(
                    arguments["key"],
                    arguments["genre"], 
                    arguments.get("length", 8)
                )
            elif name == "create_techno_song":
                return await self.handlers["composition"].create_techno_song(
                    bpm=arguments.get("bpm", 132),
                    bars=arguments.get("bars", 64),
                    style=arguments.get("style", "industrial"),
                    key=arguments.get("key", "Am")
                )
            elif name == "create_midi_clip":
                return await self.handlers["midi"].create_midi_clip(
                    arguments["track_id"],
                    arguments["clip_slot"],
                    arguments.get("scale_name", "natural_minor"),
                    arguments.get("root_note", "A"),
                    arguments.get("length_bars", 4),
                    arguments.get("genre", "techno")
                )
            elif name == "add_notes":
                return await self.handlers["midi"].add_notes(
                    arguments["track_id"],
                    arguments["clip_id"],
                    arguments["notes_data"]
                )
            elif name == "generate_melody":
                return await self.handlers["midi"].generate_melody(
                    arguments["track_id"],
                    arguments["clip_id"],
                    arguments.get("scale_name", "natural_minor"),
                    arguments.get("root_note", "A"),
                    arguments.get("length_bars", 4),
                    arguments.get("note_density", "medium"),
                    arguments.get("genre", "techno")
                )
            elif name == "list_instruments":
                return await self.handlers["instruments"].list_instruments(
                    arguments.get("category"),
                    arguments.get("genre")
                )
            elif name == "load_instrument":
                return await self.handlers["instruments"].load_instrument(
                    arguments["track_id"],
                    arguments["instrument_name"],
                    arguments.get("preset_name")
                )
            elif name == "get_instrument_parameters":
                return await self.handlers["instruments"].get_instrument_parameters(
                    arguments["track_id"],
                    arguments["device_id"]
                )
            elif name == "set_instrument_parameter":
                return await self.handlers["instruments"].set_instrument_parameter(
                    arguments["track_id"],
                    arguments["device_id"],
                    arguments["parameter_name"],
                    arguments["value"]
                )
            elif name == "recommend_instruments":
                return await self.handlers["instruments"].recommend_instruments(
                    arguments["genre"],
                    arguments.get("mood"),
                    arguments.get("energy_level", "medium")
                )
            elif name == "list_effects":
                return await self.handlers["effects"].list_effects(
                    arguments.get("category")
                )
            elif name == "load_effect":
                return await self.handlers["effects"].load_effect(
                    arguments["track_id"],
                    arguments["effect_name"],
                    arguments.get("preset_name")
                )
            elif name == "set_effect_parameter":
                return await self.handlers["effects"].set_effect_parameter(
                    arguments["track_id"],
                    arguments["device_id"],
                    arguments["parameter_name"],
                    arguments["value"]
                )
            elif name == "manage_effect_chain":
                return await self.handlers["effects"].manage_effect_chain(
                    arguments["track_id"],
                    arguments["action"],
                    arguments.get("device_id"),
                    arguments.get("position")
                )
            elif name == "browse_samples":
                return await self.handlers["samples"].browse_samples(
                    arguments.get("category"),
                    arguments.get("genre"),
                    arguments.get("search_term"),
                    arguments.get("bpm_range")
                )
            elif name == "load_sample":
                return await self.handlers["samples"].load_sample(
                    arguments["track_id"],
                    arguments["clip_slot"],
                    arguments["sample_path"],
                    arguments.get("auto_warp", True)
                )
            elif name == "set_warp_mode":
                return await self.handlers["samples"].set_warp_mode(
                    arguments["track_id"],
                    arguments["clip_id"],
                    arguments["warp_mode"]
                )
            elif name == "recommend_samples":
                return await self.handlers["samples"].recommend_samples(
                    arguments["genre"],
                    arguments.get("mood"),
                    arguments.get("bpm"),
                    arguments.get("instrument_type")
                )
            elif name == "ping":
                result = await self.ableton_tools.ping()
                return [{"type": "text", "text": result.get("message", "Ping completed")}]
            else:
                return [{"type": "text", "text": f"Unknown tool: {name}"}]
                
        except Exception as e:
            logger.error(f"Error calling tool {name}: {str(e)}")
            return [{"type": "text", "text": f"Error: {str(e)}"}]
    
    async def run(self):
        """Run the MCP server."""
        import sys
        logger.info("🎵 Starting AbletonMCP Server...")
        print("🎵 Initializing AbletonMCP Server...", file=sys.stderr)
        
        try:
            # Initialize connection to Ableton Live
            print("🔌 Connecting to Ableton Live...", file=sys.stderr)
            await self.ableton_tools.connect()
            print("✅ Connected to Ableton Live", file=sys.stderr)
        except Exception as e:
            print(f"⚠️ Warning: Could not connect to Ableton Live: {e}", file=sys.stderr)
            print("Server will continue without Ableton connection", file=sys.stderr)
        
        try:
            print("📡 Starting MCP stdio server...", file=sys.stderr)
            # Run the MCP server
            async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
                print("🚀 MCP server ready for communication", file=sys.stderr)
                await self.server.run(
                    read_stream, 
                    write_stream,
                    self.server.create_initialization_options()
                )
        except Exception as e:
            print(f"❌ MCP server error: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            raise

async def main():
    """Main entry point."""
    try:
        print("🚀 Starting AbletonMCP Server...", file=sys.stderr)
        server = AbletonMCPServer()
        print("✅ Server instance created", file=sys.stderr)
        await server.run()
    except Exception as e:
        print(f"❌ Fatal error in main: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise

if __name__ == "__main__":
    import sys
    print("🎵 AbletonMCP starting up...", file=sys.stderr)
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"💥 Fatal startup error: {e}", file=sys.stderr)
        sys.exit(1)