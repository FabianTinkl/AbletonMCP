"""
Reverb Effects Knowledge Base

Comprehensive database of reverb and spatial effects including algorithmic reverbs,
convolution reverbs, and specialized spatial processors.
"""

REVERB_EFFECTS = {
    "Reverb": {
        "description": "High-quality algorithmic reverb with multiple room types",
        "category": "reverb",
        "genres": ["all"],
        "presets": {
            "rooms": ["Small Room", "Medium Room", "Large Room", "Concert Hall"],
            "plates": ["Vintage Plate", "Bright Plate", "Warm Plate", "Dark Plate"],
            "halls": ["Church", "Cathedral", "Arena", "Stadium"],
            "special": ["Spring", "Ambience", "Shimmer", "Reverse"]
        },
        "key_parameters": {
            "PreDelay": {"min": 0, "max": 250, "default": 0, "unit": "ms"},
            "DecayTime": {"min": 0.1, "max": 60, "default": 2.5, "unit": "s"},
            "DiffusionNetwork": {"min": 0, "max": 100, "default": 68, "unit": "%"},
            "HighFreqDamping": {"min": 200, "max": 20000, "default": 10000, "unit": "Hz"},
            "DryWet": {"min": 0, "max": 100, "default": 25, "unit": "%"}
        },
        "usage_tips": {
            "vocals": "Short decay, medium pre-delay for clarity",
            "drums": "Gated reverb for punch, long for ambience",
            "leads": "Medium decay with high-frequency damping",
            "ambient": "Long decay, high diffusion for soundscapes"
        },
        "device_path": "Live/Reverb"
    },

    "Echo": {
        "description": "Multi-tap delay with filtering and modulation",
        "category": "reverb", 
        "genres": ["electronic", "ambient", "experimental", "dub"],
        "presets": {
            "delay": ["Quarter Note", "Dotted Eighth", "Triplet", "Ping Pong"],
            "ambient": ["Space Echo", "Reverse Echo", "Filtered Echo", "Modulated Echo"],
            "rhythmic": ["Synced Echo", "Polyrhythm", "Offset Echo", "Swing Echo"],
            "special": ["Freeze", "Granular", "Pitch Echo", "Reverse"]
        },
        "key_parameters": {
            "LeftTime": {"min": 1, "max": 2000, "default": 250, "unit": "ms"},
            "RightTime": {"min": 1, "max": 2000, "default": 375, "unit": "ms"},
            "Feedback": {"min": 0, "max": 100, "default": 25, "unit": "%"},
            "LowCut": {"min": 20, "max": 1000, "default": 20, "unit": "Hz"},
            "HighCut": {"min": 1000, "max": 20000, "default": 10000, "unit": "Hz"}
        },
        "usage_tips": {
            "dub_style": "High feedback with filtering",
            "stereo_width": "Different left/right times for width",
            "rhythmic": "Sync to tempo divisions",
            "ambient": "Long feedback times with modulation"
        },
        "device_path": "Live/Echo"
    },

    "Max_for_Live_Convolution_Reverb": {
        "description": "Convolution reverb using impulse responses of real spaces",
        "category": "reverb",
        "genres": ["all"],
        "presets": {
            "halls": ["Symphony Hall", "Opera House", "Concert Hall", "Church"],
            "rooms": ["Studio A", "Live Room", "Vocal Booth", "Drum Room"],
            "chambers": ["Echo Chamber", "Plate Chamber", "Spring Chamber", "Tile Room"],
            "creative": ["Backwards", "Gated", "Shimmer", "Pitched"]
        },
        "key_parameters": {
            "Dry": {"min": -60, "max": 0, "default": 0, "unit": "dB"},
            "Wet": {"min": -60, "max": 12, "default": -12, "unit": "dB"},
            "PreDelay": {"min": 0, "max": 500, "default": 0, "unit": "ms"},
            "DecayTime": {"min": 0.1, "max": 10, "default": 1, "unit": "ratio"}
        },
        "usage_tips": {
            "realism": "Use hall IRs for realistic spaces",
            "character": "Creative IRs for unique textures",
            "subtlety": "Low wet levels for natural enhancement",
            "special_fx": "High wet levels for creative effects"
        },
        "device_path": "Max for Live/Max Audio Effect/Convolution Reverb"
    }
}