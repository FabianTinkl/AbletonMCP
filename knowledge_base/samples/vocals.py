"""
Vocal Samples Knowledge Base

Comprehensive database of vocal samples including vocal chops, phrases,
ad-libs, and processed vocal textures.
"""

VOCAL_SAMPLES = {
    "Vocal_Chop_House": {
        "description": "Chopped vocal sample perfect for house music",
        "category": "vocal_chop",
        "genres": ["house", "deep_house", "garage", "electronic"],
        "bpm": 128,
        "key": "C",
        "tags": ["vocal", "chop", "house", "soulful", "processed"],
        "variations": ["Vocal_Chop_Pitched", "Vocal_Chop_Reversed", "Vocal_Chop_Gated"],
        "processing_tips": {
            "house": "Vintage compression and EQ",
            "deep_house": "Warm reverb",
            "garage": "Pitch bend and stutter"
        },
        "frequency_range": {"low": 200, "peak": 2000, "high": 8000},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Vocal_Stab": {
        "description": "Short vocal stab for rhythmic emphasis",
        "category": "vocal_stab",
        "genres": ["house", "techno", "electronic", "pop"],
        "bpm": None,
        "key": "G",
        "tags": ["vocal", "stab", "short", "percussive", "accent"],
        "variations": ["Vocal_Stab_High", "Vocal_Stab_Low", "Vocal_Stab_Filtered"],
        "processing_tips": {
            "house": "Layer with percussion",
            "techno": "Heavy processing and effects",
            "pop": "Clean and present"
        },
        "frequency_range": {"low": 300, "peak": 1500, "high": 6000},
        "file_formats": ["wav", "aiff"]
    },

    "Vocal_Phrase_Deep": {
        "description": "Soulful vocal phrase for deep house",
        "category": "vocal_phrase",
        "genres": ["deep_house", "soulful_house", "disco", "funk"],
        "bpm": 120,
        "key": "Am",
        "tags": ["vocal", "phrase", "soulful", "deep", "emotional"],
        "variations": ["Vocal_Phrase_Major", "Vocal_Phrase_Sad", "Vocal_Phrase_Uplifting"],
        "processing_tips": {
            "deep_house": "Warm compression and reverb",
            "disco": "Vintage tape saturation",
            "funk": "Natural dynamics"
        },
        "frequency_range": {"low": 150, "peak": 1000, "high": 5000},
        "length": "8_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Vocal_Texture_Pad": {
        "description": "Processed vocal texture as atmospheric pad",
        "category": "vocal_texture",
        "genres": ["ambient", "electronic", "cinematic", "experimental"],
        "bpm": None,
        "key": "Dm",
        "tags": ["vocal", "texture", "pad", "atmospheric", "processed"],
        "variations": ["Vocal_Texture_Bright", "Vocal_Texture_Dark", "Vocal_Texture_Evolving"],
        "processing_tips": {
            "ambient": "Heavy reverb and delay",
            "electronic": "Granular synthesis",
            "cinematic": "Orchestral layering"
        },
        "frequency_range": {"low": 100, "peak": 800, "high": 4000},
        "file_formats": ["wav", "aiff"]
    },

    "Vocal_Adlib_Hip_Hop": {
        "description": "Hip-hop style vocal ad-lib",
        "category": "vocal_adlib",
        "genres": ["hip_hop", "trap", "electronic", "urban"],
        "bpm": None,
        "key": None,
        "tags": ["vocal", "adlib", "hip_hop", "urban", "processed"],
        "variations": ["Vocal_Adlib_Pitched", "Vocal_Adlib_Reversed", "Vocal_Adlib_Chopped"],
        "processing_tips": {
            "hip_hop": "Autotune and compression",
            "trap": "Heavy processing",
            "electronic": "Vocoder effects"
        },
        "frequency_range": {"low": 200, "peak": 1200, "high": 4000},
        "file_formats": ["wav", "aiff"]
    },

    "Vocal_Harmony": {
        "description": "Layered vocal harmonies",
        "category": "vocal_harmony",
        "genres": ["pop", "r&b", "electronic", "cinematic"],
        "bpm": None,
        "key": "C_maj",
        "tags": ["vocal", "harmony", "layered", "rich", "musical"],
        "variations": ["Vocal_Harmony_Minor", "Vocal_Harmony_Sus", "Vocal_Harmony_7th"],
        "processing_tips": {
            "pop": "Clean compression and EQ",
            "r&b": "Warm analog processing",
            "electronic": "Digital effects and modulation"
        },
        "frequency_range": {"low": 150, "peak": 1500, "high": 6000},
        "file_formats": ["wav", "aiff"]
    }
}