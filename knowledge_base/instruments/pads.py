"""
Pad Instruments Knowledge Base

Comprehensive database of pad instruments for atmospheric and background elements.
"""

PADS = {
    "Analog_Pad": {
        "description": "Warm analog-style pad synthesizer",
        "category": "pads",
        "genres": ["trance", "ambient", "house", "techno"],
        "presets": {
            "warm": ["Warm Strings", "Soft Pad", "Vintage Pad", "Analog Strings"],
            "dark": ["Dark Pad", "Mysterious", "Industrial Pad", "Brooding"],
            "bright": ["Bright Pad", "Shimmering", "Ethereal", "Heavenly"],
            "evolving": ["Evolving Pad", "Moving Pad", "Breathing", "Morphing"]
        },
        "key_parameters": {
            "Filter Cutoff": {"min": 0, "max": 127, "default": 80},
            "Filter Resonance": {"min": 0, "max": 127, "default": 16},
            "Attack": {"min": 0, "max": 127, "default": 32},
            "Release": {"min": 0, "max": 127, "default": 80},
            "Chorus Depth": {"min": 0, "max": 127, "default": 32}
        },
        "frequency_range": (200, 2000),
        "device_path": "Live/Pads/Analog Pad"
    },

    "Wavetable_Pad": {
        "description": "Digital wavetable pad with evolving textures",
        "category": "pads",
        "genres": ["trance", "ambient", "techno", "experimental"],
        "presets": {
            "evolving": ["Evolving Waves", "Morphing Pad", "Textural", "Moving"],
            "atmospheric": ["Atmospheric", "Spacey", "Ethereal", "Floating"],
            "digital": ["Digital Pad", "Synthetic", "Modern", "Crystalline"],
            "organic": ["Organic Waves", "Natural", "Flowing", "Breathing"]
        },
        "key_parameters": {
            "Wave Position": {"min": 0, "max": 127, "default": 0},
            "Wave Morph": {"min": 0, "max": 127, "default": 0},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 100},
            "LFO Rate": {"min": 0, "max": 127, "default": 16},
            "LFO Amount": {"min": 0, "max": 127, "default": 32}
        },
        "frequency_range": (150, 3000),
        "device_path": "Live/Pads/Wavetable Pad"
    },

    "String_Pad": {
        "description": "Orchestral string pad emulation",
        "category": "pads",
        "genres": ["trance", "ambient", "cinematic", "house"],
        "presets": {
            "orchestral": ["Full Strings", "Violin Section", "Cello Section", "Orchestra"],
            "synthetic": ["Synth Strings", "Analog Strings", "Vintage Strings", "Retro"],
            "ambient": ["Ambient Strings", "Soft Strings", "Floating", "Dreamy"],
            "epic": ["Epic Strings", "Dramatic", "Cinematic", "Powerful"]
        },
        "key_parameters": {
            "String Mix": {"min": 0, "max": 127, "default": 100},
            "Expression": {"min": 0, "max": 127, "default": 64},
            "Vibrato": {"min": 0, "max": 127, "default": 16},
            "Reverb": {"min": 0, "max": 127, "default": 32}
        },
        "frequency_range": (100, 4000),
        "device_path": "Live/Pads/String Pad"
    },

    "Choir_Pad": {
        "description": "Vocal choir pad for ethereal atmospheres",
        "category": "pads", 
        "genres": ["ambient", "trance", "cinematic", "experimental"],
        "presets": {
            "ethereal": ["Ethereal Choir", "Angelic", "Heavenly", "Divine"],
            "dark": ["Dark Choir", "Mysterious", "Gothic", "Haunting"],
            "modern": ["Modern Choir", "Synthetic Voices", "Digital Choir", "Processed"],
            "classic": ["Classic Choir", "Traditional", "Cathedral", "Sacred"]
        },
        "key_parameters": {
            "Vowel Shape": {"min": 0, "max": 127, "default": 64},
            "Breath": {"min": 0, "max": 127, "default": 32},
            "Vibrato": {"min": 0, "max": 127, "default": 16},
            "Space": {"min": 0, "max": 127, "default": 48}
        },
        "frequency_range": (200, 2500),
        "device_path": "Live/Pads/Choir Pad"
    }
}

# Pad usage patterns by genre
PAD_USAGE = {
    "trance": {
        "role": "harmonic background, builds and breakdowns",
        "playing_style": "sustained chords, evolving textures",
        "effects": ["reverb", "delay", "chorus", "filters"],
        "frequency_placement": "mids, avoid bass frequencies",
        "characteristics": ["uplifting", "evolving", "emotional", "atmospheric"]
    },
    "ambient": {
        "role": "primary harmonic and textural element",
        "playing_style": "long sustained notes, slow evolution",
        "effects": ["heavy reverb", "delay", "modulation"],
        "frequency_placement": "full spectrum with emphasis on mids",
        "characteristics": ["spacious", "evolving", "peaceful", "immersive"]
    },
    "techno": {
        "role": "atmospheric fills, transitions, breakdowns",
        "playing_style": "filtered sweeps, rhythmic chops",
        "effects": ["filters", "distortion", "compression"],
        "frequency_placement": "mids to highs, carved around bass",
        "characteristics": ["industrial", "filtered", "rhythmic", "atmospheric"]
    },
    "house": {
        "role": "harmonic support, emotional elements",
        "playing_style": "chord progressions, sustained harmony",
        "effects": ["reverb", "chorus", "EQ"],
        "frequency_placement": "mids, complementing piano/vocals",
        "characteristics": ["warm", "soulful", "supportive", "musical"]
    }
}

def get_pads_by_mood(mood: str):
    """Get pad recommendations based on mood."""
    mood_mapping = {
        "warm": ["Analog_Pad", "String_Pad"],
        "dark": ["Analog_Pad", "Wavetable_Pad"],
        "bright": ["Wavetable_Pad", "Choir_Pad"],
        "ethereal": ["Choir_Pad", "Wavetable_Pad"],
        "atmospheric": ["Wavetable_Pad", "String_Pad"]
    }
    return mood_mapping.get(mood.lower(), list(PADS.keys()))

def get_pad_usage_info(genre: str):
    """Get information about how pads are used in a specific genre."""
    return PAD_USAGE.get(genre.lower(), {})