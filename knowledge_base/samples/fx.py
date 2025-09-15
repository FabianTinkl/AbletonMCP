"""
FX Samples Knowledge Base

Comprehensive database of sound effect samples including risers, impacts,
sweeps, and atmospheric sounds.
"""

FX_SAMPLES = {
    "White_Noise_Riser": {
        "description": "White noise sweep building tension",
        "category": "riser",
        "genres": ["electronic", "techno", "trance", "dubstep"],
        "bpm": None,
        "key": None,
        "tags": ["noise", "riser", "sweep", "tension", "buildup"],
        "variations": ["Noise_Riser_Short", "Noise_Riser_Long", "Noise_Riser_Filtered"],
        "processing_tips": {
            "electronic": "High-pass filter automation",
            "techno": "Layer with reverb",
            "trance": "Sidechain to create pumping effect"
        },
        "frequency_range": {"low": 100, "peak": 5000, "high": 15000},
        "length": "8_beats",
        "file_formats": ["wav", "aiff"]
    },

    "Impact_Hit": {
        "description": "Heavy impact hit for drops and accents",
        "category": "impact",
        "genres": ["cinematic", "electronic", "trap", "dubstep"],
        "bpm": None,
        "key": "C",
        "tags": ["impact", "hit", "drop", "accent", "heavy"],
        "variations": ["Impact_Soft", "Impact_Heavy", "Impact_Metallic", "Impact_Sub"],
        "processing_tips": {
            "cinematic": "Deep reverb for epic feel",
            "electronic": "Layer with sub bass",
            "trap": "Heavy compression"
        },
        "frequency_range": {"low": 30, "peak": 100, "high": 8000},
        "file_formats": ["wav", "aiff"]
    },

    "Reverse_Cymbal": {
        "description": "Reversed cymbal crash for builds",
        "category": "reverse",
        "genres": ["rock", "electronic", "cinematic", "pop"],
        "bpm": None,
        "key": None,
        "tags": ["reverse", "cymbal", "build", "crash", "backwards"],
        "variations": ["Reverse_Short", "Reverse_Long", "Reverse_Filtered", "Reverse_Pitched"],
        "processing_tips": {
            "rock": "Natural room reverb",
            "electronic": "Filter sweeps",
            "cinematic": "Orchestral reverb"
        },
        "frequency_range": {"low": 1000, "peak": 8000, "high": 16000},
        "length": "2_beats",
        "file_formats": ["wav", "aiff"]
    },

    "Industrial_Noise_Sweep": {
        "description": "Harsh industrial noise sweep",
        "category": "sweep",
        "genres": ["industrial", "techno", "hardcore", "experimental"],
        "bpm": None,
        "key": None,
        "tags": ["industrial", "noise", "sweep", "harsh", "aggressive"],
        "variations": ["Industrial_Up", "Industrial_Down", "Industrial_Filtered", "Industrial_Distorted"],
        "processing_tips": {
            "industrial": "Heavy distortion and filtering",
            "techno": "Use sparingly for impact",
            "experimental": "Granular processing"
        },
        "frequency_range": {"low": 200, "peak": 2000, "high": 10000},
        "length": "4_beats",
        "file_formats": ["wav", "aiff"]
    },

    "Vinyl_Crackle": {
        "description": "Vintage vinyl record crackle texture",
        "category": "texture",
        "genres": ["lo_fi", "jazz", "hip_hop", "vintage"],
        "bpm": None,
        "key": None,
        "tags": ["vinyl", "crackle", "texture", "vintage", "lo_fi"],
        "variations": ["Vinyl_Light", "Vinyl_Heavy", "Vinyl_Dust", "Vinyl_Pop"],
        "processing_tips": {
            "lo_fi": "Layer under entire mix",
            "hip_hop": "Use subtly for character",
            "jazz": "Natural vintage feel"
        },
        "frequency_range": {"low": 2000, "peak": 8000, "high": 15000},
        "length": "continuous",
        "file_formats": ["wav", "aiff"]
    },

    "Sub_Drop": {
        "description": "Deep sub bass drop for electronic music",
        "category": "drop",
        "genres": ["dubstep", "trap", "electronic", "bass_music"],
        "bpm": None,
        "key": "C",
        "tags": ["sub", "drop", "bass", "deep", "electronic"],
        "variations": ["Sub_Drop_Short", "Sub_Drop_Long", "Sub_Drop_Filtered", "Sub_Drop_Pitched"],
        "processing_tips": {
            "dubstep": "Heavy sidechain compression",
            "trap": "Layer with kick drum",
            "electronic": "Careful low-end management"
        },
        "frequency_range": {"low": 20, "peak": 60, "high": 200},
        "file_formats": ["wav", "aiff"]
    },

    "Laser_Zap": {
        "description": "Sci-fi laser sound effect",
        "category": "laser",
        "genres": ["electronic", "sci_fi", "experimental", "game"],
        "bpm": None,
        "key": None,
        "tags": ["laser", "zap", "sci_fi", "electronic", "synthetic"],
        "variations": ["Laser_Short", "Laser_Long", "Laser_Sweep", "Laser_Burst"],
        "processing_tips": {
            "electronic": "Use for accent hits",
            "sci_fi": "Layer with reverb",
            "game": "Quick attack, fast decay"
        },
        "frequency_range": {"low": 500, "peak": 3000, "high": 12000},
        "file_formats": ["wav", "aiff"]
    },

    "Ambient_Drone": {
        "description": "Atmospheric drone for background texture",
        "category": "drone",
        "genres": ["ambient", "cinematic", "experimental", "dark"],
        "bpm": None,
        "key": "Dm",
        "tags": ["ambient", "drone", "atmospheric", "texture", "sustained"],
        "variations": ["Drone_Bright", "Drone_Dark", "Drone_Evolving", "Drone_Static"],
        "processing_tips": {
            "ambient": "Heavy reverb and delay",
            "cinematic": "Orchestral processing",
            "experimental": "Granular manipulation"
        },
        "frequency_range": {"low": 50, "peak": 400, "high": 2000},
        "length": "continuous",
        "file_formats": ["wav", "aiff"]
    }
}