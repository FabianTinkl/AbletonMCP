"""
Synthesizers Knowledge Base

Comprehensive database of Ableton Live Suite synthesizers with presets,
parameters, and genre-specific recommendations.
"""

SYNTHESIZERS = {
    "Wavetable": {
        "description": "Advanced wavetable synthesizer with dual oscillators",
        "category": "synthesizer",
        "genres": ["techno", "trance", "dubstep", "ambient"],
        "presets": {
            "bass": ["Deep Sub", "Wobble Bass", "Acid Bass", "Techno Bass"],
            "lead": ["Bright Lead", "Acid Lead", "Pluck Lead", "Supersaw Lead"],
            "pad": ["Warm Pad", "Evolving Pad", "Dark Pad", "Ethereal Pad"],
            "arp": ["Classic Arp", "Acid Arp", "Melodic Arp", "Rhythmic Arp"]
        },
        "key_parameters": {
            "OSC 1 Position": {"min": 0, "max": 127, "default": 0},
            "OSC 2 Position": {"min": 0, "max": 127, "default": 0},
            "Filter Frequency": {"min": 0, "max": 127, "default": 64},
            "Filter Resonance": {"min": 0, "max": 127, "default": 0},
            "Amp Attack": {"min": 0, "max": 127, "default": 0},
            "Amp Decay": {"min": 0, "max": 127, "default": 64},
            "Amp Sustain": {"min": 0, "max": 127, "default": 100},
            "Amp Release": {"min": 0, "max": 127, "default": 32}
        },
        "device_path": "Live/Wavetable"
    },
    
    "Operator": {
        "description": "FM synthesizer with 4 operators",
        "category": "synthesizer", 
        "genres": ["techno", "minimal", "experimental", "ambient"],
        "presets": {
            "bass": ["Sub Bass", "FM Bass", "Distorted Bass", "Wobble Bass"],
            "lead": ["Bell Lead", "FM Lead", "Brass Lead", "Digital Lead"],
            "pad": ["FM Pad", "Metallic Pad", "Soft Pad", "Evolving Pad"],
            "percussion": ["FM Kick", "FM Snare", "Digital Perc", "Bell Perc"]
        },
        "key_parameters": {
            "Op A Level": {"min": 0, "max": 127, "default": 100},
            "Op B Level": {"min": 0, "max": 127, "default": 0},
            "Op C Level": {"min": 0, "max": 127, "default": 0},
            "Op D Level": {"min": 0, "max": 127, "default": 0},
            "LFO Rate": {"min": 0, "max": 127, "default": 32},
            "LFO Amount": {"min": 0, "max": 127, "default": 0}
        },
        "device_path": "Live/Operator"
    },
    
    "Analog": {
        "description": "Analog-modeled synthesizer with classic sound",
        "category": "synthesizer",
        "genres": ["techno", "house", "trance", "minimal"],
        "presets": {
            "bass": ["Analog Bass", "Sub Bass", "Acid Bass", "Deep Bass"],
            "lead": ["Analog Lead", "Saw Lead", "Square Lead", "Sync Lead"],
            "pad": ["Analog Pad", "String Pad", "Warm Pad", "Vintage Pad"],
            "arp": ["Analog Arp", "Sequence", "Classic Arp", "Rhythmic"]
        },
        "key_parameters": {
            "OSC 1 Wave": {"min": 0, "max": 4, "default": 0},
            "OSC 2 Wave": {"min": 0, "max": 4, "default": 0},
            "Filter Frequency": {"min": 0, "max": 127, "default": 64},
            "Filter Resonance": {"min": 0, "max": 127, "default": 0},
            "Amp Attack": {"min": 0, "max": 127, "default": 0},
            "Amp Release": {"min": 0, "max": 127, "default": 32}
        },
        "device_path": "Live/Analog"
    },

    "Collision": {
        "description": "Mallet instrument synthesizer",
        "category": "synthesizer",
        "genres": ["ambient", "experimental", "minimal", "techno"],
        "presets": {
            "mallet": ["Marimba", "Vibraphone", "Xylophone", "Glockenspiel"],
            "percussion": ["Timpani", "Steel Drum", "Glass", "Metal"],
            "experimental": ["Bowed", "Struck", "Resonant", "Evolving"]
        },
        "key_parameters": {
            "Mallet Volume": {"min": 0, "max": 127, "default": 100},
            "Resonator Volume": {"min": 0, "max": 127, "default": 100},
            "Mallet Stiffness": {"min": 0, "max": 127, "default": 64},
            "Resonator Decay": {"min": 0, "max": 127, "default": 64}
        },
        "device_path": "Live/Collision"
    }
}

# Synthesizer recommendations by mood and energy
SYNTH_RECOMMENDATIONS = {
    "dark": ["Wavetable", "Operator"],
    "bright": ["Analog", "Collision"],
    "aggressive": ["Wavetable", "Operator"],
    "mellow": ["Analog", "Collision"],
    "experimental": ["Operator", "Collision"],
    "classic": ["Analog"]
}

def get_synth_by_mood(mood: str):
    """Get synthesizer recommendations based on mood."""
    return SYNTH_RECOMMENDATIONS.get(mood.lower(), list(SYNTHESIZERS.keys()))

def get_synth_presets(synth_name: str, preset_type: str = None):
    """Get presets for a specific synthesizer."""
    if synth_name not in SYNTHESIZERS:
        return {}
    
    presets = SYNTHESIZERS[synth_name]["presets"]
    if preset_type:
        return presets.get(preset_type, [])
    return presets