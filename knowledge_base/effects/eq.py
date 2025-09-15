"""
EQ Effects Knowledge Base

Comprehensive database of equalization effects including parametric EQs,
graphic EQs, and specialized EQ tools.
"""

EQ_EFFECTS = {
    "EQ_Eight": {
        "description": "8-band parametric equalizer with spectrum analyzer",
        "category": "eq",
        "genres": ["all"],
        "presets": {
            "vocal": ["Vocal Presence", "Warm Vocal", "Bright Vocal", "Radio Voice"],
            "drums": ["Punchy Drums", "Bright Drums", "Warm Drums", "Modern Drums"],
            "bass": ["Sub Emphasis", "Mid Cut", "Presence Boost", "Vintage Bass"],
            "master": ["Master Polish", "Air Boost", "Warm Master", "Transparent"]
        },
        "key_parameters": {
            "Band_1_Freq": {"min": 20, "max": 20000, "default": 100, "unit": "Hz"},
            "Band_1_Gain": {"min": -15, "max": 15, "default": 0, "unit": "dB"},
            "Band_1_Q": {"min": 0.1, "max": 30, "default": 0.71},
            "Band_8_Freq": {"min": 20, "max": 20000, "default": 10000, "unit": "Hz"},
            "Band_8_Gain": {"min": -15, "max": 15, "default": 0, "unit": "dB"},
            "Band_8_Q": {"min": 0.1, "max": 30, "default": 0.71}
        },
        "usage_tips": {
            "kick": "Boost around 60-80Hz for thump, 2-5kHz for click",
            "snare": "Cut around 200-400Hz for clarity, boost 1-3kHz for snap",
            "bass": "High-pass at 30-40Hz, boost fundamental around 80-120Hz",
            "vocal": "High-pass at 80-100Hz, boost presence around 2-5kHz"
        },
        "device_path": "Live/EQ Eight"
    },

    "EQ_Three": {
        "description": "Simple 3-band equalizer with high and low shelving",
        "category": "eq",
        "genres": ["all"],
        "presets": {
            "general": ["Bright", "Warm", "Scooped", "Neutral"],
            "drums": ["Punchy", "Crisp", "Warm", "Modern"],
            "bass": ["Deep", "Punchy", "Warm", "Present"],
            "vocals": ["Bright", "Warm", "Present", "Smooth"]
        },
        "key_parameters": {
            "GainHi": {"min": -15, "max": 15, "default": 0, "unit": "dB"},
            "GainMid": {"min": -15, "max": 15, "default": 0, "unit": "dB"},
            "GainLo": {"min": -15, "max": 15, "default": 0, "unit": "dB"},
            "FreqHi": {"min": 1000, "max": 20000, "default": 10000, "unit": "Hz"},
            "FreqLo": {"min": 20, "max": 1000, "default": 100, "unit": "Hz"}
        },
        "usage_tips": {
            "quick_fix": "Fast EQ adjustments for live performance",
            "mixing": "Good for broad tonal shaping",
            "mastering": "Gentle overall balance adjustments"
        },
        "device_path": "Live/EQ Three"
    },

    "Bass": {
        "description": "Low-frequency enhancer and sub-bass synthesizer",
        "category": "eq",
        "genres": ["electronic", "hip-hop", "techno", "house"],
        "presets": {
            "enhancement": ["Subtle", "Medium", "Strong", "Extreme"],
            "genre": ["Hip Hop", "Electronic", "Rock", "Pop"]
        },
        "key_parameters": {
            "Frequency": {"min": 20, "max": 300, "default": 60, "unit": "Hz"},
            "Gain": {"min": 0, "max": 24, "default": 6, "unit": "dB"},
            "Dry_Wet": {"min": 0, "max": 100, "default": 50, "unit": "%"}
        },
        "usage_tips": {
            "kick_drums": "Enhance sub frequencies for more impact",
            "bass_lines": "Add weight to thin bass sounds",
            "full_mix": "Add overall low-end presence"
        },
        "device_path": "Live/Bass"
    },

    "Treble": {
        "description": "High-frequency enhancer with presence and air controls",
        "category": "eq",
        "genres": ["all"],
        "presets": {
            "enhancement": ["Subtle", "Medium", "Bright", "Air"],
            "instrument": ["Vocal", "Acoustic", "Electric", "Synth"]
        },
        "key_parameters": {
            "Frequency": {"min": 1000, "max": 20000, "default": 10000, "unit": "Hz"},
            "Gain": {"min": 0, "max": 24, "default": 6, "unit": "dB"},
            "Dry_Wet": {"min": 0, "max": 100, "default": 50, "unit": "%"}
        },
        "usage_tips": {
            "vocals": "Add presence and clarity",
            "cymbals": "Enhance sparkle and shimmer",
            "mix": "Add overall brightness and air"
        },
        "device_path": "Live/Treble"
    }
}