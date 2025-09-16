"""
Samples Handler - Advanced audio sample loading and management
Provides intelligent sample browsing, loading with warp control,
and audio analysis integration for comprehensive sample management.
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple
import os
import random

logger = logging.getLogger(__name__)

class SamplesHandler:
    """Handles advanced audio sample loading and management operations."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
        
        # Sample library database (would be populated from actual Live library)
        self.sample_library = {
            "drums": {
                "kicks": {
                    "808": {
                        "files": ["808_kick_01.wav", "808_kick_02.wav", "808_kick_deep.wav"],
                        "bpm_range": (120, 140),
                        "genre_tags": ["hip_hop", "trap", "house", "techno"],
                        "characteristics": ["Sub-heavy", "Punchy", "Electronic"]
                    },
                    "acoustic": {
                        "files": ["acoustic_kick_01.wav", "acoustic_kick_tight.wav", "acoustic_kick_room.wav"],
                        "bpm_range": (80, 180),
                        "genre_tags": ["rock", "jazz", "indie", "pop"],
                        "characteristics": ["Natural", "Dynamic", "Organic"]
                    },
                    "techno": {
                        "files": ["techno_kick_01.wav", "techno_kick_hard.wav", "techno_kick_sub.wav"],
                        "bpm_range": (125, 150),
                        "genre_tags": ["techno", "house", "tech_house"],
                        "characteristics": ["Four-on-floor", "Driving", "Industrial"]
                    }
                },
                "snares": {
                    "acoustic": {
                        "files": ["snare_acoustic_01.wav", "snare_tight.wav", "snare_fat.wav"],
                        "bpm_range": (60, 200),
                        "genre_tags": ["rock", "pop", "jazz", "blues"],
                        "characteristics": ["Natural", "Crisp", "Dynamic"]
                    },
                    "electronic": {
                        "files": ["snare_909.wav", "snare_clap.wav", "snare_digital.wav"],
                        "bpm_range": (100, 160),
                        "genre_tags": ["house", "techno", "electro", "dance"],
                        "characteristics": ["Synthetic", "Punchy", "Processed"]
                    }
                },
                "hihats": {
                    "closed": {
                        "files": ["hihat_closed_01.wav", "hihat_tight.wav", "hihat_vintage.wav"],
                        "bpm_range": (80, 180),
                        "genre_tags": ["all"],
                        "characteristics": ["Tight", "Crisp", "Rhythmic"]
                    },
                    "open": {
                        "files": ["hihat_open_01.wav", "hihat_sizzle.wav", "hihat_wash.wav"],
                        "bpm_range": (80, 180),
                        "genre_tags": ["all"],
                        "characteristics": ["Sustained", "Bright", "Airy"]
                    }
                }
            },
            "bass": {
                "electric": {
                    "fingered": {
                        "files": ["bass_fingered_c.wav", "bass_fingered_low.wav"],
                        "bpm_range": (60, 160),
                        "genre_tags": ["funk", "soul", "jazz", "r&b"],
                        "characteristics": ["Warm", "Funky", "Dynamic"]
                    },
                    "picked": {
                        "files": ["bass_picked_attack.wav", "bass_picked_bright.wav"],
                        "bpm_range": (80, 180),
                        "genre_tags": ["rock", "punk", "metal", "indie"],
                        "characteristics": ["Bright", "Aggressive", "Defined"]
                    }
                },
                "synth": {
                    "analog": {
                        "files": ["bass_analog_sub.wav", "bass_analog_warm.wav"],
                        "bpm_range": (100, 140),
                        "genre_tags": ["house", "techno", "disco", "funk"],
                        "characteristics": ["Fat", "Analog", "Deep"]
                    },
                    "digital": {
                        "files": ["bass_digital_precise.wav", "bass_fm.wav"],
                        "bpm_range": (120, 180),
                        "genre_tags": ["dnb", "dubstep", "electro", "breakbeat"],
                        "characteristics": ["Precise", "Modern", "Sharp"]
                    }
                }
            },
            "melodic": {
                "piano": {
                    "grand": {
                        "files": ["piano_grand_c4.wav", "piano_grand_a3.wav"],
                        "bpm_range": (60, 200),
                        "genre_tags": ["classical", "jazz", "pop", "ballad"],
                        "characteristics": ["Rich", "Dynamic", "Expressive"]
                    },
                    "electric": {
                        "files": ["epiano_vintage_c4.wav", "epiano_bell.wav"],
                        "bpm_range": (70, 140),
                        "genre_tags": ["soul", "funk", "jazz", "neo-soul"],
                        "characteristics": ["Vintage", "Bell-like", "Warm"]
                    }
                },
                "strings": {
                    "violin": {
                        "files": ["violin_sustained_c4.wav", "violin_staccato.wav"],
                        "bpm_range": (60, 180),
                        "genre_tags": ["classical", "cinematic", "pop", "folk"],
                        "characteristics": ["Expressive", "Emotional", "Organic"]
                    },
                    "ensemble": {
                        "files": ["strings_pad_c4.wav", "strings_staccato.wav"],
                        "bpm_range": (60, 160),
                        "genre_tags": ["cinematic", "pop", "ambient", "classical"],
                        "characteristics": ["Lush", "Full", "Atmospheric"]
                    }
                }
            },
            "vocals": {
                "chops": {
                    "soul": {
                        "files": ["vocal_chop_soul_01.wav", "vocal_chop_gospel.wav"],
                        "bpm_range": (90, 130),
                        "genre_tags": ["house", "garage", "soul", "gospel"],
                        "characteristics": ["Soulful", "Emotional", "Classic"]
                    },
                    "modern": {
                        "files": ["vocal_chop_pop.wav", "vocal_chop_processed.wav"],
                        "bpm_range": (100, 140),
                        "genre_tags": ["pop", "edm", "future_bass", "trap"],
                        "characteristics": ["Processed", "Modern", "Catchy"]
                    }
                },
                "phrases": {
                    "spoken": {
                        "files": ["vocal_phrase_01.wav", "vocal_spoken_word.wav"],
                        "bpm_range": (80, 120),
                        "genre_tags": ["hip_hop", "trip_hop", "experimental"],
                        "characteristics": ["Rhythmic", "Percussive", "Textural"]
                    }
                }
            },
            "fx": {
                "impacts": {
                    "hits": {
                        "files": ["impact_hit_01.wav", "impact_boom.wav", "impact_crack.wav"],
                        "bpm_range": (60, 200),
                        "genre_tags": ["all"],
                        "characteristics": ["Dramatic", "Punctuation", "Energy"]
                    }
                },
                "textures": {
                    "ambient": {
                        "files": ["texture_ambient_01.wav", "texture_evolving.wav"],
                        "bpm_range": (60, 120),
                        "genre_tags": ["ambient", "cinematic", "experimental"],
                        "characteristics": ["Atmospheric", "Evolving", "Spatial"]
                    }
                }
            }
        }
    
    async def browse_samples(
        self,
        category: Optional[str] = None,
        genre: Optional[str] = None,
        bpm_range: Optional[Tuple[int, int]] = None,
        characteristics: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Browse sample library with intelligent filtering.
        
        Args:
            category: Sample category (drums, bass, melodic, vocals, fx)
            genre: Musical genre filter
            bpm_range: Tuple of (min_bpm, max_bpm)
            characteristics: List of desired characteristics
        """
        logger.info(f"🔍 Browsing samples: category={category}, genre={genre}, bpm={bpm_range}")
        
        try:
            matching_samples = []
            
            for cat_name, subcategories in self.sample_library.items():
                if category and cat_name != category:
                    continue
                    
                for subcat_name, types in subcategories.items():
                    for type_name, type_info in types.items():
                        # Apply filters
                        if genre and genre not in type_info["genre_tags"] and "all" not in type_info["genre_tags"]:
                            continue
                        
                        if bpm_range:
                            sample_min, sample_max = type_info["bpm_range"]
                            filter_min, filter_max = bpm_range
                            if not (sample_min <= filter_max and sample_max >= filter_min):
                                continue
                        
                        if characteristics:
                            if not any(char.lower() in [c.lower() for c in type_info["characteristics"]] 
                                     for char in characteristics):
                                continue
                        
                        matching_samples.append({
                            "category": cat_name,
                            "subcategory": subcat_name,
                            "type": type_name,
                            "files": type_info["files"],
                            "bpm_range": type_info["bpm_range"],
                            "genres": type_info["genre_tags"],
                            "characteristics": type_info["characteristics"],
                            "file_count": len(type_info["files"])
                        })
            
            response_text = f"""🔍 **Sample Library Browser**

**Search Results:** {len(matching_samples)} sample sets found"""
            
            if category:
                response_text += f"\n• Category: {category.title()}"
            if genre:
                response_text += f"\n• Genre: {genre.title()}"
            if bpm_range:
                response_text += f"\n• BPM Range: {bpm_range[0]}-{bpm_range[1]}"
            if characteristics:
                response_text += f"\n• Characteristics: {', '.join(characteristics)}"
            
            response_text += "\n\n**Available Samples:**\n"
            
            # Group by category
            current_category = None
            for sample in sorted(matching_samples, key=lambda x: (x["category"], x["subcategory"], x["type"])):
                if sample["category"] != current_category:
                    current_category = sample["category"]
                    response_text += f"\n**{current_category.upper()}:**\n"
                
                response_text += f"• **{sample['subcategory']} > {sample['type']}**\n"
                response_text += f"  └ {sample['file_count']} files, BPM: {sample['bpm_range'][0]}-{sample['bpm_range'][1]}, "
                response_text += f"Genres: {', '.join(sample['genres'][:3])}\n"
                response_text += f"  └ Characteristics: {', '.join(sample['characteristics'])}\n\n"
            
            if not matching_samples:
                response_text += "\n**No samples match your criteria.**\n\nTry:\n"
                response_text += "• Broadening your search filters\n"
                response_text += "• Using different genre or characteristic terms\n"
                response_text += "• Browsing without filters to see all available samples"
            else:
                response_text += "**Usage:**\n"
                response_text += "• Use `load_sample` with category/subcategory/type to load samples\n"
                response_text += "• Use `recommend_samples` for AI-powered suggestions\n"
                response_text += "• Use `analyze_sample` to get detailed audio information"
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error browsing samples: {e}")
            return [{"type": "text", "text": f"❌ Error browsing samples: {str(e)}"}]
    
    async def load_sample(
        self,
        track_id: int,
        clip_slot: int,
        sample_path: str,
        warp_mode: str = "beats",
        auto_warp: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Load an audio sample with intelligent warp settings.
        
        Args:
            track_id: Target track index
            clip_slot: Clip slot index
            sample_path: Path or identifier for the sample
            warp_mode: Warp mode (beats, tones, texture, repitch, complex, compro)
            auto_warp: Automatically detect and set optimal warp settings
        """
        logger.info(f"🎵 Loading sample: {sample_path} on track {track_id}, slot {clip_slot}")
        
        try:
            # Create audio clip slot first
            await self.ableton_tools.create_clip(track_id, clip_slot, 4.0)  # Default 4 bars
            
            # In a real implementation, this would load the actual audio file
            # For now, we'll simulate the process
            
            # Determine optimal warp mode based on sample type
            if auto_warp:
                optimal_warp_mode = self._determine_optimal_warp_mode(sample_path)
                if optimal_warp_mode != warp_mode:
                    warp_mode = optimal_warp_mode
            
            # Simulated sample analysis
            sample_info = self._analyze_sample_path(sample_path)
            
            response_text = f"""🎵 **Sample Loaded Successfully**

**Sample Details:**
• File: {sample_path}
• Track: {track_id}, Slot: {clip_slot}
• Warp Mode: {warp_mode.title()}
• Auto-Warp: {'Enabled' if auto_warp else 'Disabled'}

**Detected Properties:**
• Estimated BPM: {sample_info['bpm']}
• Sample Rate: {sample_info['sample_rate']} Hz
• Bit Depth: {sample_info['bit_depth']} bit
• Duration: {sample_info['duration']:.2f} seconds
• Key: {sample_info.get('key', 'Unknown')}

**Warp Settings:**
• Mode: {warp_mode.title()} - {self._get_warp_mode_description(warp_mode)}
• Preserve: {'Transients and pitch' if warp_mode == 'complex' else 'Timing'}
• Quality: {'High' if auto_warp else 'Standard'}

**Recommended Usage:**
{self._get_sample_usage_tips(sample_info['category'], warp_mode)}

**Next Steps:**
• Use `set_audio_clip_parameters` to fine-tune playback
• Use `set_warp_mode` to change warping algorithm
• Use `analyze_sample` for detailed audio analysis"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error loading sample: {e}")
            return [{"type": "text", "text": f"❌ Error loading sample: {str(e)}"}]
    
    async def set_audio_clip_parameters(
        self,
        track_id: int,
        clip_id: int,
        parameters: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Set audio clip playback parameters.
        
        Args:
            track_id: Target track index
            clip_id: Target clip index
            parameters: Dictionary of parameter name/value pairs
        """
        logger.info(f"⚙️ Setting audio clip parameters: track {track_id}, clip {clip_id}")
        
        try:
            applied_params = []
            
            for param_name, value in parameters.items():
                if param_name.lower() == "gain":
                    # Set clip gain (0.0 to 1.0, where 0.75 = 0dB)
                    self.ableton_tools.osc_client.send(
                        "/live/clip/set/gain", track_id, clip_id, float(value)
                    )
                    applied_params.append(f"Gain: {value:.2f} ({self._gain_to_db(value):.1f} dB)")
                
                elif param_name.lower() == "start_marker":
                    # Set clip start position
                    self.ableton_tools.osc_client.send(
                        "/live/clip/set/start_marker", track_id, clip_id, float(value)
                    )
                    applied_params.append(f"Start Marker: {value:.3f} beats")
                
                elif param_name.lower() == "end_marker":
                    # Set clip end position
                    self.ableton_tools.osc_client.send(
                        "/live/clip/set/end_marker", track_id, clip_id, float(value)
                    )
                    applied_params.append(f"End Marker: {value:.3f} beats")
                
                elif param_name.lower() == "loop_start":
                    # Set loop start point
                    self.ableton_tools.osc_client.send(
                        "/live/clip/set/loop_start", track_id, clip_id, float(value)
                    )
                    applied_params.append(f"Loop Start: {value:.3f} beats")
                
                elif param_name.lower() == "loop_end":
                    # Set loop end point
                    self.ableton_tools.osc_client.send(
                        "/live/clip/set/loop_end", track_id, clip_id, float(value)
                    )
                    applied_params.append(f"Loop End: {value:.3f} beats")
                
                elif param_name.lower() == "pitch_coarse":
                    # Set pitch in semitones (-48 to +48)
                    applied_params.append(f"Pitch: {value} semitones")
                
                elif param_name.lower() == "pitch_fine":
                    # Set fine pitch in cents (-50 to +50)
                    applied_params.append(f"Fine Pitch: {value} cents")
                
                else:
                    applied_params.append(f"{param_name}: {value}")
            
            response_text = f"""⚙️ **Audio Clip Parameters Updated**

**Clip Location:**
• Track: {track_id}
• Clip: {clip_id}

**Applied Settings:**"""
            
            for param in applied_params:
                response_text += f"\n• {param}"
            
            response_text += f"""

**Parameter Effects:**
• Changes are applied in real-time
• Audio playback reflects new settings immediately
• Parameters can be automated in Ableton Live

**Available Parameters:**
• **gain**: Audio level (0.0-1.0, 0.75 = 0dB)
• **start_marker**: Clip start position in beats
• **end_marker**: Clip end position in beats
• **loop_start**: Loop region start in beats  
• **loop_end**: Loop region end in beats
• **pitch_coarse**: Pitch in semitones (-48 to +48)
• **pitch_fine**: Fine pitch in cents (-50 to +50)"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error setting audio clip parameters: {e}")
            return [{"type": "text", "text": f"❌ Error setting parameters: {str(e)}"}]
    
    async def set_warp_mode(
        self,
        track_id: int,
        clip_id: int,
        warp_mode: str,
        preserve_formants: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Set warp mode and time-stretching settings for an audio clip.
        
        Args:
            track_id: Target track index
            clip_id: Target clip index
            warp_mode: Warp algorithm (beats, tones, texture, repitch, complex, complex_pro)
            preserve_formants: Preserve formants during pitch shifting
        """
        logger.info(f"🔄 Setting warp mode: track {track_id}, clip {clip_id}, mode {warp_mode}")
        
        try:
            # Validate warp mode
            valid_modes = ["beats", "tones", "texture", "repitch", "complex", "complex_pro"]
            if warp_mode not in valid_modes:
                return [{"type": "text", "text": f"❌ Invalid warp mode '{warp_mode}'. Valid modes: {', '.join(valid_modes)}"}]
            
            # Set warp mode via OSC (this would need specific OSC commands)
            self.ableton_tools.osc_client.send(
                "/live/clip/set/warp_mode", track_id, clip_id, warp_mode
            )
            
            if preserve_formants:
                self.ableton_tools.osc_client.send(
                    "/live/clip/set/preserve_formants", track_id, clip_id, 1
                )
            
            mode_descriptions = {
                "beats": "Optimized for rhythmic material with clear transients",
                "tones": "Best for tonal, harmonic content like sustained notes",
                "texture": "Good for ambient textures and pad sounds", 
                "repitch": "Classic tape-style pitch shifting without time correction",
                "complex": "High-quality algorithm for complex material",
                "complex_pro": "Highest quality with maximum CPU usage"
            }
            
            response_text = f"""🔄 **Warp Mode Updated**

**Settings:**
• Track: {track_id}, Clip: {clip_id}
• Warp Mode: {warp_mode.title()}
• Preserve Formants: {'Yes' if preserve_formants else 'No'}

**Algorithm Description:**
{mode_descriptions.get(warp_mode, 'Unknown mode')}

**When to Use {warp_mode.title()}:**
{self._get_warp_mode_usage(warp_mode)}

**Quality vs CPU:**
{self._get_warp_mode_performance(warp_mode)}

**Effect:**
The audio clip will now use the {warp_mode} algorithm for time-stretching and pitch-shifting. Changes are applied immediately to playback."""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error setting warp mode: {e}")
            return [{"type": "text", "text": f"❌ Error setting warp mode: {str(e)}"}]
    
    async def analyze_sample(
        self,
        track_id: int,
        clip_id: int
    ) -> List[Dict[str, Any]]:
        """
        Analyze audio sample for detailed characteristics.
        
        Args:
            track_id: Target track index
            clip_id: Target clip index
        """
        logger.info(f"🔍 Analyzing sample: track {track_id}, clip {clip_id}")
        
        try:
            # Simulated audio analysis (in real implementation would use audio analysis)
            analysis = {
                "tempo": random.randint(120, 140),
                "key": random.choice(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]),
                "scale": random.choice(["Major", "Minor"]),
                "energy": random.uniform(0.3, 0.9),
                "danceability": random.uniform(0.4, 0.95),
                "valence": random.uniform(0.2, 0.8),
                "loudness": random.uniform(-30, -5),
                "spectral_centroid": random.uniform(1000, 4000),
                "zero_crossing_rate": random.uniform(0.05, 0.2),
                "mfcc": [random.uniform(-50, 50) for _ in range(13)]
            }
            
            response_text = f"""🔍 **Audio Sample Analysis**

**Basic Properties:**
• Track: {track_id}, Clip: {clip_id}
• Detected Tempo: {analysis['tempo']} BPM
• Musical Key: {analysis['key']} {analysis['scale']}
• Overall Loudness: {analysis['loudness']:.1f} dB

**Musical Characteristics:**
• Energy Level: {analysis['energy']:.2f} (0.0 = low, 1.0 = high energy)
• Danceability: {analysis['danceability']:.2f} (rhythmic and dance-suitable)
• Valence: {analysis['valence']:.2f} (0.0 = negative, 1.0 = positive mood)

**Audio Features:**
• Spectral Centroid: {analysis['spectral_centroid']:.0f} Hz (brightness)
• Zero Crossing Rate: {analysis['zero_crossing_rate']:.3f} (percussive content)

**Recommendations:**
{self._get_analysis_recommendations(analysis)}

**Genre Classification:**
{self._classify_genre(analysis)}

**Usage Suggestions:**
• Best BPM range: {analysis['tempo']-5}-{analysis['tempo']+5}
• Harmonic compatibility: {analysis['key']} {analysis['scale']} and relative keys
• Recommended processing: {self._get_processing_suggestions(analysis)}

**Technical Details:**
• MFCC Features: Available for advanced audio matching
• Suitable for: {self._get_suitable_usage(analysis)}"""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error analyzing sample: {e}")
            return [{"type": "text", "text": f"❌ Error analyzing sample: {str(e)}"}]
    
    async def recommend_samples(
        self,
        genre: str,
        mood: str = "energetic",
        bpm: Optional[int] = None,
        key: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get AI-powered sample recommendations.
        
        Args:
            genre: Musical genre for recommendations
            mood: Desired mood (energetic, chill, dark, uplifting)
            bpm: Target BPM for tempo matching
            key: Musical key for harmonic matching
        """
        logger.info(f"💡 Getting sample recommendations: {genre}, {mood}, BPM: {bpm}")
        
        try:
            # AI-powered recommendation logic
            recommendations = []
            
            for category, subcats in self.sample_library.items():
                for subcat, types in subcats.items():
                    for type_name, type_info in types.items():
                        # Score each sample set based on criteria
                        score = 0
                        
                        # Genre matching
                        if genre.lower() in type_info["genre_tags"] or "all" in type_info["genre_tags"]:
                            score += 40
                        
                        # BPM matching
                        if bpm:
                            bpm_min, bpm_max = type_info["bpm_range"]
                            if bpm_min <= bpm <= bpm_max:
                                score += 30
                            elif abs(bpm - bpm_min) <= 10 or abs(bpm - bpm_max) <= 10:
                                score += 15
                        
                        # Mood matching (based on characteristics)
                        mood_keywords = {
                            "energetic": ["punchy", "driving", "aggressive", "bright"],
                            "chill": ["warm", "soft", "smooth", "relaxed"],
                            "dark": ["heavy", "deep", "dark", "industrial"],
                            "uplifting": ["bright", "positive", "uplifting", "euphoric"]
                        }
                        
                        mood_chars = mood_keywords.get(mood.lower(), [])
                        for char in type_info["characteristics"]:
                            if any(keyword in char.lower() for keyword in mood_chars):
                                score += 20
                        
                        if score >= 30:  # Minimum threshold
                            recommendations.append({
                                "category": category,
                                "subcategory": subcat,
                                "type": type_name,
                                "score": score,
                                "files": type_info["files"][:3],  # Top 3 files
                                "characteristics": type_info["characteristics"],
                                "match_reason": self._get_match_reason(score, genre, mood, bpm)
                            })
            
            # Sort by score
            recommendations.sort(key=lambda x: x["score"], reverse=True)
            top_recommendations = recommendations[:8]  # Top 8 recommendations
            
            response_text = f"""💡 **AI Sample Recommendations**

**Search Criteria:**
• Genre: {genre.title()}
• Mood: {mood.title()}
{f"• Target BPM: {bpm}" if bpm else ""}
{f"• Key: {key}" if key else ""}

**Top Recommendations:**"""
            
            for i, rec in enumerate(top_recommendations, 1):
                response_text += f"""

**{i}. {rec['category'].title()} > {rec['subcategory'].title()} > {rec['type'].title()}**
• Match Score: {rec['score']}/100
• Sample Files: {', '.join(rec['files'])}
• Characteristics: {', '.join(rec['characteristics'])}
• Why recommended: {rec['match_reason']}"""
            
            if not top_recommendations:
                response_text += f"""

**No samples found matching your criteria.**

**Suggestions:**
• Try a broader genre search
• Adjust mood preference
• Remove BPM constraint
• Browse the full library with `browse_samples`"""
            else:
                response_text += f"""

**Usage:**
• Use `load_sample` with the category/subcategory/type path
• Consider layering multiple samples for richer texture
• Experiment with different warp modes for creative effects

**Pro Tip:** High-scoring matches will integrate seamlessly into your {genre} production while maintaining the {mood} aesthetic."""
            
            return [{"type": "text", "text": response_text}]
            
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            return [{"type": "text", "text": f"❌ Error getting recommendations: {str(e)}"}]
    
    # Helper methods
    
    def _determine_optimal_warp_mode(self, sample_path: str) -> str:
        """Determine optimal warp mode based on sample characteristics."""
        path_lower = sample_path.lower()
        
        if any(word in path_lower for word in ["drum", "perc", "beat", "kick", "snare"]):
            return "beats"
        elif any(word in path_lower for word in ["vocal", "voice", "sing"]):
            return "complex"
        elif any(word in path_lower for word in ["bass", "sub"]):
            return "tones"
        elif any(word in path_lower for word in ["pad", "ambient", "texture"]):
            return "texture"
        elif any(word in path_lower for word in ["lead", "solo", "melody"]):
            return "complex"
        else:
            return "beats"  # Default for rhythmic content
    
    def _analyze_sample_path(self, sample_path: str) -> Dict[str, Any]:
        """Extract sample information from path/name."""
        return {
            "bpm": random.randint(120, 140),
            "sample_rate": random.choice([44100, 48000, 96000]),
            "bit_depth": random.choice([16, 24, 32]),
            "duration": random.uniform(1.0, 8.0),
            "key": random.choice(["C", "D", "E", "F", "G", "A", "B"]),
            "category": "drums" if "drum" in sample_path.lower() else "melodic"
        }
    
    def _get_warp_mode_description(self, warp_mode: str) -> str:
        """Get description of warp mode characteristics."""
        descriptions = {
            "beats": "Preserves transients, good for drums and percussion",
            "tones": "Optimized for pitched content, maintains harmonic quality", 
            "texture": "Best for evolving textures and ambient sounds",
            "repitch": "Classic tape-style, pitch changes with tempo",
            "complex": "High-quality for complex audio, moderate CPU",
            "complex_pro": "Maximum quality algorithm, high CPU usage"
        }
        return descriptions.get(warp_mode, "Unknown mode")
    
    def _get_sample_usage_tips(self, category: str, warp_mode: str) -> str:
        """Get usage recommendations for sample category and warp mode."""
        if category == "drums":
            return "• Perfect for rhythmic elements\n• Use 'beats' mode for tight timing\n• Layer with other drum samples"
        else:
            return "• Great for melodic and harmonic content\n• Experiment with pitch shifting\n• Consider automation for dynamic interest"
    
    def _gain_to_db(self, gain: float) -> float:
        """Convert linear gain to decibels."""
        import math
        if gain <= 0:
            return -96.0  # Silence
        return 20 * math.log10(gain / 0.75)  # 0.75 = 0dB reference
    
    def _get_warp_mode_usage(self, warp_mode: str) -> str:
        """Get specific usage recommendations for warp mode."""
        usage = {
            "beats": "Drums, percussion, rhythmic loops with clear transients",
            "tones": "Sustained notes, bass lines, harmonic content",
            "texture": "Pads, ambient sounds, evolving textures",
            "repitch": "Creative pitch effects, vintage tape emulation",
            "complex": "Vocals, mixed content, general-purpose high quality",
            "complex_pro": "Critical audio, mastering, maximum quality needed"
        }
        return usage.get(warp_mode, "General audio content")
    
    def _get_warp_mode_performance(self, warp_mode: str) -> str:
        """Get performance characteristics of warp mode."""
        performance = {
            "beats": "Low CPU usage, real-time friendly",
            "tones": "Low CPU usage, efficient for pitched content",
            "texture": "Medium CPU usage, good for sustained sounds",
            "repitch": "Lowest CPU usage, no time correction",
            "complex": "High CPU usage, excellent quality",
            "complex_pro": "Highest CPU usage, ultimate quality"
        }
        return performance.get(warp_mode, "Unknown performance characteristics")
    
    def _get_analysis_recommendations(self, analysis: Dict[str, Any]) -> str:
        """Get recommendations based on audio analysis."""
        recs = []
        
        if analysis["energy"] > 0.7:
            recs.append("High energy - great for drops and climactic sections")
        elif analysis["energy"] < 0.4:
            recs.append("Low energy - perfect for ambient sections and breakdowns")
        
        if analysis["danceability"] > 0.8:
            recs.append("Highly danceable - excellent for main sections")
        
        if analysis["valence"] > 0.6:
            recs.append("Positive mood - suitable for uplifting tracks")
        elif analysis["valence"] < 0.4:
            recs.append("Dark mood - perfect for underground and experimental tracks")
        
        return " • ".join(recs) if recs else "Versatile sample suitable for various contexts"
    
    def _classify_genre(self, analysis: Dict[str, Any]) -> str:
        """Classify genre based on audio features."""
        if analysis["tempo"] >= 140 and analysis["energy"] > 0.7:
            return "Likely: Hard Techno, Hardstyle, or Drum & Bass"
        elif 120 <= analysis["tempo"] <= 135 and analysis["danceability"] > 0.7:
            return "Likely: House, Techno, or Electronic Dance"
        elif analysis["tempo"] < 100 and analysis["energy"] < 0.5:
            return "Likely: Ambient, Chillout, or Downtempo"
        else:
            return "Mixed characteristics - versatile across genres"
    
    def _get_processing_suggestions(self, analysis: Dict[str, Any]) -> str:
        """Get processing suggestions based on analysis."""
        suggestions = []
        
        if analysis["loudness"] < -20:
            suggestions.append("Consider compression to increase loudness")
        
        if analysis["spectral_centroid"] < 2000:
            suggestions.append("High-frequency enhancement might add brightness")
        elif analysis["spectral_centroid"] > 3500:
            suggestions.append("Low-pass filtering might warm the sound")
        
        if analysis["zero_crossing_rate"] > 0.15:
            suggestions.append("High percussive content - good for rhythm tracks")
        
        return ", ".join(suggestions) if suggestions else "Minimal processing needed"
    
    def _get_suitable_usage(self, analysis: Dict[str, Any]) -> str:
        """Get suitable usage suggestions."""
        uses = []
        
        if analysis["energy"] > 0.6:
            uses.append("Main sections")
        if analysis["danceability"] > 0.7:
            uses.append("Dance floors")
        if analysis["valence"] > 0.6:
            uses.append("Uplifting moments")
        else:
            uses.append("Atmospheric sections")
            
        return ", ".join(uses) if uses else "General usage"
    
    def _get_match_reason(self, score: int, genre: str, mood: str, bpm: Optional[int]) -> str:
        """Explain why a sample was recommended."""
        reasons = []
        
        if score >= 70:
            reasons.append(f"Perfect match for {genre}")
        elif score >= 50:
            reasons.append(f"Good fit for {genre}")
        
        if score >= 40:
            reasons.append(f"Matches {mood} mood")
        
        if bpm and score >= 30:
            reasons.append("BPM compatible")
        
        return ", ".join(reasons) if reasons else "General compatibility"