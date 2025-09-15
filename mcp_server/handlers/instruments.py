"""
Instruments Handler - Advanced instrument loading and parameter control
Provides comprehensive instrument management with preset loading, parameter discovery,
and real-time control of all instrument parameters.
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger(__name__)

class InstrumentsHandler:
    """Handles advanced instrument loading and parameter control operations."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
        
        # Ableton Live Suite instruments database
        self.live_instruments = {
            "synths": {
                "Wavetable": {
                    "category": "Wavetable Synthesizer",
                    "description": "Advanced wavetable synthesizer with dual oscillators",
                    "presets": ["Init Wavetable", "Ambient Pad", "Analog Pluck", "Bass Wobble", "Epic Lead"],
                    "key_parameters": ["Oscillator Position", "Filter Cutoff", "Filter Resonance", "ADSR Envelope"]
                },
                "Operator": {
                    "category": "FM Synthesizer", 
                    "description": "4-operator FM synthesizer",
                    "presets": ["Init FM", "Electric Piano", "Bass Growl", "Bell Tone", "Brass Section"],
                    "key_parameters": ["Operator A Level", "Operator B Level", "Filter Frequency", "LFO Rate"]
                },
                "Analog": {
                    "category": "Analog Synthesizer",
                    "description": "Virtual analog synthesizer with classic sound",
                    "presets": ["Init Analog", "Saw Lead", "Sub Bass", "Pad Warm", "Seq Pluck"],
                    "key_parameters": ["Oscillator 1 Level", "Oscillator 2 Level", "Filter Cutoff", "Resonance"]
                },
                "Bass": {
                    "category": "Bass Synthesizer",
                    "description": "Specialized bass synthesizer",
                    "presets": ["Sub Bass", "Analog Bass", "Dist Bass", "FM Bass", "Wobble Bass"],
                    "key_parameters": ["Sub Oscillator", "Glide Time", "Filter Cutoff", "Distortion"]
                }
            },
            "drums": {
                "Drum Machine": {
                    "category": "Drum Machine",
                    "description": "Classic drum machine sounds",
                    "presets": ["808 Kit", "909 Kit", "Vintage Kit", "Electronic Kit", "Hip Hop Kit"],
                    "key_parameters": ["Kick Tune", "Snare Tone", "Hi-Hat Decay", "Master Volume"]
                },
                "Impulse": {
                    "category": "Multi-sampling Drum Machine",
                    "description": "8-slot drum sampler",
                    "presets": ["Acoustic Kit", "Electronic Kit", "Vintage Kit", "Processed Kit", "Ambient Kit"],
                    "key_parameters": ["Slot Volume", "Slot Tune", "Slot Decay", "Filter Frequency"]
                },
                "Drum Kit": {
                    "category": "Acoustic Drum Kit",
                    "description": "Multi-sampled acoustic drum kit",
                    "presets": ["Studio Kit", "Vintage Kit", "Jazz Kit", "Rock Kit", "Brushes Kit"],
                    "key_parameters": ["Kick Volume", "Snare Tone", "Room Ambience", "Overhead Mix"]
                }
            },
            "keys": {
                "Electric Pianos": {
                    "category": "Electric Piano",
                    "description": "Classic electric piano sounds",
                    "presets": ["Vintage EP", "Suitcase EP", "Digital EP", "Clavinet", "Wurli"],
                    "key_parameters": ["Tone", "Bell", "Tremolo Speed", "Amp Drive"]
                },
                "Pianos": {
                    "category": "Acoustic Piano",
                    "description": "Sampled acoustic pianos",
                    "presets": ["Grand Piano", "Upright Piano", "Honky Tonk", "Prepared Piano", "Soft Piano"],
                    "key_parameters": ["Timbre", "Dynamics", "Pedal Noise", "String Resonance"]
                },
                "Organ": {
                    "category": "Organ",
                    "description": "Classic organ sounds",
                    "presets": ["Hammond B3", "Church Organ", "Farfisa", "Vox Continental", "Reed Organ"],
                    "key_parameters": ["Drawbar Settings", "Rotary Speed", "Percussion", "Vibrato"]
                }
            },
            "world": {
                "Ethnic Instruments": {
                    "category": "World Instruments",
                    "description": "Traditional instruments from around the world",
                    "presets": ["Sitar", "Tabla", "Gamelan", "Duduk", "Shakuhachi"],
                    "key_parameters": ["Instrument Type", "Playing Style", "Resonance", "Breath Control"]
                }
            }
        }
    
    async def list_instruments(
        self,
        category: Optional[str] = None,
        search_term: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Browse available Ableton Live Suite instruments.
        
        Args:
            category: Filter by category (synths, drums, keys, world)
            search_term: Search for instruments containing this term
        """
        logger.info(f"🎛️ Listing instruments: category={category}, search={search_term}")
        
        try:
            instruments_list = []
            
            for cat_name, category_instruments in self.live_instruments.items():
                if category and cat_name != category:
                    continue
                    
                for instrument_name, instrument_info in category_instruments.items():
                    if search_term and search_term.lower() not in instrument_name.lower():
                        continue
                    
                    instruments_list.append({
                        "name": instrument_name,
                        "category": cat_name,
                        "type": instrument_info["category"],
                        "description": instrument_info["description"],
                        "preset_count": len(instrument_info["presets"]),
                        "key_parameters": instrument_info["key_parameters"]
                    })
            
            response_text = f"""🎛️ **Available Instruments**

**Found {len(instruments_list)} instruments"""
            
            if category:
                response_text += f" in category '{category}'"
            if search_term:
                response_text += f" matching '{search_term}'"
            
            response_text += "**\n\n"
            
            # Group by category
            current_category = None
            for instrument in sorted(instruments_list, key=lambda x: (x["category"], x["name"])):
                if instrument["category"] != current_category:
                    current_category = instrument["category"]
                    response_text += f"**{current_category.upper()}:**\n"
                
                response_text += f"• **{instrument['name']}** - {instrument['description']}\n"
                response_text += f"  └ {instrument['preset_count']} presets, Key controls: {', '.join(instrument['key_parameters'][:3])}\n\n"
            
            response_text += """**Usage:**
• Use `load_instrument` to load an instrument on a track
• Use `list_instrument_presets` to see available presets
• Use `get_instrument_parameters` to see all controllable parameters"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error listing instruments: {e}")
            return [{"type": "text", "text": f"❌ Error listing instruments: {str(e)}"}]
    
    async def load_instrument(
        self,
        track_id: int,
        instrument_name: str,
        preset_name: Optional[str] = None,
        device_position: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Provide guidance for loading instruments (AbletonOSC cannot load devices dynamically).
        
        Args:
            track_id: Target track index
            instrument_name: Name of the instrument to load
            preset_name: Optional preset name to load
            device_position: Position in the device chain (0 = first)
        """
        logger.info(f"🎹 Providing guidance for instrument: {instrument_name} on track {track_id}")
        
        try:
            # Find instrument info
            instrument_info = None
            category = None
            
            for cat_name, category_instruments in self.live_instruments.items():
                if instrument_name in category_instruments:
                    instrument_info = category_instruments[instrument_name]
                    category = cat_name
                    break
            
            if not instrument_info:
                available = []
                for cat_instruments in self.live_instruments.values():
                    available.extend(cat_instruments.keys())
                return [{"type": "text", "text": f"❌ Instrument '{instrument_name}' not found. Available: {', '.join(available[:10])}"}]
            
            # Check if device already exists on track
            try:
                device_names = await self.ableton_tools.osc_client.get_devices_name(track_id)
                if device_names and any(instrument_name.lower() in name.lower() for name in device_names):
                    # Device already exists - provide control info
                    return await self._provide_existing_device_info(track_id, instrument_name, instrument_info, category, preset_name)
            except:
                pass  # Continue with manual loading instructions
            
            preset_info = f" with preset '{preset_name}'" if preset_name else ""
            
            response_text = f"""⚠️ **Manual Loading Required**

**AbletonOSC Limitation:**
• Cannot automatically load instruments
• Must manually load devices in Ableton Live first

**To Load {instrument_name}:**

**Step 1: Manual Loading in Live**
1. Select track {track_id} in Ableton Live
2. Open the Browser (press Cmd+Alt+B / Ctrl+Alt+B)
3. Navigate to: Instruments → {category.title()}
4. Drag "{instrument_name}" to track {track_id}
{f'5. Load preset "{preset_name}" from the instrument' if preset_name else '5. Use default settings or browse presets'}

**Step 2: After Loading**
Once loaded, use these MCP commands:
• `get_instrument_parameters` - See all controls
• `set_instrument_parameter` - Adjust settings remotely
• Check device with: `get_devices_on_track({track_id})`

**Instrument Details:**
• **{instrument_name}** - {instrument_info['description']}
• **Category:** {instrument_info['category']}
• **Key Controls:** {', '.join(instrument_info['key_parameters'][:4])}

**Available Presets ({len(instrument_info['presets'])}):**
{', '.join(instrument_info['presets'][:8])}

**Next Steps:**
1. Load the instrument manually in Ableton Live
2. Run this command again to verify loading
3. Use parameter control commands for remote adjustment

💡 **Tip:** Once loaded, all device parameters can be controlled remotely via MCP!"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error providing instrument guidance: {e}")
            return [{"type": "text", "text": f"❌ Error providing guidance: {str(e)}"}]
    
    async def _provide_existing_device_info(
        self, 
        track_id: int, 
        instrument_name: str, 
        instrument_info: dict, 
        category: str,
        preset_name: Optional[str]
    ) -> List[Dict[str, Any]]:
        """Provide info for already loaded device."""
        response_text = f"""✅ **{instrument_name} Found on Track {track_id}**

**Instrument Details:**
• **Name:** {instrument_name} 
• **Category:** {instrument_info['category']}
• **Description:** {instrument_info['description']}

**Current Status:**
• Device is loaded and ready for control
• All parameters accessible via MCP commands
• Real-time parameter adjustment available

**Key Parameters:**"""
        
        for param in instrument_info["key_parameters"]:
            response_text += f"\n• {param}"
        
        response_text += f"""

**Available Commands:**
• `get_instrument_parameters({track_id}, 0)` - View all parameters
• `set_instrument_parameter({track_id}, 0, param_name, value)` - Adjust controls
• `get_device_name({track_id}, 0)` - Confirm device identity

**Available Presets:**
{', '.join(instrument_info['presets'][:6])}

**Ready for Control!** 🎛️
The {instrument_name} is loaded and ready. Use parameter control commands to adjust settings in real-time."""
        
        return [{"type": "text", "text": response_text}]
    
    async def get_instrument_parameters(
        self,
        track_id: int,
        device_id: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Get all controllable parameters for an instrument.
        
        Args:
            track_id: Target track index
            device_id: Device index on the track (0 = first device)
        """
        logger.info(f"🔍 Getting parameters for instrument on track {track_id}, device {device_id}")
        
        try:
            # Get parameter names via OSC
            parameter_names = await self.ableton_tools.osc_client.send_and_wait(
                "/live/device/get/parameters/name",
                "/live/device/get/parameters/name",
                track_id, device_id
            )
            
            if not parameter_names:
                return [{"type": "text", "text": f"❌ Could not retrieve parameters for device on track {track_id}"}]
            
            # Get parameter values
            parameter_values = await self.ableton_tools.osc_client.send_and_wait(
                "/live/device/get/parameters/value",
                "/live/device/get/parameters/value", 
                track_id, device_id
            )
            
            # Combine names and values
            parameters = []
            for i, name in enumerate(parameter_names):
                value = parameter_values[i] if i < len(parameter_values) else 0.0
                parameters.append({
                    "index": i,
                    "name": name,
                    "value": value,
                    "normalized": value  # OSC typically returns 0.0-1.0
                })
            
            response_text = f"""🔍 **Instrument Parameters**

**Device Location:**
• Track: {track_id}
• Device Index: {device_id}
• Total Parameters: {len(parameters)}

**Parameters:**"""
            
            # Show parameters in groups
            for i, param in enumerate(parameters):
                if i < 20:  # Show first 20 parameters
                    percentage = int(param['value'] * 100)
                    response_text += f"\n• [{param['index']:2d}] {param['name']}: {percentage}%"
                elif i == 20:
                    response_text += f"\n• ... and {len(parameters) - 20} more parameters"
                    break
            
            response_text += f"""

**Usage:**
• Use parameter index or name with `set_instrument_parameter`
• Example: `set_instrument_parameter(track={track_id}, device={device_id}, param=0, value=0.75)`
• Values should be between 0.0 and 1.0 (0-100%)

**Key Parameters:** {', '.join([p['name'] for p in parameters[:5]])}"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error getting instrument parameters: {e}")
            return [{"type": "text", "text": f"❌ Error getting parameters: {str(e)}"}]
    
    async def set_instrument_parameter(
        self,
        track_id: int,
        device_id: int,
        parameter: Any,  # Can be index (int) or name (str)
        value: float
    ) -> List[Dict[str, Any]]:
        """
        Set a specific instrument parameter value.
        
        Args:
            track_id: Target track index
            device_id: Device index on the track
            parameter: Parameter index (int) or name (str)
            value: Parameter value (0.0 to 1.0)
        """
        logger.info(f"🎛️ Setting parameter for track {track_id}, device {device_id}: {parameter} = {value}")
        
        try:
            # Validate value range
            if not 0.0 <= value <= 1.0:
                return [{"type": "text", "text": f"❌ Parameter value must be between 0.0 and 1.0, got {value}"}]
            
            # If parameter is a string name, we need to get its index
            param_index = parameter
            param_name = str(parameter)
            
            if isinstance(parameter, str):
                # Get parameter names to find index
                parameter_names = await self.ableton_tools.osc_client.send_and_wait(
                    "/live/device/get/parameters/name",
                    "/live/device/get/parameters/name",
                    track_id, device_id
                )
                
                if parameter_names and parameter in parameter_names:
                    param_index = parameter_names.index(parameter)
                    param_name = parameter
                else:
                    return [{"type": "text", "text": f"❌ Parameter '{parameter}' not found"}]
            
            # Set the parameter value
            await self.ableton_tools.set_device_parameter(track_id, device_id, param_index, value)
            
            percentage = int(value * 100)
            
            response_text = f"""🎛️ **Parameter Updated Successfully**

**Parameter Details:**
• Name: {param_name}
• Index: {param_index}
• New Value: {value:.3f} ({percentage}%)

**Location:**
• Track: {track_id}
• Device: {device_id}

**Effect:**
The parameter has been updated and should be audible in your Ableton Live session. You can continue adjusting parameters in real-time for live performance or precise sound design."""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error setting instrument parameter: {e}")
            return [{"type": "text", "text": f"❌ Error setting parameter: {str(e)}"}]
    
    async def load_instrument_preset(
        self,
        track_id: int,
        device_id: int,
        preset_name: str
    ) -> List[Dict[str, Any]]:
        """
        Provide guidance for loading presets (AbletonOSC cannot load presets dynamically).
        
        Args:
            track_id: Target track index
            device_id: Device index on the track
            preset_name: Name of the preset to load
        """
        logger.info(f"💾 Providing preset guidance for '{preset_name}' on track {track_id}, device {device_id}")
        
        try:
            # Get device name first
            try:
                device_name = await self.ableton_tools.osc_client.get_device_name(track_id, device_id)
                device_class = await self.ableton_tools.osc_client.get_device_class_name(track_id, device_id)
            except:
                device_name = ["Unknown Device"]
                device_class = ["Unknown"]
            
            device_name_str = device_name[0] if device_name else "Unknown Device"
            device_class_str = device_class[0] if device_class else "Unknown"
            
            response_text = f"""⚠️ **Manual Preset Loading Required**

**AbletonOSC Limitation:**
• Cannot automatically load presets
• Must manually select presets in Ableton Live

**Current Device:**
• Track: {track_id}
• Device: {device_name_str} ({device_class_str})
• Target Preset: {preset_name}

**To Load Preset "{preset_name}":**

**Step 1: In Ableton Live**
1. Click on the device on track {track_id}
2. Look for preset/bank browser in device interface
3. Navigate to preset list or use device's preset buttons
4. Select "{preset_name}" from the available presets
5. Preset will load automatically

**Step 2: Verify Loading**
After loading preset, use:
• `get_instrument_parameters({track_id}, {device_id})` - See new parameter values
• `set_instrument_parameter` - Fine-tune the preset settings

**Alternative Approach:**
If the device supports it, you can try:
1. Using the device's built-in preset navigation
2. Right-click device → Browse presets
3. Use Previous/Next preset buttons on the device

**Parameter Control Available:**
Once preset is loaded, all parameters remain controllable via MCP commands for real-time adjustment and automation.

💡 **Note:** Preset must be loaded manually, but all parameter control works remotely!"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error providing preset guidance: {e}")
            return [{"type": "text", "text": f"❌ Error providing preset guidance: {str(e)}"}]
    
    async def recommend_instruments(
        self,
        genre: str,
        role: str = "lead"  # lead, bass, pad, drums, etc.
    ) -> List[Dict[str, Any]]:
        """
        Get AI-powered instrument recommendations for a specific genre and role.
        
        Args:
            genre: Musical genre (techno, house, trance, etc.)
            role: Instrument role (lead, bass, pad, drums, percussion)
        """
        logger.info(f"💡 Getting instrument recommendations: {genre} {role}")
        
        try:
            # Genre and role-based recommendations
            recommendations = {
                "techno": {
                    "lead": ["Wavetable", "Operator", "Analog"],
                    "bass": ["Bass", "Analog", "Operator"],
                    "pad": ["Wavetable", "Analog"],
                    "drums": ["Drum Machine", "Impulse"]
                },
                "house": {
                    "lead": ["Electric Pianos", "Analog", "Wavetable"],
                    "bass": ["Bass", "Analog"],
                    "pad": ["Analog", "Wavetable"],
                    "drums": ["Drum Machine", "Impulse"]
                },
                "trance": {
                    "lead": ["Wavetable", "Analog", "Operator"],
                    "bass": ["Bass", "Analog"],
                    "pad": ["Wavetable", "Analog"],
                    "drums": ["Drum Machine", "Impulse"]
                }
            }
            
            genre_recs = recommendations.get(genre.lower(), recommendations["techno"])
            role_instruments = genre_recs.get(role.lower(), genre_recs["lead"])
            
            response_text = f"""💡 **Instrument Recommendations**

**For {genre.title()} - {role.title()} Role:**

**Top Recommendations:**"""
            
            for i, instrument in enumerate(role_instruments, 1):
                if instrument in [inst for cat in self.live_instruments.values() for inst in cat.keys()]:
                    # Find the instrument info
                    for cat_instruments in self.live_instruments.values():
                        if instrument in cat_instruments:
                            info = cat_instruments[instrument]
                            response_text += f"\n\n**{i}. {instrument}**\n• {info['description']}\n• Recommended presets: {', '.join(info['presets'][:3])}"
                            break
            
            response_text += f"""

**Why these work for {genre.title()} {role}:**
• Sonic characteristics match genre expectations
• Parameter sets suitable for {role} sounds
• Proven presets for immediate use
• Professional sound quality

**Quick Start:**
Use `load_instrument(track_id=1, instrument_name="{role_instruments[0]}")` to get started immediately."""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            return [{"type": "text", "text": f"❌ Error getting recommendations: {str(e)}"}]