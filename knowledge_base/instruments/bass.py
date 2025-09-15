"""
Bass Instruments Knowledge Base

Comprehensive database of bass instruments and sounds for electronic music production.
"""

BASS_INSTRUMENTS = {
    "Analog_Bass": {
        "description": "Classic analog bass synthesizer",
        "category": "bass",
        "genres": ["techno", "house", "minimal", "trance"],
        "presets": {
            "deep": ["Deep Sub", "Warm Sub", "Rounded Bass", "Soft Bass"],
            "aggressive": ["Acid Bass", "Distorted Bass", "Gritty Bass", "Harsh Bass"],
            "melodic": ["Lead Bass", "Melodic Sub", "Plucky Bass", "Bouncy Bass"],
            "minimal": ["Clean Bass", "Simple Bass", "Subtle Bass", "Pure Bass"]
        },
        "key_parameters": {
            "Filter Cutoff": {"min": 0, "max": 127, "default": 64},
            "Filter Resonance": {"min": 0, "max": 127, "default": 16},
            "Envelope Decay": {"min": 0, "max": 127, "default": 48},
            "LFO Rate": {"min": 0, "max": 127, "default": 32},
            "Drive": {"min": 0, "max": 127, "default": 0}
        },
        "frequency_range": (40, 250),
        "device_path": "Live/Bass/Analog Bass"
    },

    "Sub_Bass": {
        "description": "Deep sub-bass frequencies",
        "category": "bass",
        "genres": ["dubstep", "trap", "drum_and_bass", "techno"],
        "presets": {
            "deep": ["Deep Sub", "Sine Sub", "Low Sub", "Foundation"],
            "moving": ["Wobble Sub", "LFO Sub", "Moving Sub", "Modulated Sub"],
            "punchy": ["Punchy Sub", "Attack Sub", "Sharp Sub", "Defined Sub"]
        },
        "key_parameters": {
            "Sine Level": {"min": 0, "max": 127, "default": 100},
            "Sub Octave": {"min": 0, "max": 127, "default": 50},
            "LFO Rate": {"min": 0, "max": 127, "default": 0},
            "LFO Amount": {"min": 0, "max": 127, "default": 0}
        },
        "frequency_range": (20, 80),
        "device_path": "Live/Bass/Sub Bass"
    },

    "Reese_Bass": {
        "description": "Complex detuned bass sound popular in drum & bass",
        "category": "bass",
        "genres": ["drum_and_bass", "dubstep", "breakbeat"],
        "presets": {
            "classic": ["Classic Reese", "Vintage Reese", "Old School", "Original"],
            "modern": ["Modern Reese", "Sharp Reese", "Digital Reese", "Clean Reese"],
            "aggressive": ["Heavy Reese", "Distorted Reese", "Gritty Reese", "Hard Reese"]
        },
        "key_parameters": {
            "Detune Amount": {"min": 0, "max": 127, "default": 32},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 48},
            "Chorus Depth": {"min": 0, "max": 127, "default": 64},
            "Distortion": {"min": 0, "max": 127, "default": 16}
        },
        "frequency_range": (50, 200),
        "device_path": "Live/Bass/Reese Bass"
    },

    "FM_Bass": {
        "description": "FM synthesis bass with complex harmonics",
        "category": "bass", 
        "genres": ["techno", "experimental", "minimal"],
        "presets": {
            "digital": ["Digital Bass", "FM Pluck", "Metallic Bass", "Bell Bass"],
            "warm": ["Warm FM", "Soft FM", "Rounded FM", "Smooth FM"],
            "aggressive": ["Hard FM", "Distorted FM", "Sharp FM", "Piercing FM"]
        },
        "key_parameters": {
            "FM Amount": {"min": 0, "max": 127, "default": 64},
            "Operator Ratio": {"min": 0, "max": 127, "default": 32},
            "Feedback": {"min": 0, "max": 127, "default": 16},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 80}
        },
        "frequency_range": (60, 300),
        "device_path": "Live/Bass/FM Bass"
    }
}

# Bass patterns and playing styles by genre
BASS_PATTERNS = {
    "techno": {
        "pattern_style": "repetitive, driving, often quantized",
        "note_length": "short to medium",
        "frequency_focus": "60-120 Hz with some mids",
        "effects": ["distortion", "compression", "EQ"],
        "characteristics": ["driving", "hypnotic", "powerful", "industrial"]
    },
    "house": {
        "pattern_style": "groovy, often following chord progression",
        "note_length": "medium, with some sustain",
        "frequency_focus": "80-150 Hz",
        "effects": ["compression", "EQ", "subtle chorus"],
        "characteristics": ["warm", "groovy", "musical", "danceable"]
    },
    "drum_and_bass": {
        "pattern_style": "complex, syncopated, often pitched",
        "note_length": "varies greatly",
        "frequency_focus": "50-200 Hz with sub emphasis",
        "effects": ["distortion", "chorus", "reverb"],
        "characteristics": ["complex", "rolling", "powerful", "varied"]
    },
    "dubstep": {
        "pattern_style": "heavily modulated, rhythmic, aggressive",
        "note_length": "short with long modulated sections",
        "frequency_focus": "30-100 Hz sub focus",
        "effects": ["heavy distortion", "LFO", "filters"],
        "characteristics": ["aggressive", "modulated", "powerful", "rhythmic"]
    }
}

def get_bass_by_frequency_range(min_freq: int, max_freq: int):
    """Get bass instruments within specified frequency range."""
    return {name: info for name, info in BASS_INSTRUMENTS.items()
            if (info["frequency_range"][0] >= min_freq and 
                info["frequency_range"][1] <= max_freq)}

def get_bass_by_genre(genre: str):
    """Get bass recommendations for a specific genre."""
    return {name: info for name, info in BASS_INSTRUMENTS.items()
            if genre.lower() in info["genres"]}

def get_bass_pattern_info(genre: str):
    """Get bass pattern and playing style info for a genre."""
    return BASS_PATTERNS.get(genre.lower(), {})