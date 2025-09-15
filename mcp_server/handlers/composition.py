"""
Composition Handler - AI-powered music generation and arrangement
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional
import random

logger = logging.getLogger(__name__)

class CompositionHandler:
    """Handles AI composition and music generation."""
    
    def __init__(self, ableton_tools):
        """Initialize with AbletonTools instance."""
        self.ableton_tools = ableton_tools
        
        # Techno/Industrial music knowledge base
        self.techno_chord_progressions = {
            "Am": [
                ["Am", "F", "C", "G"],
                ["Am", "Dm", "G", "C"], 
                ["Am", "F", "G", "Am"],
                ["Am", "C", "F", "G"],
                ["Am", "F", "Dm", "G"]
            ],
            "Dm": [
                ["Dm", "Bb", "F", "C"],
                ["Dm", "Gm", "C", "F"],
                ["Dm", "Bb", "C", "Dm"],
                ["Dm", "F", "Bb", "C"]
            ],
            "Em": [
                ["Em", "C", "G", "D"],
                ["Em", "Am", "D", "G"],
                ["Em", "C", "D", "Em"],
                ["Em", "G", "C", "D"]
            ]
        }
        
        self.industrial_elements = {
            "dark_progressions": [
                ["Am", "F", "G", "Am"],
                ["Dm", "Bb", "F", "C"],
                ["Em", "C", "Am", "B7"]
            ],
            "typical_bpms": [128, 130, 132, 135, 138, 140],
            "song_sections": ["intro", "buildup", "drop", "breakdown", "buildup2", "drop2", "outro"]
        }
    
    async def generate_chord_progression(self, key: str, genre: str, length: int = 8) -> List[Dict[str, Any]]:
        """Generate a chord progression for the specified key and genre."""
        logger.info(f"🎼 Generating {genre} chord progression in {key}, {length} bars")
        
        try:
            # Select appropriate chord progressions based on genre
            if genre == "techno" or genre == "industrial":
                base_progressions = self.techno_chord_progressions.get(key, [])
                if not base_progressions:
                    # Fallback to Am if key not found
                    base_progressions = self.techno_chord_progressions["Am"]
                    key = "Am"
            else:
                # Default to techno for other genres
                base_progressions = self.techno_chord_progressions.get(key, self.techno_chord_progressions["Am"])
            
            # Select a random progression
            base_progression = random.choice(base_progressions)
            
            # Extend progression to desired length
            full_progression = []
            bars_per_chord = max(1, length // len(base_progression))
            
            for chord in base_progression:
                for _ in range(bars_per_chord):
                    full_progression.append(chord)
            
            # Trim to exact length if needed
            full_progression = full_progression[:length]
            
            # Ensure we have the right length
            while len(full_progression) < length:
                full_progression.extend(base_progression[:length - len(full_progression)])
            
            result_text = f"""🎼 **Generated {genre.title()} Chord Progression in {key}**

**Length:** {length} bars
**Progression:** {' | '.join(full_progression)}

**Genre Characteristics:**
• Style: {genre.title()} 
• Key: {key}
• Bars per chord: {bars_per_chord}
• Total bars: {length}

This progression follows typical {genre} harmonic patterns with {'dark, industrial tonality' if genre == 'industrial' else 'driving techno energy'}.
"""
            
            return [{"type": "text", "text": result_text}]
            
        except Exception as e:
            logger.error(f"Error generating chord progression: {e}")
            return [{"type": "text", "text": f"❌ Error generating chord progression: {str(e)}"}]
    
    async def create_techno_song(self, bpm: float = 132, bars: int = 64, style: str = "industrial", key: str = "Am") -> List[Dict[str, Any]]:
        """Create a complete techno song structure in Ableton Live."""
        logger.info(f"🏗️ Creating {style} techno song: {bars} bars at {bpm} BPM in {key}")
        
        try:
            # Set up the basic project
            await self.ableton_tools.set_tempo(bpm)
            
            # Define song structure based on total bars
            if bars <= 32:
                sections = {"intro": 8, "drop": 16, "outro": 8}
            elif bars <= 64:
                sections = {"intro": 8, "buildup": 8, "drop": 24, "breakdown": 8, "drop2": 8, "outro": 8}
            else:
                sections = {"intro": 16, "buildup": 16, "drop": 32, "breakdown": 16, "buildup2": 16, "drop2": 24, "outro": 16}
            
            # Generate chord progression
            chord_length = max(8, bars // 4)  # Progression should repeat throughout song
            progression_result = await self.generate_chord_progression(key, "techno", chord_length)
            
            # Create tracks for the song
            tracks_to_create = [
                ("midi", "Kick"),
                ("midi", "Bass"),
                ("midi", "Lead Synth"),
                ("midi", "Pad"),
                ("audio", "Percussion"),
                ("return", "Reverb"),
                ("return", "Delay")
            ]
            
            created_tracks = []
            for track_type, track_name in tracks_to_create:
                try:
                    result = await self.ableton_tools.create_track(track_type, track_name)
                    if result["status"] == "success":
                        created_tracks.append(track_name)
                        # Small delay to avoid overwhelming Ableton
                        await asyncio.sleep(0.1)
                except Exception as track_error:
                    logger.warning(f"Failed to create track {track_name}: {track_error}")
            
            # Generate style-specific characteristics
            style_info = self._get_style_characteristics(style)
            
            result_text = f"""🎵 **Created {style.title()} Techno Song**

