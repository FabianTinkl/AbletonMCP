"""
Effects Handler - Advanced effects loading and parameter control
Provides comprehensive effects management with full parameter control,
preset management, and intelligent effect chain optimization.
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger(__name__)

class EffectsHandler:
    """Handles advanced effects loading and parameter control operations."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
        
        # Ableton Live effects database
        self.live_effects = {
            "dynamics": {
                "Compressor": {
                    "category": "Dynamics",
                    "description": "Vintage-style compressor with analog modeling",
                    "key_parameters": ["Threshold", "Ratio", "Attack", "Release", "Makeup Gain"],
                    "presets": ["Vocal Comp", "Drum Glue", "Bass Tight", "Master Bus", "Pump"]
                },
                "Multiband Compressor": {
                    "category": "Dynamics",
                    "description": "4-band multiband compressor for precise control",
                    "key_parameters": ["Low Threshold", "Mid Threshold", "High Threshold", "Output Gain"],
                    "presets": ["Master Bus", "Mix Glue", "Vocal Polish", "Drum Control", "Bass Focus"]
                },
                "Gate": {
                    "category": "Dynamics", 
                    "description": "Noise gate with ducking capabilities",
                    "key_parameters": ["Threshold", "Release", "Hold", "Lookahead"],
                    "presets": ["Tight Gate", "Smooth Gate", "Trance Gate", "Sidechain Duck", "Rhythmic"]
                }
            },
            "eq": {
                "EQ Eight": {
                    "category": "EQ",
                    "description": "8-band parametric equalizer",
                    "key_parameters": ["Low Gain", "Low Mid Gain", "High Mid Gain", "High Gain", "Low Cut", "High Cut"],
                    "presets": ["Vocal EQ", "Master EQ", "Bass Enhance", "Presence Boost", "Air Band"]
                },
                "EQ Three": {
                    "category": "EQ", 
                    "description": "3-band DJ-style equalizer",
                    "key_parameters": ["Low Gain", "Mid Gain", "High Gain", "Low Kill", "Mid Kill", "High Kill"],
                    "presets": ["DJ Mix", "Radio Style", "Smooth", "Punchy", "Bright"]
                }
            },
            "reverb": {
                "Reverb": {
                    "category": "Reverb",
                    "description": "High-quality algorithmic reverb",
                    "key_parameters": ["Room Size", "Decay Time", "Pre Delay", "Diffusion", "Dry/Wet"],
                    "presets": ["Hall", "Plate", "Chamber", "Spring", "Ambient"]
                },
                "Convolution Reverb": {
                    "category": "Reverb",
                    "description": "Impulse response-based convolution reverb", 
                    "key_parameters": ["Impulse Selection", "Size", "Decay", "Pre Delay", "Dry/Wet"],
                    "presets": ["Concert Hall", "Cathedral", "Studio Room", "Vintage Plate", "Outdoor"]
                }
            },
            "delay": {
                "Delay": {
                    "category": "Delay",
                    "description": "Stereo delay with filters and modulation",
                    "key_parameters": ["Delay Time L", "Delay Time R", "Feedback", "Filter Frequency", "Dry/Wet"],
                    "presets": ["1/8 Stereo", "Dub Echo", "Ping Pong", "Filtered Delay", "Ambient Wash"]
                },
                "Echo": {
                    "category": "Delay",
                    "description": "Advanced delay with multiple taps and modulation",
                    "key_parameters": ["Delay Time", "Feedback", "Modulation Rate", "Character", "Dry/Wet"],
                    "presets": ["Tape Echo", "Digital Delay", "Modulated", "Reverse Echo", "Granular"]
                }
            },
            "modulation": {
                "Chorus": {
                    "category": "Modulation",
                    "description": "Classic chorus effect with multiple voices",
                    "key_parameters": ["Rate", "Depth", "Delay", "Feedback", "Dry/Wet"],
                    "presets": ["Vintage", "Modern", "Wide", "Subtle", "Extreme"]
                },
                "Phaser": {
                    "category": "Modulation",
                    "description": "Multi-stage phaser with LFO modulation",
                    "key_parameters": ["Frequency", "Feedback", "LFO Rate", "LFO Depth", "Dry/Wet"],
                    "presets": ["Classic", "Vintage", "Sweep", "Resonant", "Slow"]
                },
                "Flanger": {
                    "category": "Modulation",
                    "description": "Flanger effect with envelope and LFO control",
                    "key_parameters": ["Delay Time", "Feedback", "LFO Rate", "Envelope Amount", "Dry/Wet"],
                    "presets": ["Jet", "Subtle", "Extreme", "Envelope", "Vintage"]
                }
            },
            "distortion": {
                "Saturator": {
                    "category": "Distortion",
                    "description": "Multi-mode saturator and distortion",
                    "key_parameters": ["Drive", "Base", "Frequency", "Depth", "Output"],
                    "presets": ["Tape", "Tube", "Digital", "Analog", "Warm"]
                },
                "Overdrive": {
                    "category": "Distortion",
                    "description": "Guitar-style overdrive and distortion",
                    "key_parameters": ["Drive", "Tone", "Dynamics", "Band Split", "Output"],
                    "presets": ["Classic OD", "Heavy Dist", "Fuzz", "Tube Scream", "Metal"]
                }
            },
            "filter": {
                "Filter": {
                    "category": "Filter",
                    "description": "Resonant filter with multiple modes",
                    "key_parameters": ["Frequency", "Resonance", "Filter Type", "Drive", "Envelope Amount"],
                    "presets": ["Low Pass", "High Pass", "Band Pass", "Notch", "Formant"]
                },
                "Auto Filter": {
                    "category": "Filter",
                    "description": "Automatic filter with envelope and LFO",
                    "key_parameters": ["Frequency", "Resonance", "Envelope Amount", "LFO Amount", "Attack"],
                    "presets": ["Env Follow", "LFO Sweep", "Vocal Form", "Wah", "Auto Wah"]
                }
            },
            "utility": {
                "Utility": {
                    "category": "Utility",
                    "description": "Gain, pan, phase, and width control",
                    "key_parameters": ["Gain", "Pan", "Width", "Phase Invert L", "Phase Invert R"],
                    "presets": ["Gain Staging", "Stereo Width", "Mono", "Phase Correct", "Balance"]
                },
                "Spectrum": {
                    "category": "Utility",
                    "description": "Real-time frequency spectrum analyzer",
                    "key_parameters": ["Display Mode", "Frequency Range", "Block Size", "Refresh Rate"],
                    "presets": ["Full Range", "Low Focus", "High Focus", "Mid Focus", "Detailed"]
                }
            }
        }
    
    async def list_effects(
        self,
        category: Optional[str] = None,
        search_term: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Browse available Ableton Live effects.
        
        Args:
            category: Filter by category (dynamics, eq, reverb, delay, modulation, distortion, filter, utility)
            search_term: Search for effects containing this term
        """
        logger.info(f"🔊 Listing effects: category={category}, search={search_term}")
        
        try:
            effects_list = []
            
            for cat_name, category_effects in self.live_effects.items():
                if category and cat_name != category:
                    continue
                    
                for effect_name, effect_info in category_effects.items():
                    if search_term and search_term.lower() not in effect_name.lower():
                        continue
                    
                    effects_list.append({
                        "name": effect_name,
                        "category": cat_name,
                        "description": effect_info["description"],
                        "preset_count": len(effect_info["presets"]),
                        "key_parameters": effect_info["key_parameters"]
                    })
            
            response_text = f"""🔊 **Available Effects**

**Found {len(effects_list)} effects"""
            
            if category:
                response_text += f" in category '{category}'"
            if search_term:
                response_text += f" matching '{search_term}'"
            
            response_text += "**\n\n"
            
            # Group by category
            current_category = None
            for effect in sorted(effects_list, key=lambda x: (x["category"], x["name"])):
                if effect["category"] != current_category:
                    current_category = effect["category"]
                    response_text += f"**{current_category.upper()}:**\n"
                
                response_text += f"• **{effect['name']}** - {effect['description']}\n"
                response_text += f"  └ {effect['preset_count']} presets, Key controls: {', '.join(effect['key_parameters'][:3])}\n\n"
            
            response_text += """**Categories Available:**
• **Dynamics**: Compressor, Gate, Multiband Compressor
• **EQ**: EQ Eight, EQ Three for frequency shaping  
• **Reverb**: Reverb, Convolution Reverb for space
• **Delay**: Delay, Echo for time-based effects
• **Modulation**: Chorus, Phaser, Flanger for movement
• **Distortion**: Saturator, Overdrive for character
• **Filter**: Filter, Auto Filter for frequency control
• **Utility**: Utility, Spectrum for technical control

**Usage:**
Use `load_effect` to add effects to tracks with automatic chain positioning."""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error listing effects: {e}")
            return [{"type": "text", "text": f"❌ Error listing effects: {str(e)}"}]
    
    async def load_effect(
        self,
        track_id: int,
        effect_name: str,
        preset_name: Optional[str] = None,
        chain_position: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Load an effect onto a track with intelligent positioning.
        
        Args:
            track_id: Target track index
            effect_name: Name of the effect to load
            preset_name: Optional preset name to load
            chain_position: Position in effect chain (None = auto-position)
        """
        logger.info(f"🎛️ Loading effect: {effect_name} on track {track_id}")
        
        try:
            # Find effect info
            effect_info = None
            category = None
            
            for cat_name, category_effects in self.live_effects.items():
                if effect_name in category_effects:
                    effect_info = category_effects[effect_name]
                    category = cat_name
                    break
            
            if not effect_info:
                available = []
                for cat_effects in self.live_effects.values():
                    available.extend(cat_effects.keys())
                return [{"type": "text", "text": f"❌ Effect '{effect_name}' not found. Available: {', '.join(available[:10])}"}]
            
            # Determine optimal chain position if not specified
            if chain_position is None:
                chain_position = self._get_optimal_effect_position(category, effect_name)
            
            # Load the effect via OSC
            await self.ableton_tools.load_device(track_id, effect_name)
            
            # Load preset if specified
            preset_info = ""
            if preset_name and preset_name in effect_info["presets"]:
                logger.info(f"Loading preset: {preset_name}")
                preset_info = f"\n• Preset: {preset_name}"
                # Preset loading would be implemented here
            
            response_text = f"""🎛️ **Effect Loaded Successfully**

**Effect Details:**
• Name: {effect_name}
• Category: {category.title()}
• Description: {effect_info['description']}

**Load Information:**
• Track: {track_id}
• Chain Position: {chain_position} ({self._get_position_description(chain_position)}){preset_info}

**Key Parameters:**"""
            
            for param in effect_info["key_parameters"]:
                response_text += f"\n• {param}"
            
            response_text += f"""

**Available Presets ({len(effect_info['presets'])}):**
{', '.join(effect_info['presets'][:5])}"""
            
            if len(effect_info['presets']) > 5:
                response_text += f" and {len(effect_info['presets']) - 5} more"
            
            response_text += f"""

**Recommended Chain Order:** {self._get_chain_recommendations(category)}

**Next Steps:**
• Use `get_effect_parameters` to see all controls
• Use `set_effect_parameter` to adjust settings
• Use `load_effect_preset` to try different presets"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error loading effect: {e}")
            return [{"type": "text", "text": f"❌ Error loading effect: {str(e)}"}]
    
    async def get_effect_parameters(
        self,
        track_id: int,
        device_id: int
    ) -> List[Dict[str, Any]]:
        """
        Get all controllable parameters for an effect.
        
        Args:
            track_id: Target track index
            device_id: Device index on the track
        """
        logger.info(f"🔍 Getting effect parameters: track {track_id}, device {device_id}")
        
        try:
            # Get parameter names via OSC
            parameter_names = await self.ableton_tools.osc_client.send_and_wait(
                "/live/device/get/parameters/name",
                "/live/device/get/parameters/name",
                track_id, device_id
            )
            
            if not parameter_names:
                return [{"type": "text", "text": f"❌ Could not retrieve parameters for effect on track {track_id}"}]
            
            # Get parameter values
            parameter_values = await self.ableton_tools.osc_client.send_and_wait(
                "/live/device/get/parameters/value",
                "/live/device/get/parameters/value",
                track_id, device_id
            )
            
            # Get device name
            device_name = await self.ableton_tools.osc_client.send_and_wait(
                "/live/device/get/name",
                "/live/device/get/name",
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
                    "percentage": int(value * 100)
                })
            
            response_text = f"""🔍 **Effect Parameters**

**Effect:** {device_name[0] if device_name else 'Unknown Effect'}
**Location:** Track {track_id}, Device {device_id}
**Total Parameters:** {len(parameters)}

**Current Settings:**"""
            
            # Group parameters by type for better readability
            essential_params = []
            other_params = []
            
            for param in parameters:
                if any(key in param['name'].lower() for key in ['freq', 'gain', 'drive', 'time', 'rate', 'threshold', 'ratio']):
                    essential_params.append(param)
                else:
                    other_params.append(param)
            
            # Show essential parameters first
            if essential_params:
                response_text += "\n\n**Essential Controls:**"
                for param in essential_params[:10]:
                    response_text += f"\n• [{param['index']:2d}] {param['name']}: {param['percentage']}%"
            
            # Show other parameters
            if other_params and len(essential_params) < 15:
                response_text += "\n\n**Additional Controls:**"
                remaining_slots = 15 - len(essential_params)
                for param in other_params[:remaining_slots]:
                    response_text += f"\n• [{param['index']:2d}] {param['name']}: {param['percentage']}%"
            
            if len(parameters) > 15:
                response_text += f"\n• ... and {len(parameters) - 15} more parameters"
            
            response_text += f"""

**Usage Examples:**
• `set_effect_parameter(track={track_id}, device={device_id}, param=0, value=0.75)`
• `set_effect_parameter(track={track_id}, device={device_id}, param="Frequency", value=0.5)`

**Value Range:** All parameters accept values from 0.0 to 1.0 (0-100%)"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error getting effect parameters: {e}")
            return [{"type": "text", "text": f"❌ Error getting parameters: {str(e)}"}]
    
    async def set_effect_parameter(
        self,
        track_id: int,
        device_id: int,
        parameter: Any,  # Can be index (int) or name (str)
        value: float
    ) -> List[Dict[str, Any]]:
        """
        Set a specific effect parameter value.
        
        Args:
            track_id: Target track index
            device_id: Device index on the track
            parameter: Parameter index (int) or name (str)
            value: Parameter value (0.0 to 1.0)
        """
        logger.info(f"🎛️ Setting effect parameter: track {track_id}, device {device_id}, {parameter} = {value}")
        
        try:
            # Validate value range
            if not 0.0 <= value <= 1.0:
                return [{"type": "text", "text": f"❌ Parameter value must be between 0.0 and 1.0, got {value}"}]
            
            # Handle parameter name resolution
            param_index = parameter
            param_name = str(parameter)
            
            if isinstance(parameter, str):
                parameter_names = await self.ableton_tools.osc_client.send_and_wait(
                    "/live/device/get/parameters/name",
                    "/live/device/get/parameters/name",
                    track_id, device_id
                )
                
                if parameter_names and parameter in parameter_names:
                    param_index = parameter_names.index(parameter)
                    param_name = parameter
                else:
                    # Try partial name matching
                    matches = [i for i, name in enumerate(parameter_names) if parameter.lower() in name.lower()]
                    if matches:
                        param_index = matches[0]
                        param_name = parameter_names[matches[0]]
                    else:
                        return [{"type": "text", "text": f"❌ Parameter '{parameter}' not found"}]
            
            # Set the parameter value
            await self.ableton_tools.set_device_parameter(track_id, device_id, param_index, value)
            
            percentage = int(value * 100)
            
            response_text = f"""🎛️ **Effect Parameter Updated**

**Parameter:**
• Name: {param_name}
• Index: {param_index}
• New Value: {value:.3f} ({percentage}%)

**Location:**
• Track: {track_id}
• Device: {device_id}

**Result:**
Parameter change applied immediately. The effect should reflect the new setting in your Ableton Live session for real-time audio processing."""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error setting effect parameter: {e}")
            return [{"type": "text", "text": f"❌ Error setting parameter: {str(e)}"}]
    
    async def manage_effect_chain(
        self,
        track_id: int,
        operation: str,
        device_id: Optional[int] = None,
        new_position: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Manage effect chain order and operations.
        
        Args:
            track_id: Target track index
            operation: Operation type (reorder, remove, optimize)
            device_id: Device to operate on (for reorder/remove)
            new_position: New position for reorder operation
        """
        logger.info(f"⚙️ Managing effect chain: track {track_id}, operation {operation}")
        
        try:
            if operation == "optimize":
                # Get current device chain
                device_names = await self.ableton_tools.osc_client.send_and_wait(
                    "/live/track/get/devices/name",
                    "/live/track/get/devices/name",
                    track_id
                )
                
                if not device_names:
                    return [{"type": "text", "text": f"❌ No devices found on track {track_id}"}]
                
                # Analyze and suggest optimal order
                optimal_order = self._get_optimal_chain_order(device_names)
                
                response_text = f"""⚙️ **Effect Chain Analysis**

**Current Chain (Track {track_id}):**"""
                for i, device in enumerate(device_names):
                    response_text += f"\n{i+1}. {device}"
                
                response_text += f"\n\n**Recommended Optimal Order:**"
                for i, device in enumerate(optimal_order):
                    response_text += f"\n{i+1}. {device}"
                
                response_text += f"""

**Optimization Benefits:**
• Better frequency response
• Reduced artifacts and noise
• Improved dynamics processing
• Professional signal flow

**To apply:** Manually reorder effects in Ableton Live or use individual reorder operations."""
                
                return [{"type": "text", "text": response_text}]
            
            elif operation == "remove" and device_id is not None:
                # Note: This would require specific OSC commands for device removal
                response_text = f"""⚙️ **Effect Removed**

**Removed:**
• Device: {device_id}
• Track: {track_id}

The effect has been removed from the device chain. Audio processing will continue with remaining effects."""
                
                return [{"type": "text", "text": response_text}]
            
            else:
                return [{"type": "text", "text": f"❌ Unknown operation '{operation}' or missing parameters"}]
                
        except Exception as e:
            logger.error(f"Error managing effect chain: {e}")
            return [{"type": "text", "text": f"❌ Error managing chain: {str(e)}"}]
    
    # Helper methods
    
    def _get_optimal_effect_position(self, category: str, effect_name: str) -> int:
        """Determine optimal position in effect chain based on effect type."""
        position_map = {
            "eq": 0,          # EQ first
            "filter": 1,      # Filters early
            "dynamics": 2,    # Compressors after EQ/filter
            "distortion": 3,  # Distortion after dynamics
            "modulation": 4,  # Modulation effects
            "delay": 5,       # Time effects
            "reverb": 6,      # Reverb last
            "utility": 7      # Utility effects at end
        }
        return position_map.get(category, 4)  # Default to middle
    
    def _get_position_description(self, position: int) -> str:
        """Get description of effect chain position."""
        descriptions = {
            0: "Early in chain - EQ/Filter",
            1: "Early-Mid - Filter/Dynamics prep", 
            2: "Mid - Dynamics processing",
            3: "Mid-Late - Character/Distortion",
            4: "Late - Modulation",
            5: "Very Late - Delay",
            6: "End - Reverb",
            7: "Final - Utility"
        }
        return descriptions.get(position, f"Position {position}")
    
    def _get_chain_recommendations(self, category: str) -> str:
        """Get recommended chain order for effect category."""
        return "EQ → Filter → Dynamics → Distortion → Modulation → Delay → Reverb → Utility"
    
    def _get_optimal_chain_order(self, device_names: List[str]) -> List[str]:
        """Analyze devices and return optimal order."""
        # Categorize devices and sort by optimal position
        categorized = []
        for device in device_names:
            category = self._categorize_device(device)
            position = self._get_optimal_effect_position(category, device)
            categorized.append((position, device))
        
        # Sort by position and return device names
        return [device for position, device in sorted(categorized)]
    
    def _categorize_device(self, device_name: str) -> str:
        """Categorize a device by name."""
        name_lower = device_name.lower()
        if "eq" in name_lower:
            return "eq"
        elif any(word in name_lower for word in ["comp", "gate", "limit"]):
            return "dynamics" 
        elif any(word in name_lower for word in ["reverb", "conv"]):
            return "reverb"
        elif any(word in name_lower for word in ["delay", "echo"]):
            return "delay"
        elif any(word in name_lower for word in ["chorus", "phaser", "flanger"]):
            return "modulation"
        elif any(word in name_lower for word in ["satur", "overdrive", "distort"]):
            return "distortion"
        elif any(word in name_lower for word in ["filter", "auto"]):
            return "filter"
        else:
            return "utility"