"""
Delay Effects Knowledge Base

Comprehensive database of delay effects including simple delays, multi-tap delays,
and specialized delay processors.
"""

DELAY_EFFECTS = {
    "Simple_Delay": {
        "description": "Basic stereo delay with tempo sync and filtering",
        "category": "delay",
        "genres": ["all"],
        "presets": {
            "musical": ["Quarter Note", "Eighth Note", "Dotted Eighth", "Sixteenth Note"],
            "creative": ["Ping Pong", "Wide Stereo", "Mono Echo", "Slap Back"],
            "genre": ["Dub Delay", "Rock Delay", "Electronic Delay", "Ambient Delay"]
        },
        "key_parameters": {
            "DelayTime": {"min": 1, "max": 2000, "default": 250, "unit": "ms"},
            "Sync": {"options": ["Off", "On"], "default": "On"},
            "Offset": {"min": -50, "max": 50, "default": 0, "unit": "%"},
            "Feedback": {"min": 0, "max": 100, "default": 20, "unit": "%"},
            "DryWet": {"min": 0, "max": 100, "default": 25, "unit": "%"}
        },
        "usage_tips": {
            "vocal_doubling": "Short delay (20-40ms) for thickness",
            "rhythmic_delay": "Sync to tempo divisions",
            "dub_style": "High feedback with filtering",
            "stereo_width": "Use offset for stereo movement"
        },
        "device_path": "Live/Simple Delay"
    },

    "Ping_Pong_Delay": {
        "description": "Stereo ping-pong delay with independent left/right controls",
        "category": "delay",
        "genres": ["electronic", "ambient", "pop", "rock"],
        "presets": {
            "sync": ["1/4 Ping Pong", "1/8 Ping Pong", "1/16 Ping Pong", "Dotted 1/8"],
            "creative": ["Wide Bounce", "Narrow Bounce", "Asymmetric", "Triplet Bounce"],
            "feedback": ["Subtle Echo", "Building Echo", "Infinite Echo", "Controlled Chaos"]
        },
        "key_parameters": {
            "LeftTime": {"min": 1, "max": 2000, "default": 250, "unit": "ms"},
            "RightTime": {"min": 1, "max": 2000, "default": 375, "unit": "ms"},
            "Feedback": {"min": 0, "max": 100, "default": 30, "unit": "%"},
            "Frozen": {"options": ["Off", "On"], "default": "Off"},
            "DryWet": {"min": 0, "max": 100, "default": 30, "unit": "%"}
        },
        "usage_tips": {
            "stereo_interest": "Different L/R times for movement",
            "build_tension": "Increase feedback for builds",
            "freeze": "Hold delays for special effects",
            "rhythmic": "Sync both sides to tempo"
        },
        "device_path": "Live/Ping Pong Delay"
    },

    "Grain_Delay": {
        "description": "Granular delay with pitch shifting and time stretching",
        "category": "delay",
        "genres": ["experimental", "ambient", "electronic", "post-rock"],
        "presets": {
            "granular": ["Granular Echo", "Pitch Delay", "Time Stretch", "Texture Delay"],
            "creative": ["Shimmer", "Octave Down", "Octave Up", "Harmonizer"],
            "ambient": ["Cloud Delay", "Evolving Echo", "Ethereal", "Soundscape"],
            "rhythmic": ["Rhythmic Grains", "Polyrhythm", "Swing Grains", "Offset Grains"]
        },
        "key_parameters": {
            "DelayTime": {"min": 1, "max": 2000, "default": 500, "unit": "ms"},
            "Pitch": {"min": -24, "max": 24, "default": 0, "unit": "semitones"},
            "Spray": {"min": 0, "max": 100, "default": 0, "unit": "%"},
            "Frequency": {"min": 5, "max": 100, "default": 20, "unit": "Hz"},
            "Feedback": {"min": 0, "max": 100, "default": 25, "unit": "%"}
        },
        "usage_tips": {
            "shimmer": "High pitch (+12 semitones) with feedback",
            "texture": "High spray value for granular clouds",
            "harmonies": "Fixed pitch intervals for harmonic delays",
            "movement": "Modulate spray for evolving textures"
        },
        "device_path": "Live/Grain Delay"
    },

    "Filter_Delay": {
        "description": "Delay with built-in filter and LFO modulation",
        "category": "delay",
        "genres": ["electronic", "techno", "dub", "ambient"],
        "presets": {
            "filtered": ["LP Delay", "HP Delay", "BP Delay", "Notch Delay"],
            "modulated": ["Wobble Delay", "Sweep Delay", "Tremolo Delay", "Filter LFO"],
            "dub": ["Dub Echo", "Filter Dub", "Deep Dub", "Space Dub"],
            "techno": ["Acid Delay", "Industrial Echo", "Underground", "Peak Delay"]
        },
        "key_parameters": {
            "DelayTime": {"min": 1, "max": 2000, "default": 375, "unit": "ms"},
            "Feedback": {"min": 0, "max": 100, "default": 35, "unit": "%"},
            "FilterFreq": {"min": 20, "max": 20000, "default": 2000, "unit": "Hz"},
            "FilterRes": {"min": 0, "max": 100, "default": 10, "unit": "%"},
            "LFORate": {"min": 0.01, "max": 20, "default": 1, "unit": "Hz"}
        },
        "usage_tips": {
            "dub_delays": "Low-pass filtering with high feedback",
            "movement": "LFO modulation of filter frequency",
            "buildup": "Sweep filter while adjusting feedback",
            "character": "Resonance for analog-style coloration"
        },
        "device_path": "Live/Filter Delay"
    }
}