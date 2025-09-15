"""
Filter Effects Knowledge Base

Comprehensive database of filter effects including low-pass, high-pass,
band-pass filters and specialized filter tools.
"""

FILTER_EFFECTS = {
    "Auto_Filter": {
        "description": "Versatile filter with LFO modulation and envelope following",
        "category": "filters",
        "genres": ["electronic", "techno", "house", "dubstep", "trance"],
        "presets": {
            "sweep": ["Classic Sweep", "Resonant Sweep", "Slow Sweep", "Fast Sweep"],
            "envelope": ["Envelope Follow", "Punchy Filter", "Dynamic Filter", "Wah Effect"],
            "lfo": ["Wobble", "Rhythmic", "Slow Wave", "Fast Tremolo"],
            "techno": ["Acid Filter", "Industrial Filter", "Underground", "Peak Time"]
        },
        "key_parameters": {
            "Frequency": {"min": 20, "max": 20000, "default": 1000, "unit": "Hz"},
            "Resonance": {"min": 0, "max": 100, "default": 0, "unit": "%"},
            "LFO_Rate": {"min": 0.01, "max": 20, "default": 1, "unit": "Hz"},
            "LFO_Amount": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Envelope_Amount": {"min": 0, "max": 100, "default": 0, "unit": "%"},
            "Drive": {"min": 0, "max": 100, "default": 0, "unit": "%"}
        },
        "usage_tips": {
            "techno_bass": "High resonance with LFO for acid sounds",
            "build_ups": "Sweep frequency up for tension",
            "rhythmic": "Sync LFO to beat divisions",
            "dynamics": "Use envelope following for dynamic filtering"
        },
        "device_path": "Live/Auto Filter"
    },

    "Operator": {
        "description": "Multi-mode filter section from Operator synthesizer",
        "category": "filters",
        "genres": ["all"],
        "presets": {
            "classic": ["LP 12", "LP 24", "HP 12", "HP 24"],
            "character": ["Notch", "Band Pass", "Formant", "Peak"]
        },
        "key_parameters": {
            "Frequency": {"min": 20, "max": 20000, "default": 1000, "unit": "Hz"},
            "Resonance": {"min": 0, "max": 100, "default": 0, "unit": "%"},
            "Drive": {"min": 0, "max": 100, "default": 0, "unit": "%"}
        },
        "usage_tips": {
            "surgical": "Precise frequency removal or emphasis",
            "character": "Add analog-style filter coloration",
            "resonance": "Self-oscillation for special effects"
        },
        "device_path": "Live/Operator/Filter"
    },

    "Simple_Delay": {
        "description": "Basic delay with high-cut filter",
        "category": "filters",
        "genres": ["all"],
        "presets": {
            "basic": ["Quarter Note", "Eighth Note", "Dotted Eighth", "Sixteenth"]
        },
        "key_parameters": {
            "Delay_Time": {"min": 1, "max": 2000, "default": 250, "unit": "ms"},
            "Feedback": {"min": 0, "max": 100, "default": 20, "unit": "%"},
            "HighCut": {"min": 200, "max": 20000, "default": 10000, "unit": "Hz"}
        },
        "usage_tips": {
            "dub_delays": "High feedback with low-cut filtering",
            "vocal_delays": "Short delays with high-cut for warmth",
            "rhythmic": "Sync to tempo for musical delays"
        },
        "device_path": "Live/Simple Delay"
    }
}