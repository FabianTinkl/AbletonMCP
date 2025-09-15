"""
Dynamics Effects Knowledge Base

Comprehensive database of dynamics processing effects including compressors,
limiters, gates, and expanders.
"""

DYNAMICS_EFFECTS = {
    "Compressor": {
        "description": "Standard compressor with ratio, attack, and release controls",
        "category": "dynamics",
        "genres": ["all"],
        "presets": {
            "drums": ["Drum Compressor", "Punchy Drums", "Tight Drums", "Vintage Drums"],
            "bass": ["Bass Compressor", "Tight Bass", "Punchy Bass", "Smooth Bass"],
            "vocals": ["Vocal Compressor", "Smooth Vocals", "Punchy Vocals", "Broadcasting"],
            "master": ["Master Bus", "Glue", "Mix Bus", "Mastering"]
        },
        "key_parameters": {
            "Threshold": {"min": -60, "max": 0, "default": -12, "unit": "dB"},
            "Ratio": {"min": 1, "max": 20, "default": 4},
            "Attack": {"min": 0.1, "max": 100, "default": 3, "unit": "ms"},
            "Release": {"min": 1, "max": 1000, "default": 100, "unit": "ms"},
            "Makeup": {"min": 0, "max": 30, "default": 0, "unit": "dB"}
        },
        "usage_tips": {
            "drums": "Fast attack, medium release for punch",
            "bass": "Medium attack, fast release for consistency",
            "vocals": "Medium attack, medium release for smoothness",
            "master": "Slow attack, medium release for glue"
        },
        "device_path": "Live/Compressor"
    },

    "Multiband_Compressor": {
        "description": "Multi-band compressor with frequency-specific compression",
        "category": "dynamics",
        "genres": ["all"],
        "presets": {
            "mastering": ["Master Bus", "Gentle Master", "Aggressive Master", "Transparent"],
            "drums": ["Drum Bus", "Punchy Kit", "Balanced Kit", "Controlled Kit"],
            "bass": ["Bass Control", "Sub Focus", "Midrange Control", "Full Range"],
            "mix": ["Mix Glue", "Bus Compression", "Parallel", "Vintage"]
        },
        "key_parameters": {
            "Low Threshold": {"min": -60, "max": 0, "default": -24, "unit": "dB"},
            "Mid Threshold": {"min": -60, "max": 0, "default": -18, "unit": "dB"},
            "High Threshold": {"min": -60, "max": 0, "default": -12, "unit": "dB"},
            "Low Ratio": {"min": 1, "max": 20, "default": 3},
            "Mid Ratio": {"min": 1, "max": 20, "default": 4},
            "High Ratio": {"min": 1, "max": 20, "default": 6}
        },
        "usage_tips": {
            "mastering": "Gentle ratios across all bands for cohesion",
            "drums": "Focus on low-end control and punch",
            "vocals": "Control harsh frequencies while maintaining body"
        },
        "device_path": "Live/Multiband Compressor"
    },

    "Limiter": {
        "description": "Transparent limiter for peak control and loudness",
        "category": "dynamics",
        "genres": ["all"],
        "presets": {
            "mastering": ["Transparent Master", "Loud Master", "Vintage Master", "Modern"],
            "drums": ["Drum Limiter", "Punchy Drums", "Controlled Drums"],
            "individual": ["Track Limiter", "Safety Limiter", "Creative Limiter"]
        },
        "key_parameters": {
            "Ceiling": {"min": -20, "max": 0, "default": -0.3, "unit": "dB"},
            "Release": {"min": 0.1, "max": 1000, "default": 50, "unit": "ms"},
            "Gain": {"min": 0, "max": 30, "default": 0, "unit": "dB"},
            "Lookahead": {"min": 0, "max": 10, "default": 5, "unit": "ms"}
        },
        "usage_tips": {
            "mastering": "Set ceiling to -0.3dB, use for loudness maximization",
            "individual_tracks": "Use sparingly, mostly for safety limiting",
            "creative": "Use for aggressive limiting effects"
        },
        "device_path": "Live/Limiter"
    },

    "Gate": {
        "description": "Noise gate for removing unwanted noise and creating rhythmic effects",
        "category": "dynamics",
        "genres": ["techno", "industrial", "metal", "electronic"],
        "presets": {
            "noise_reduction": ["Vocal Gate", "Drum Gate", "Guitar Gate", "Clean Gate"],
            "rhythmic": ["Rhythmic Gate", "Stutter Gate", "Tremolo Gate", "Choppy"],
            "creative": ["Reverse Gate", "Sidechain Gate", "Musical Gate", "Expressive"]
        },
        "key_parameters": {
            "Threshold": {"min": -60, "max": 0, "default": -30, "unit": "dB"},
            "Attack": {"min": 0.1, "max": 100, "default": 1, "unit": "ms"},
            "Hold": {"min": 0.1, "max": 1000, "default": 10, "unit": "ms"},
            "Release": {"min": 1, "max": 10000, "default": 100, "unit": "ms"}
        },
        "usage_tips": {
            "noise_reduction": "Set threshold just above noise floor",
            "rhythmic": "Use sidechain input for musical gating effects",
            "creative": "Experiment with hold and release for unique textures"
        },
        "device_path": "Live/Gate"
    }
}

# Dynamics processing by genre
GENRE_DYNAMICS = {
    "techno": {
        "characteristics": ["aggressive", "punchy", "controlled"],
        "typical_chain": ["Gate", "Compressor", "Limiter"],
        "settings": {
            "compression_ratio": "4:1 to 8:1",
            "attack": "fast to medium",
            "release": "medium",
            "limiting": "aggressive for loudness"
        }
    },
    "house": {
        "characteristics": ["smooth", "groovy", "warm"],
        "typical_chain": ["Compressor", "Multiband_Compressor"],
        "settings": {
            "compression_ratio": "2:1 to 4:1",
            "attack": "medium",
            "release": "medium to slow",
            "limiting": "gentle"
        }
    },
    "ambient": {
        "characteristics": ["transparent", "gentle", "natural"],
        "typical_chain": ["Compressor", "Limiter"],
        "settings": {
            "compression_ratio": "1.5:1 to 3:1",
            "attack": "slow",
            "release": "slow",
            "limiting": "transparent"
        }
    }
}

def get_dynamics_by_genre(genre: str):
    """Get dynamics effects and settings for a specific genre."""
    return GENRE_DYNAMICS.get(genre.lower(), {})

def get_compressor_settings(instrument_type: str, genre: str = None):
    """Get recommended compressor settings for instrument type and genre."""
    base_settings = {
        "drums": {"ratio": 4, "attack": 3, "release": 100},
        "bass": {"ratio": 3, "attack": 10, "release": 50},
        "vocals": {"ratio": 3, "attack": 5, "release": 150},
        "master": {"ratio": 2, "attack": 30, "release": 300}
    }
    
    settings = base_settings.get(instrument_type.lower(), base_settings["master"])
    
    # Genre-specific adjustments
    if genre == "techno":
        settings["ratio"] *= 1.5
        settings["attack"] *= 0.7
    elif genre == "ambient":
        settings["ratio"] *= 0.7
        settings["attack"] *= 2
        
    return settings