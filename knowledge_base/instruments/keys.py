"""
Keys Instruments Knowledge Base

Comprehensive database of keyboard instruments for harmonic and melodic elements.
"""

KEYS = {
    "Electric_Piano": {
        "description": "Electric piano emulation with vintage character",
        "category": "keys",
        "genres": ["house", "nu_disco", "jazz", "soul"],
        "presets": {
            "classic": ["Rhodes", "Wurlitzer", "Vintage EP", "Suitcase"],
            "modern": ["Modern EP", "Digital EP", "Clean EP", "Refined"],
            "effects": ["Chorus EP", "Tremolo EP", "Phaser EP", "Driven EP"],
            "ambient": ["Soft EP", "Atmospheric EP", "Dreamy EP", "Floating"]
        },
        "key_parameters": {
            "Tone": {"min": 0, "max": 127, "default": 64},
            "Tremolo Rate": {"min": 0, "max": 127, "default": 32},
            "Tremolo Depth": {"min": 0, "max": 127, "default": 16},
            "Drive": {"min": 0, "max": 127, "default": 0},
            "Release": {"min": 0, "max": 127, "default": 32}
        },
        "frequency_range": (80, 4000),
        "device_path": "Live/Keys/Electric Piano"
    },

    "Acoustic_Piano": {
        "description": "Sampled acoustic piano with realistic dynamics",
        "category": "keys",
        "genres": ["house", "progressive", "ambient", "jazz"],
        "presets": {
            "grand": ["Concert Grand", "Bright Grand", "Warm Grand", "Studio Grand"],
            "upright": ["Upright Piano", "Honky Tonk", "Vintage Upright", "Bar Piano"],
            "prepared": ["Prepared Piano", "Muted Piano", "Felt Piano", "Intimate"]
        },
        "key_parameters": {
            "Dynamics": {"min": 0, "max": 127, "default": 100},
            "Release Samples": {"min": 0, "max": 127, "default": 64},
            "Pedal Noise": {"min": 0, "max": 127, "default": 32},
            "Resonance": {"min": 0, "max": 127, "default": 64}
        },
        "frequency_range": (27, 4200),
        "device_path": "Live/Keys/Acoustic Piano"
    },

    "Organ": {
        "description": "Hammond organ emulation with drawbars",
        "category": "keys", 
        "genres": ["house", "gospel", "jazz", "funk"],
        "presets": {
            "classic": ["B3 Classic", "Gospel Organ", "Jazz Organ", "Hammond"],
            "percussive": ["Perc Organ", "Click Organ", "Funky Organ", "Rhythmic"],
            "ambient": ["Soft Organ", "Pad Organ", "Atmospheric", "Sustained"],
            "driven": ["Driven Organ", "Overdriven", "Rock Organ", "Dirty"]
        },
        "key_parameters": {
            "Drawbar 1": {"min": 0, "max": 127, "default": 100},
            "Drawbar 2": {"min": 0, "max": 127, "default": 80},
            "Drawbar 3": {"min": 0, "max": 127, "default": 60},
            "Percussion": {"min": 0, "max": 127, "default": 0},
            "Vibrato": {"min": 0, "max": 127, "default": 16}
        },
        "frequency_range": (60, 5000),
        "device_path": "Live/Keys/Organ"
    },

    "Clavinet": {
        "description": "Funky clavinet with percussive attack",
        "category": "keys",
        "genres": ["funk", "disco", "house", "nu_disco"],
        "presets": {
            "classic": ["Classic Clav", "Funk Clav", "Stevie Clav", "Vintage"],
            "modern": ["Modern Clav", "Digital Clav", "Clean Clav", "Refined"],
            "effects": ["Wah Clav", "Phaser Clav", "Chorus Clav", "Filtered"],
            "percussive": ["Percussive Clav", "Sharp Clav", "Punchy Clav", "Tight"]
        },
        "key_parameters": {
            "Pickup Mix": {"min": 0, "max": 127, "default": 64},
            "Mute": {"min": 0, "max": 127, "default": 32},
            "EQ Bass": {"min": 0, "max": 127, "default": 64},
            "EQ Treble": {"min": 0, "max": 127, "default": 64}
        },
        "frequency_range": (100, 3000),
        "device_path": "Live/Keys/Clavinet"
    }
}

# Keys usage patterns by genre
KEYS_USAGE = {
    "house": {
        "role": "harmonic foundation, chord progressions, hooks",
        "playing_style": "chord stabs, sustained chords, melodic lines",
        "effects": ["reverb", "delay", "chorus", "EQ"],
        "frequency_placement": "mids, complement vocals and bass",
        "characteristics": ["soulful", "warm", "musical", "groovy"]
    },
    "nu_disco": {
        "role": "main harmonic element, funky rhythms",
        "playing_style": "rhythmic chord patterns, funk rhythms",
        "effects": ["chorus", "phaser", "compression"],
        "frequency_placement": "prominent in mix, wide stereo",
        "characteristics": ["funky", "rhythmic", "vintage", "groovy"]
    },
    "progressive": {
        "role": "emotional elements, breakdowns, builds",
        "playing_style": "sustained chords, melodic phrases",
        "effects": ["reverb", "delay", "modulation"],
        "frequency_placement": "supportive, atmospheric",
        "characteristics": ["emotional", "atmospheric", "supportive", "melodic"]
    },
    "ambient": {
        "role": "textural elements, atmospheric pads",
        "playing_style": "sustained notes, slow evolution",
        "effects": ["heavy reverb", "delay", "modulation"],
        "frequency_placement": "background, wide stereo field",
        "characteristics": ["atmospheric", "textural", "peaceful", "evolving"]
    }
}

# Keys recommendations by musical function
KEYS_FUNCTION_MAPPING = {
    "harmonic": ["Acoustic_Piano", "Electric_Piano", "Organ"],
    "rhythmic": ["Clavinet", "Electric_Piano"],
    "melodic": ["Electric_Piano", "Acoustic_Piano"],
    "atmospheric": ["Organ", "Electric_Piano"],
    "percussive": ["Clavinet"]
}

def get_keys_by_function(function: str):
    """Get keys recommendations based on musical function."""
    return KEYS_FUNCTION_MAPPING.get(function.lower(), list(KEYS.keys()))

def get_keys_by_genre(genre: str):
    """Get keys recommendations for a specific genre."""
    return {name: info for name, info in KEYS.items()
            if genre.lower() in info["genres"]}

def get_keys_usage_info(genre: str):
    """Get information about how keys are used in a specific genre."""
    return KEYS_USAGE.get(genre.lower(), {})