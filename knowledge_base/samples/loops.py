"""
Loops Knowledge Base

Comprehensive database of musical loops including drum loops, bass loops,
melodic loops, and full arrangement loops.
"""

LOOP_SAMPLES = {
    "Techno_Drum_Loop_128": {
        "description": "Four-on-the-floor techno drum loop",
        "category": "drum_loop",
        "genres": ["techno", "minimal", "peak_time", "underground"],
        "bpm": 128,
        "key": None,
        "tags": ["techno", "drums", "four_on_floor", "kick", "hats"],
        "variations": ["Techno_Loop_132", "Techno_Loop_124", "Techno_Loop_Industrial"],
        "processing_tips": {
            "techno": "Layer with additional percussion",
            "minimal": "Use as foundation",
            "peak_time": "Add distortion for energy"
        },
        "frequency_range": {"low": 40, "peak": 2000, "high": 12000},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "House_Groove_120": {
        "description": "Classic house groove with swing",
        "category": "drum_loop",
        "genres": ["house", "deep_house", "disco", "funk"],
        "bpm": 120,
        "key": None,
        "tags": ["house", "groove", "swing", "shuffle", "classic"],
        "variations": ["House_Groove_124", "House_Groove_128", "House_Groove_Deep"],
        "processing_tips": {
            "house": "Vintage compression",
            "deep_house": "Warm analog saturation",
            "disco": "Tape saturation"
        },
        "frequency_range": {"low": 50, "peak": 1500, "high": 10000},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Breakbeat_Loop_140": {
        "description": "Classic Amen break style breakbeat",
        "category": "drum_loop",
        "genres": ["drum_and_bass", "jungle", "breakbeat", "hip_hop"],
        "bpm": 140,
        "key": None,
        "tags": ["breakbeat", "amen", "chopped", "jungle", "classic"],
        "variations": ["Breakbeat_Chopped", "Breakbeat_Filtered", "Breakbeat_Pitched"],
        "processing_tips": {
            "dnb": "Time-stretch and chop",
            "jungle": "Heavy processing and effects",
            "hip_hop": "Slow down and add swing"
        },
        "frequency_range": {"low": 60, "peak": 2500, "high": 8000},
        "length": "2_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Acid_Bass_Loop_128": {
        "description": "Classic acid bass line loop",
        "category": "bass_loop",
        "genres": ["acid", "techno", "house", "electronic"],
        "bpm": 128,
        "key": "Am",
        "tags": ["acid", "bass", "303", "resonant", "filter"],
        "variations": ["Acid_Bass_Cm", "Acid_Bass_Em", "Acid_Bass_Filtered"],
        "processing_tips": {
            "acid": "Automate filter resonance",
            "techno": "Heavy sidechain compression",
            "house": "Subtle filter movement"
        },
        "frequency_range": {"low": 40, "peak": 150, "high": 400},
        "length": "8_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Deep_House_Chord_Loop": {
        "description": "Warm chord progression for deep house",
        "category": "chord_loop",
        "genres": ["deep_house", "soulful_house", "jazz_house", "ambient"],
        "bpm": 120,
        "key": "Am",
        "tags": ["deep", "chords", "warm", "jazz", "soulful"],
        "variations": ["Deep_Chords_Cm", "Deep_Chords_Em", "Deep_Chords_Gm"],
        "processing_tips": {
            "deep_house": "Vintage compression and reverb",
            "jazz_house": "Natural room ambience",
            "ambient": "Heavy reverb and delay"
        },
        "frequency_range": {"low": 100, "peak": 800, "high": 4000},
        "length": "8_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Trance_Arp_Loop_132": {
        "description": "Uplifting trance arpeggio sequence",
        "category": "melodic_loop",
        "genres": ["trance", "progressive", "uplifting", "electronic"],
        "bpm": 132,
        "key": "Em",
        "tags": ["trance", "arpeggio", "uplifting", "melodic", "sequence"],
        "variations": ["Trance_Arp_Am", "Trance_Arp_Gm", "Trance_Arp_Fast"],
        "processing_tips": {
            "trance": "Gate for rhythmic interest",
            "progressive": "Automate filter cutoff",
            "uplifting": "Layer with pads"
        },
        "frequency_range": {"low": 200, "peak": 1500, "high": 6000},
        "length": "16_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Minimal_Perc_Loop": {
        "description": "Subtle percussion loop for minimal techno",
        "category": "percussion_loop",
        "genres": ["minimal", "microhouse", "deep_tech", "underground"],
        "bpm": 128,
        "key": None,
        "tags": ["minimal", "percussion", "subtle", "clicks", "micro"],
        "variations": ["Minimal_Perc_Sparse", "Minimal_Perc_Dense", "Minimal_Perc_Filtered"],
        "processing_tips": {
            "minimal": "Very dry, precise placement",
            "microhouse": "Subtle reverb",
            "deep_tech": "Layer with other percussion"
        },
        "frequency_range": {"low": 200, "peak": 3000, "high": 10000},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Industrial_Texture_Loop": {
        "description": "Dark industrial atmospheric loop",
        "category": "texture_loop",
        "genres": ["industrial", "dark_techno", "experimental", "ambient"],
        "bpm": 120,
        "key": None,
        "tags": ["industrial", "dark", "texture", "atmospheric", "noise"],
        "variations": ["Industrial_Light", "Industrial_Heavy", "Industrial_Rhythmic"],
        "processing_tips": {
            "industrial": "Heavy distortion and reverb",
            "dark_techno": "Use as background element",
            "experimental": "Granular processing"
        },
        "frequency_range": {"low": 100, "peak": 2000, "high": 8000},
        "length": "8_bars",
        "file_formats": ["wav", "aiff"]
    }
}