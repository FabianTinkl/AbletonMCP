"""
Melodic Samples Knowledge Base

Comprehensive database of melodic samples including leads, arpeggios,
chords, and melodic loops.
"""

MELODIC_SAMPLES = {
    "Acid_Lead_Loop": {
        "description": "Resonant acid lead with filter sweeps",
        "category": "lead",
        "genres": ["acid", "techno", "trance", "electronic"],
        "bpm": 128,
        "key": "Am",
        "tags": ["acid", "lead", "resonant", "filter", "loop"],
        "variations": ["Acid_Lead_Cm", "Acid_Lead_Em", "Acid_Lead_Gm"],
        "processing_tips": {
            "acid": "High resonance, automated filter",
            "techno": "Layer with pads",
            "trance": "Add delay and reverb"
        },
        "frequency_range": {"low": 200, "peak": 1000, "high": 5000},
        "length": "8_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Piano_Chord_Stab": {
        "description": "House piano chord stab",
        "category": "chord",
        "genres": ["house", "deep_house", "garage", "disco"],
        "bpm": None,
        "key": "C_maj",
        "tags": ["piano", "chord", "stab", "house", "classic"],
        "variations": ["Piano_Dm", "Piano_Em", "Piano_Am", "Piano_Gm"],
        "processing_tips": {
            "house": "Vintage compression and EQ",
            "garage": "Pitch bend and chop",
            "deep_house": "Warm saturation"
        },
        "frequency_range": {"low": 100, "peak": 800, "high": 4000},
        "file_formats": ["wav", "aiff"]
    },

    "Supersaw_Lead": {
        "description": "Wide detuned supersaw lead",
        "category": "lead",
        "genres": ["trance", "progressive", "bigroom", "electronic"],
        "bpm": 132,
        "key": "Em",
        "tags": ["supersaw", "wide", "detuned", "lead", "epic"],
        "variations": ["Supersaw_Narrow", "Supersaw_Filtered", "Supersaw_Gated"],
        "processing_tips": {
            "trance": "Heavy reverb and delay",
            "progressive": "Sidechain compression",
            "bigroom": "Add distortion for power"
        },
        "frequency_range": {"low": 150, "peak": 2000, "high": 8000},
        "length": "16_bars",
        "file_formats": ["wav", "aiff", "rex"]
    },

    "Arp_Sequence": {
        "description": "Rhythmic arpeggio sequence",
        "category": "arp",
        "genres": ["trance", "progressive", "synthwave", "electronic"],
        "bpm": 128,
        "key": "Am",
        "tags": ["arp", "sequence", "rhythmic", "melodic", "synth"],
        "variations": ["Arp_Major", "Arp_Fast", "Arp_Slow", "Arp_Gated"],
        "processing_tips": {
            "trance": "Gate for rhythmic interest",
            "synthwave": "Chorus and reverb",
            "progressive": "Automate filter cutoff"
        },
        "frequency_range": {"low": 200, "peak": 1500, "high": 6000},
        "length": "4_bars",
        "file_formats": ["wav", "aiff", "rex"]
    }
}