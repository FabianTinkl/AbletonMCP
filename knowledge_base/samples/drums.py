"""
Drum Samples Knowledge Base

Comprehensive database of drum samples including kicks, snares, hats,
and complete drum kits for various genres.
"""

DRUM_SAMPLES = {
    "909_Kick": {
        "description": "Classic Roland TR-909 kick drum sample",
        "category": "kick",
        "genres": ["techno", "house", "electronic", "acid"],
        "bpm": None,  # One-shot
        "key": "C",
        "tags": ["909", "classic", "electronic", "punchy", "sub"],
        "variations": ["909_Kick_Short", "909_Kick_Long", "909_Kick_Sub", "909_Kick_Click"],
        "processing_tips": {
            "techno": "Layer with sub for deeper impact",
            "house": "EQ boost around 60Hz and 2kHz",
            "minimal": "Use dry, no reverb",
            "peak_time": "Add distortion for aggression"
        },
        "frequency_range": {"low": 40, "peak": 65, "high": 200},
        "file_formats": ["wav", "aiff"]
    },

    "808_Kick": {
        "description": "Deep sub-bass kick inspired by TR-808",
        "category": "kick",
        "genres": ["hip-hop", "trap", "electronic", "bass"],
        "bpm": None,
        "key": "C",
        "tags": ["808", "sub", "deep", "bass", "long"],
        "variations": ["808_Kick_Short", "808_Kick_Pitched", "808_Sub_Only", "808_Click"],
        "processing_tips": {
            "hip_hop": "Tune to song key for bass line",
            "electronic": "High-pass at 30Hz to avoid mud",
            "trap": "Layer with snap for attack",
            "bass_music": "Sidechain everything to this"
        },
        "frequency_range": {"low": 25, "peak": 45, "high": 120},
        "file_formats": ["wav", "aiff"]
    },

    "Industrial_Kick": {
        "description": "Distorted, aggressive kick with metallic character",
        "category": "kick",
        "genres": ["industrial", "techno", "hardcore", "experimental"],
        "bpm": None,
        "key": "C",
        "tags": ["industrial", "distorted", "aggressive", "metallic", "harsh"],
        "variations": ["Industrial_Soft", "Industrial_Hard", "Industrial_Noise", "Industrial_Metal"],
        "processing_tips": {
            "industrial": "Add more distortion and compression",
            "techno": "Use sparingly for impact moments",
            "hardcore": "Layer multiple variations",
            "experimental": "Reverse or pitch shift"
        },
        "frequency_range": {"low": 50, "peak": 85, "high": 400},
        "file_formats": ["wav", "aiff"]
    },

    "House_Kick": {
        "description": "Four-on-the-floor house kick with warmth",
        "category": "kick",
        "genres": ["house", "deep_house", "tech_house", "disco"],
        "bpm": None,
        "key": "C",
        "tags": ["house", "warm", "four_on_floor", "punchy", "classic"],
        "variations": ["House_Deep", "House_Punchy", "House_Vintage", "House_Modern"],
        "processing_tips": {
            "deep_house": "Warm saturation and compression",
            "tech_house": "Tighter, more controlled",
            "disco": "Vintage tape saturation",
            "progressive": "Longer tail with reverb"
        },
        "frequency_range": {"low": 50, "peak": 75, "high": 180},
        "file_formats": ["wav", "aiff"]
    },

    "909_Snare": {
        "description": "Classic TR-909 snare with characteristic snap",
        "category": "snare",
        "genres": ["techno", "house", "electronic", "breakbeat"],
        "bpm": None,
        "key": "D",
        "tags": ["909", "snare", "electronic", "snap", "classic"],
        "variations": ["909_Snare_Short", "909_Snare_Long", "909_Rim", "909_Clap"],
        "processing_tips": {
            "techno": "Add reverb for space",
            "house": "Layer with clap",
            "breakbeat": "Pitch down for variation",
            "minimal": "Use dry and tight"
        },
        "frequency_range": {"low": 200, "peak": 2500, "high": 8000},
        "file_formats": ["wav", "aiff"]
    },

    "Industrial_Snare": {
        "description": "Harsh, distorted snare with metallic resonance",
        "category": "snare",
        "genres": ["industrial", "techno", "hardcore", "metal"],
        "bpm": None,
        "key": "D",
        "tags": ["industrial", "harsh", "distorted", "metallic", "aggressive"],
        "variations": ["Industrial_Short", "Industrial_Reverb", "Industrial_Noise", "Industrial_Metal"],
        "processing_tips": {
            "industrial": "Heavy compression and gate",
            "techno": "Use for accent hits",
            "hardcore": "Layer with noise",
            "metal": "Blend with acoustic snare"
        },
        "frequency_range": {"low": 150, "peak": 3000, "high": 10000},
        "file_formats": ["wav", "aiff"]
    },

    "909_Hat_Closed": {
        "description": "Classic TR-909 closed hi-hat",
        "category": "hihat",
        "genres": ["techno", "house", "electronic", "acid"],
        "bpm": None,
        "key": "F#",
        "tags": ["909", "hihat", "closed", "electronic", "crisp"],
        "variations": ["909_Hat_Tight", "909_Hat_Loose", "909_Hat_Filtered", "909_Hat_Accent"],
        "processing_tips": {
            "techno": "High-pass filter for clarity",
            "house": "Swing timing for groove",
            "minimal": "Very dry and precise",
            "acid": "Filter sweeps for movement"
        },
        "frequency_range": {"low": 5000, "peak": 8000, "high": 15000},
        "file_formats": ["wav", "aiff"]
    },

    "909_Hat_Open": {
        "description": "Classic TR-909 open hi-hat with decay",
        "category": "hihat",
        "genres": ["techno", "house", "electronic", "breakbeat"],
        "bpm": None,
        "key": "F#",
        "tags": ["909", "hihat", "open", "electronic", "decay"],
        "variations": ["909_Open_Short", "909_Open_Long", "909_Open_Filtered", "909_Open_Reverse"],
        "processing_tips": {
            "techno": "Use sparingly for emphasis",
            "house": "Off-beat placement for groove",
            "breakbeat": "Choke with closed hat",
            "trance": "Reverb for atmosphere"
        },
        "frequency_range": {"low": 3000, "peak": 7000, "high": 12000},
        "file_formats": ["wav", "aiff"]
    }
}