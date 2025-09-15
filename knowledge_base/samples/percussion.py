"""
Percussion Samples Knowledge Base

Comprehensive database of percussion samples including shakers, congas,
bongos, and various world percussion instruments.
"""

PERCUSSION_SAMPLES = {
    "Shaker_Loop": {
        "description": "Steady shaker loop for groove",
        "category": "shaker",
        "genres": ["house", "latin", "world", "pop"],
        "bpm": 120,
        "key": None,
        "tags": ["shaker", "groove", "steady", "rhythm", "latin"],
        "variations": ["Shaker_Soft", "Shaker_Hard", "Shaker_Swing", "Shaker_Triplet"],
        "processing_tips": {
            "house": "High-pass filter, subtle reverb",
            "latin": "Natural sound, minimal processing",
            "electronic": "Layer with electronic percussion"
        },
        "frequency_range": {"low": 2000, "peak": 8000, "high": 15000},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Conga_Hit": {
        "description": "Single conga drum hit",
        "category": "conga",
        "genres": ["latin", "world", "house", "afro"],
        "bpm": None,
        "key": "G",
        "tags": ["conga", "hit", "latin", "world", "acoustic"],
        "variations": ["Conga_Low", "Conga_Mid", "Conga_High", "Conga_Slap"],
        "processing_tips": {
            "latin": "Natural reverb, warm EQ",
            "house": "Tight compression",
            "world": "Minimal processing"
        },
        "frequency_range": {"low": 80, "peak": 200, "high": 2000},
        "file_formats": ["wav", "aiff"]
    },

    "Bongo_Pattern": {
        "description": "Traditional bongo rhythm pattern",
        "category": "bongo",
        "genres": ["latin", "world", "jazz", "fusion"],
        "bpm": 100,
        "key": None,
        "tags": ["bongo", "pattern", "latin", "rhythm", "traditional"],
        "variations": ["Bongo_Fast", "Bongo_Slow", "Bongo_Simple", "Bongo_Complex"],
        "processing_tips": {
            "latin": "Room reverb for authenticity",
            "jazz": "Natural dynamics",
            "fusion": "Subtle compression"
        },
        "frequency_range": {"low": 150, "peak": 400, "high": 3000},
        "length": "2_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Tambourine_Shake": {
        "description": "Tambourine shake for accent",
        "category": "tambourine",
        "genres": ["pop", "rock", "folk", "world"],
        "bpm": None,
        "key": None,
        "tags": ["tambourine", "shake", "accent", "bright", "metallic"],
        "variations": ["Tambourine_Short", "Tambourine_Long", "Tambourine_Roll", "Tambourine_Hit"],
        "processing_tips": {
            "pop": "Bright EQ, controlled dynamics",
            "rock": "Compression for punch",
            "folk": "Natural reverb"
        },
        "frequency_range": {"low": 1000, "peak": 5000, "high": 12000},
        "file_formats": ["wav", "aiff"]
    },

    "Industrial_Perc": {
        "description": "Metallic industrial percussion hit",
        "category": "industrial",
        "genres": ["industrial", "techno", "experimental", "hardcore"],
        "bpm": None,
        "key": None,
        "tags": ["industrial", "metallic", "harsh", "aggressive", "noise"],
        "variations": ["Industrial_Soft", "Industrial_Heavy", "Industrial_Reverb", "Industrial_Dry"],
        "processing_tips": {
            "industrial": "Heavy distortion and reverb",
            "techno": "Use sparingly for impact",
            "experimental": "Granular processing"
        },
        "frequency_range": {"low": 200, "peak": 2000, "high": 8000},
        "file_formats": ["wav", "aiff"]
    }
}