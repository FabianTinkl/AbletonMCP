"""
Bass Samples Knowledge Base

Comprehensive database of bass samples including sub bass, acid bass,
synthetic bass lines, and bass one-shots.
"""

BASS_SAMPLES = {
    "Acid_Bass_C": {
        "description": "Classic acid bass line with TB-303 character",
        "category": "bass_line",
        "genres": ["acid", "techno", "house", "electronic"],
        "bpm": 128,
        "key": "C",
        "tags": ["acid", "303", "resonant", "filtered", "classic"],
        "variations": ["Acid_Bass_Cm", "Acid_Bass_Am", "Acid_Bass_Gm", "Acid_Bass_Fm"],
        "processing_tips": {
            "acid": "High resonance filter sweeps",
            "techno": "Sidechain to kick heavily",
            "house": "Subtle filter movement",
            "minimal": "Dry, no effects"
        },
        "frequency_range": {"low": 40, "peak": 120, "high": 300},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Sub_Bass_One_Shot": {
        "description": "Deep sub bass one-shot for low-end foundation",
        "category": "bass_one_shot",
        "genres": ["techno", "dubstep", "trap", "bass_music"],
        "bpm": None,
        "key": "C",
        "tags": ["sub", "deep", "foundation", "sine", "low_end"],
        "variations": ["Sub_Bass_Short", "Sub_Bass_Long", "Sub_Bass_Pitched", "Sub_Bass_Shaped"],
        "processing_tips": {
            "techno": "Tune to kick drum frequency",
            "dubstep": "Layer with mid bass",
            "trap": "Pitch bend for movement",
            "minimal": "Very clean, no distortion"
        },
        "frequency_range": {"low": 25, "peak": 60, "high": 120},
        "file_formats": ["wav", "aiff"]
    },

    "Industrial_Bass": {
        "description": "Distorted bass with industrial character",
        "category": "bass_one_shot", 
        "genres": ["industrial", "techno", "hardcore", "experimental"],
        "bpm": None,
        "key": "C",
        "tags": ["industrial", "distorted", "aggressive", "metallic", "harsh"],
        "variations": ["Industrial_Soft", "Industrial_Heavy", "Industrial_Noise", "Industrial_Filtered"],
        "processing_tips": {
            "industrial": "Heavy saturation and bit crushing",
            "techno": "Use for accent moments",
            "hardcore": "Layer with clean sub",
            "experimental": "Reverse or granular processing"
        },
        "frequency_range": {"low": 60, "peak": 150, "high": 500},
        "file_formats": ["wav", "aiff"]
    },

    "Deep_House_Bass": {
        "description": "Warm, rolling bass line perfect for deep house",
        "category": "bass_line",
        "genres": ["deep_house", "house", "tech_house", "minimal"],
        "bpm": 120,
        "key": "Am",
        "tags": ["deep", "warm", "rolling", "smooth", "analog"],
        "variations": ["Deep_Bass_Cm", "Deep_Bass_Dm", "Deep_Bass_Em", "Deep_Bass_Gm"],
        "processing_tips": {
            "deep_house": "Vintage analog emulation",
            "tech_house": "Tighter compression",
            "minimal": "Very subtle processing",
            "progressive": "Longer phrases"
        },
        "frequency_range": {"low": 50, "peak": 100, "high": 250},
        "length": "8_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "FM_Bass_Stab": {
        "description": "Sharp FM synthesized bass stab",
        "category": "bass_stab",
        "genres": ["techno", "electro", "breakbeat", "experimental"],
        "bpm": None,
        "key": "C",
        "tags": ["fm", "stab", "digital", "sharp", "percussive"],
        "variations": ["FM_Bass_Short", "FM_Bass_Long", "FM_Bass_Detuned", "FM_Bass_Filtered"],
        "processing_tips": {
            "techno": "Use for rhythmic emphasis",
            "electro": "Layer with drums",
            "breakbeat": "Pitch bend for variation",
            "experimental": "Granular manipulation"
        },
        "frequency_range": {"low": 80, "peak": 200, "high": 800},
        "file_formats": ["wav", "aiff"]
    },

    "Wobble_Bass": {
        "description": "LFO modulated dubstep-style wobble bass",
        "category": "bass_line",
        "genres": ["dubstep", "bass_music", "electronic", "experimental"],
        "bpm": 140,
        "key": "E",
        "tags": ["wobble", "lfo", "modulated", "dubstep", "aggressive"],
        "variations": ["Wobble_Slow", "Wobble_Fast", "Wobble_Filtered", "Wobble_Distorted"],
        "processing_tips": {
            "dubstep": "Extreme filtering and distortion",
            "electronic": "Subtle wobble for movement",
            "bass_music": "Layer with sub bass",
            "experimental": "Randomize LFO rates"
        },
        "frequency_range": {"low": 60, "peak": 180, "high": 600},
        "length": "2_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Reese_Bass": {
        "description": "Classic detuned sawtooth Reese bass",
        "category": "bass_one_shot",
        "genres": ["drum_and_bass", "jungle", "breakbeat", "electronic"],
        "bpm": None,
        "key": "A",
        "tags": ["reese", "detuned", "sawtooth", "classic", "wide"],
        "variations": ["Reese_Narrow", "Reese_Wide", "Reese_Filtered", "Reese_Distorted"],
        "processing_tips": {
            "dnb": "Heavy filtering and modulation",
            "jungle": "Pitch bend and chop",
            "breakbeat": "Layer with percussion",
            "electronic": "Subtle detuning"
        },
        "frequency_range": {"low": 40, "peak": 120, "high": 400},
        "file_formats": ["wav", "aiff"]
    },

    "Slap_Bass": {
        "description": "Percussive slap bass with attack",
        "category": "bass_one_shot",
        "genres": ["funk", "house", "disco", "electronic"],
        "bpm": None,
        "key": "E",
        "tags": ["slap", "percussive", "attack", "funk", "acoustic"],
        "variations": ["Slap_Soft", "Slap_Hard", "Slap_Muted", "Slap_Sustained"],
        "processing_tips": {
            "funk": "Minimal processing, natural sound",
            "house": "Compression for consistency",
            "disco": "Vintage tape saturation",
            "electronic": "Layer with synthesized bass"
        },
        "frequency_range": {"low": 60, "peak": 150, "high": 800},
        "file_formats": ["wav", "aiff"]
    }
}