**Project Setup:**
• Tempo: {bpm} BPM
• Length: {bars} bars
• Key: {key}
• Style: {style.title()}

**Song Structure:**"""
            
            current_bar = 1
            for section, section_bars in sections.items():
                result_text += f"\n• {section.title()}: Bars {current_bar}-{current_bar + section_bars - 1} ({section_bars} bars)"
                current_bar += section_bars
            
            result_text += f"""

**Created Tracks:**"""
            for track in created_tracks:
                result_text += f"\n• {track}"
            
            result_text += f"""

**Style Characteristics ({style.title()}):**"""
            for characteristic in style_info:
                result_text += f"\n• {characteristic}"
            
            result_text += f"""

**Chord Progression:** 
{' | '.join(self.techno_chord_progressions.get(key, ["Am", "F", "C", "G"]))}

**Next Steps:**
1. Add drum patterns and percussion elements
2. Program basslines following the chord progression  
3. Create atmospheric pads and textures
4. Add lead synth melodies and arpeggios
5. Apply effects and mixing
"""
            
            return [{"type": "text", "text": result_text}]
            
        except Exception as e:
            logger.error(f"Error creating techno song: {e}")
            return [{"type": "text", "text": f"❌ Error creating techno song: {str(e)}"}]
    
    def _get_style_characteristics(self, style: str) -> List[str]:
        """Get style-specific characteristics for different techno substyles."""
        characteristics = {
            "industrial": [
                "Dark, heavy atmosphere with mechanical elements",
                "Distorted and aggressive sound design",
                "Complex polyrhythms and syncopated patterns",
                "Heavy use of reverb and delay for spatial depth",
                "Emphasis on minor keys and dissonant harmonies"
            ],
            "minimal": [
                "Stripped-down arrangement focusing on groove",
                "Subtle variations and gradual development",
                "Clean, precise sound design",
                "Emphasis on rhythm over melody",
                "Long, evolving structures"
            ],
            "peak_time": [
                "High-energy, driving rhythms",
                "Big room sound with powerful kicks",
                "Uplifting and euphoric progressions",
                "Strong breakdown and buildup sections",
                "Designed for main floor impact"
            ],
            "underground": [
                "Raw, unpolished aesthetic",
                "Hypnotic and repetitive patterns", 
                "Emphasis on groove and funk",
                "Vintage analog sound character",
                "Subtle but effective arrangements"
            ]
        }
        
        return characteristics.get(style, characteristics["industrial"])
    
    async def create_drum_pattern(self, style: str = "industrial", length: int = 4) -> List[Dict[str, Any]]:
        """Create a drum pattern appropriate for the specified style."""
        logger.info(f"🥁 Creating {style} drum pattern, {length} bars")
        
        try:
            patterns = {
                "industrial": {
                    "kick": "X...X...X..X....",  # 4/4 with syncopation
                    "snare": "....X.......X..",
                    "hihat": "..X...X...X...X.",
                    "perc": "X.X.....X.X....."
                },
                "minimal": {
                    "kick": "X.......X.......",  # Clean 4/4
                    "snare": "....X.......X...",
                    "hihat": "..X...X...X...X.",
                    "perc": "................"
                },
                "peak_time": {
                    "kick": "X...X...X...X...",  # Driving 4/4
                    "snare": "....X.......X...",
                    "hihat": "X.X.X.X.X.X.X.X.",
                    "perc": "..X.....X.X....."
                }
            }
            
            pattern = patterns.get(style, patterns["industrial"])
            
            result_text = f"""🥁 **{style.title()} Drum Pattern ({length} bars)**

**Pattern Layout:**
• Kick:   {pattern['kick']}
• Snare:  {pattern['snare']} 
• Hi-Hat: {pattern['hihat']}
• Perc:   {pattern['perc']}

**Legend:** X = Hit, . = Rest
**Pattern repeats every {len(pattern['kick'])} steps**

**Style Notes:**
{self._get_drum_style_notes(style)}
"""
            
            return [{"type": "text", "text": result_text}]
            
        except Exception as e:
            logger.error(f"Error creating drum pattern: {e}")
            return [{"type": "text", "text": f"❌ Error creating drum pattern: {str(e)}"}]
    
    def _get_drum_style_notes(self, style: str) -> str:
        """Get style-specific notes for drum programming."""
        notes = {
            "industrial": "Heavy kick with distortion, aggressive snare, complex hi-hat patterns with polyrhythms",
            "minimal": "Clean, precise hits with subtle swing, emphasis on space and groove",
            "peak_time": "Powerful kick for maximum impact, driving hi-hats, prominent snare on 2 and 4",
            "underground": "Raw, punchy drums with vintage character and groove-focused patterns"
        }
        return notes.get(style, notes["industrial"])