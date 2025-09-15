"""
Drum Instruments Knowledge Base

Comprehensive database of Ableton Live Suite drum instruments and kits.
"""

DRUMS = {
    "Drum_Racks": {
        "description": "Container for drum samples with built-in effects",
        "category": "drums",
        "genres": ["all"],
        "presets": {
            "techno": ["Industrial Kit", "Analog Kit", "Minimal Kit", "Peak Time Kit"],
            "house": ["Classic 909", "Deep House Kit", "Funky Kit", "Disco Kit"],
            "trance": ["Uplifting Kit", "Progressive Kit", "Psy Kit", "Euro Kit"],
            "drum_and_bass": ["Jungle Kit", "Liquid Kit", "Neurofunk Kit", "Jump Up Kit"],
            "dubstep": ["Heavy Kit", "Wobble Kit", "Hybrid Kit", "Future Kit"]
        },
        "key_parameters": {
            "Kick Volume": {"min": 0, "max": 127, "default": 100},
            "Snare Volume": {"min": 0, "max": 127, "default": 100},
            "Hi-Hat Volume": {"min": 0, "max": 127, "default": 100},
            "Master Volume": {"min": 0, "max": 127, "default": 100},
            "Master Pitch": {"min": -48, "max": 48, "default": 0}
        },
        "device_path": "Live/Drum Rack"
    },

    "Analog_Kick": {
        "description": "Analog-modeled kick drum synthesizer",
        "category": "drums",
        "genres": ["techno", "house", "minimal"],
        "presets": {
            "techno": ["Industrial Kick", "Distorted Kick", "Sub Kick", "Punchy Kick"],
            "house": ["Classic 909", "Deep Kick", "Thump Kick", "Warm Kick"],
            "minimal": ["Clean Kick", "Soft Kick", "Subtle Kick", "Woody Kick"]
        },
        "key_parameters": {
            "Tone": {"min": 0, "max": 127, "default": 64},
            "Decay": {"min": 0, "max": 127, "default": 64},
            "Pitch": {"min": 0, "max": 127, "default": 64},
            "Sub": {"min": 0, "max": 127, "default": 32},
            "Drive": {"min": 0, "max": 127, "default": 0}
        },
        "device_path": "Live/Analog Kick"
    },

    "Analog_Snare": {
        "description": "Analog-modeled snare drum synthesizer",
        "category": "drums",
        "genres": ["techno", "house", "breakbeat"],
        "presets": {
            "techno": ["Industrial Snare", "Clap Snare", "Rim Snare", "Gated Snare"],
            "house": ["Classic Snare", "Deep Snare", "Crisp Snare", "Vintage Snare"],
            "breakbeat": ["Breakbeat Snare", "Funky Snare", "Chopped Snare", "Filtered Snare"]
        },
        "key_parameters": {
            "Tone": {"min": 0, "max": 127, "default": 64},
            "Snap": {"min": 0, "max": 127, "default": 64},
            "Decay": {"min": 0, "max": 127, "default": 64},
            "Noise": {"min": 0, "max": 127, "default": 64}
        },
        "device_path": "Live/Analog Snare"
    },

    "Analog_Hi-Hat": {
        "description": "Analog-modeled hi-hat synthesizer",
        "category": "drums",
        "genres": ["techno", "house", "minimal"],
        "presets": {
            "techno": ["Industrial Hats", "Metallic Hats", "Filtered Hats", "Gated Hats"],
            "house": ["Classic Hats", "Open Hats", "Closed Hats", "Shuffled Hats"],
            "minimal": ["Soft Hats", "Subtle Hats", "Tight Hats", "Clean Hats"]
        },
        "key_parameters": {
            "Tone": {"min": 0, "max": 127, "default": 64},
            "Decay": {"min": 0, "max": 127, "default": 32},
            "Filter": {"min": 0, "max": 127, "default": 64},
            "Noise": {"min": 0, "max": 127, "default": 64}
        },
        "device_path": "Live/Analog Hi-Hat"
    }
}

# Drum patterns by genre (BPM and rhythm characteristics)
DRUM_PATTERNS = {
    "techno": {
        "kick_pattern": "4/4 on beats 1, 2, 3, 4",
        "snare_pattern": "on beats 2, 4 with variations",
        "hihat_pattern": "16th notes with accent variations",
        "bpm_range": (120, 150),
        "characteristics": ["driving", "hypnotic", "industrial", "minimal"]
    },
    "house": {
        "kick_pattern": "4/4 on beats 1, 2, 3, 4",
        "snare_pattern": "on beats 2, 4",
        "hihat_pattern": "8th or 16th notes with swing",
        "bpm_range": (120, 130),
        "characteristics": ["groovy", "warm", "soulful", "danceable"]
    },
    "trance": {
        "kick_pattern": "4/4 on beats 1, 2, 3, 4",
        "snare_pattern": "on beat 2, 4 with rolls",
        "hihat_pattern": "16th notes with filters",
        "bpm_range": (130, 140),
        "characteristics": ["uplifting", "energetic", "melodic", "euphoric"]
    },
    "drum_and_bass": {
        "kick_pattern": "on beat 1, syncopated variations",
        "snare_pattern": "on beat 3 with breakbeat variations",
        "hihat_pattern": "complex breakbeat patterns",
        "bpm_range": (160, 180),
        "characteristics": ["complex", "syncopated", "energetic", "rolling"]
    }
}

def get_drums_by_genre(genre: str):
    """Get drum recommendations for a specific genre."""
    return {name: info for name, info in DRUMS.items() 
            if genre.lower() in info["genres"] or "all" in info["genres"]}

def get_drum_pattern(genre: str):
    """Get drum pattern information for a genre."""
    return DRUM_PATTERNS.get(genre.lower(), {})