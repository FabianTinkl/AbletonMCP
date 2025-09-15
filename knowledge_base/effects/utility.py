"""
Utility Effects Knowledge Base

Comprehensive database of utility effects including gain, EQ, spectrum analyzer,
and other mixing/mastering utilities.
"""

UTILITY_EFFECTS = {
    "Utility": {
        "description": "Essential mixing utility with gain, phase, stereo controls",
        "category": "utility",
        "genres": ["all"],
        "presets": {
            "gain": ["Unity", "+6dB", "+12dB", "-6dB", "-12dB"],
            "phase": ["Phase Invert", "Left Invert", "Right Invert", "Normal"],
            "stereo": ["Mono", "Stereo", "Side", "Mid", "Width"],
            "dc": ["DC Filter On", "DC Filter Off"]
        },
        "key_parameters": {
            "Gain": {"min": -35, "max": 35, "default": 0, "unit": "dB"},
            "Channel_Mode": {"options": ["L+R", "L", "R", "L+R Swap"], "default": "L+R"},
            "Stereo_Width": {"min": 0, "max": 200, "default": 100, "unit": "%"},
            "Bass_Mono": {"min": 0, "max": 120, "default": 0, "unit": "Hz"},
            "DC_Filter": {"options": ["Off", "On"], "default": "Off"},
            "Phase_Invert": {"options": ["Off", "On"], "default": "Off"}
        },
        "usage_tips": {
            "gain_staging": "Precise gain adjustments for proper levels",
            "phase_issues": "Invert phase to fix phase cancellation",
            "stereo_width": "Adjust stereo image width",
            "bass_focus": "Mono low frequencies for focused bass"
        },
        "device_path": "Live/Utility"
    },

    "Spectrum": {
        "description": "Real-time spectrum analyzer with multiple display modes",
        "category": "utility",
        "genres": ["all"],
        "presets": {
            "analysis": ["Standard", "High Resolution", "Musical", "Mastering"],
            "range": ["Full Range", "Low Focus", "Mid Focus", "High Focus"],
            "averaging": ["Fast", "Medium", "Slow", "Hold"],
            "display": ["Linear", "Log", "Mel Scale", "Bark Scale"]
        },
        "key_parameters": {
            "Range": {"options": ["20Hz-20kHz", "20Hz-5kHz", "100Hz-10kHz"], "default": "20Hz-20kHz"},
            "Resolution": {"options": ["Low", "Medium", "High"], "default": "Medium"},
            "Averaging": {"options": ["Off", "Low", "Medium", "High"], "default": "Medium"},
            "Display": {"options": ["Linear", "Logarithmic"], "default": "Logarithmic"}
        },
        "usage_tips": {
            "mixing": "Identify frequency buildup and gaps",
            "mastering": "High resolution for detailed analysis",
            "problem_solving": "Find resonances and problem frequencies",
            "reference": "Compare against reference tracks"
        },
        "device_path": "Live/Spectrum"
    },

    "Tuner": {
        "description": "Chromatic tuner with cent accuracy",
        "category": "utility",
        "genres": ["all"],
        "presets": {
            "standard": ["A=440Hz", "A=432Hz", "A=444Hz"],
            "instrument": ["Guitar", "Bass", "Violin", "Chromatic"]
        },
        "key_parameters": {
            "Reference": {"min": 400, "max": 480, "default": 440, "unit": "Hz"},
            "Cent_Accuracy": {"min": 1, "max": 10, "default": 1, "unit": "cents"},
            "Input_Level": {"min": -60, "max": 0, "default": -12, "unit": "dB"}
        },
        "usage_tips": {
            "recording": "Ensure instruments are properly tuned",
            "live_performance": "Silent tuning during performances",
            "reference": "Check tuning of samples and loops",
            "precision": "Use cent accuracy for exact tuning"
        },
        "device_path": "Live/Tuner"
    },

    "Beat_Repeat": {
        "description": "Real-time beat slicing and repeating effect",
        "category": "utility",
        "genres": ["electronic", "hip-hop", "experimental", "techno"],
        "presets": {
            "repeat": ["1/16 Repeat", "1/8 Repeat", "1/4 Repeat", "1/2 Repeat"],
            "stutter": ["Stutter", "Glitch", "Drum Roll", "Build Up"],
            "gate": ["Gate", "Rhythmic Gate", "Tremolo Gate", "Sync Gate"],
            "creative": ["Random", "Reverse", "Pitch", "Filter"]
        },
        "key_parameters": {
            "Interval": {"options": ["1/32", "1/16", "1/8", "1/4", "1/2", "1", "2"], "default": "1/16"},
            "Repeat": {"min": 1, "max": 32, "default": 8},
            "Grid": {"min": 1, "max": 32, "default": 16},
            "Chance": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Gate": {"min": 0, "max": 100, "default": 100, "unit": "%"}
        },
        "usage_tips": {
            "build_ups": "Use for creating tension before drops",
            "glitch": "Random settings for glitch effects",
            "drums": "Stutter effects on drum tracks",
            "live_performance": "Real-time beat manipulation"
        },
        "device_path": "Live/Beat Repeat"
    },

    "Limiter": {
        "description": "Transparent limiting for level control and loudness",
        "category": "utility",
        "genres": ["all"],
        "presets": {
            "mastering": ["Gentle Master", "Modern Master", "Loud Master", "Transparent"],
            "protection": ["Safety Limit", "Brick Wall", "Soft Limit", "Peak Limit"],
            "creative": ["Pump", "Slam", "Vintage", "Character"],
            "genre": ["Pop Master", "Rock Master", "Electronic", "Classical"]
        },
        "key_parameters": {
            "Gain": {"min": 0, "max": 36, "default": 0, "unit": "dB"},
            "Ceiling": {"min": -20, "max": 0, "default": -0.3, "unit": "dB"},
            "Release": {"min": 0.01, "max": 1000, "default": 10, "unit": "ms"},
            "Lookahead": {"min": 0, "max": 10, "default": 5, "unit": "ms"}
        },
        "usage_tips": {
            "mastering": "Gentle settings for transparent limiting",
            "protection": "Prevent digital clipping",
            "loudness": "Increase perceived loudness",
            "creative": "Extreme settings for pump effects"
        },
        "device_path": "Live/Limiter"
    }
}