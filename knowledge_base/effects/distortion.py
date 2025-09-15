"""
Distortion Effects Knowledge Base

Comprehensive database of distortion effects including overdrive, distortion,
saturation, and specialized harmonic processors.
"""

DISTORTION_EFFECTS = {
    "Saturator": {
        "description": "Multimode saturation and distortion processor",
        "category": "distortion",
        "genres": ["all"],
        "presets": {
            "tape": ["Tape Saturation", "Warm Tape", "Hot Tape", "Vintage Tape"],
            "tube": ["Tube Warmth", "Tube Drive", "Valve Saturation", "Classic Tube"],
            "digital": ["Digital Clip", "Bit Crush", "Digital Fuzz", "Lo-Fi"],
            "analog": ["Analog Clip", "Soft Clip", "Hard Clip", "Asymmetric"]
        },
        "key_parameters": {
            "Drive": {"min": 0, "max": 36, "default": 0, "unit": "dB"},
            "Base": {"min": -30, "max": 30, "default": 0, "unit": "dB"},
            "Frequency": {"min": 20, "max": 20000, "default": 1000, "unit": "Hz"},
            "Depth": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Output": {"min": -30, "max": 30, "default": 0, "unit": "dB"}
        },
        "usage_tips": {
            "subtle_warmth": "Low drive with tube or tape models",
            "vocal_presence": "Mid-frequency saturation",
            "drum_punch": "Analog clip mode for drums",
            "bass_thickness": "Tube saturation for bass instruments"
        },
        "device_path": "Live/Saturator"
    },

    "Overdrive": {
        "description": "Guitar-style overdrive with tone shaping",
        "category": "distortion",
        "genres": ["rock", "blues", "electronic", "industrial"],
        "presets": {
            "guitar": ["Blues Drive", "Rock Overdrive", "Lead Drive", "Rhythm Drive"],
            "bass": ["Bass Drive", "Tube Bass", "Distorted Bass", "Fuzz Bass"],
            "electronic": ["Synth Drive", "Analog Drive", "Digital Drive", "Warm Drive"],
            "extreme": ["Heavy Drive", "Fuzz Drive", "Blown Drive", "Screaming Drive"]
        },
        "key_parameters": {
            "Drive": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Tone": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Dynamics": {"min": 0, "max": 100, "default": 25, "unit": "%"},
            "Output": {"min": -30, "max": 30, "default": 0, "unit": "dB"},
            "DryWet": {"min": 0, "max": 100, "default": 100, "unit": "%"}
        },
        "usage_tips": {
            "guitar": "Medium drive with dynamics for touch sensitivity",
            "bass": "Low drive to maintain low-end clarity",
            "leads": "High drive for cutting through mix",
            "parallel": "Use dry/wet for parallel processing"
        },
        "device_path": "Live/Overdrive"
    },

    "Amp": {
        "description": "Guitar amplifier simulation with cabinet modeling",
        "category": "distortion",
        "genres": ["rock", "blues", "jazz", "metal", "electronic"],
        "presets": {
            "clean": ["Jazz Clean", "Vintage Clean", "Modern Clean", "Pristine"],
            "crunch": ["Classic Crunch", "British Crunch", "American Crunch", "Vintage Crunch"],
            "lead": ["Lead Channel", "High Gain", "Metal Lead", "Solo Boost"],
            "bass": ["Bass Amp", "Tube Bass", "Modern Bass", "Vintage Bass"]
        },
        "key_parameters": {
            "Gain": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Bass": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Mid": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Treble": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Presence": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Output": {"min": -30, "max": 30, "default": 0, "unit": "dB"}
        },
        "usage_tips": {
            "guitar_recording": "Match amp type to musical style",
            "re_amping": "Process DI signals through amp models",
            "character": "Add tube warmth to electronic sounds",
            "eq_shaping": "Use amp EQ for musical tone shaping"
        },
        "device_path": "Live/Amp"
    },

    "Cabinet": {
        "description": "Guitar cabinet simulation with microphone modeling",
        "category": "distortion",
        "genres": ["rock", "blues", "jazz", "metal", "electronic"],
        "presets": {
            "guitar": ["4x12 Modern", "4x12 Vintage", "2x12 Combo", "1x12 Studio"],
            "bass": ["8x10 Bass", "4x10 Bass", "1x15 Bass", "2x10 Bass"],
            "vintage": ["Vintage 4x12", "Classic 2x12", "Old School", "Retro"],
            "modern": ["Modern 4x12", "High Gain", "Metal Cab", "Studio Cab"]
        },
        "key_parameters": {
            "Model": {"options": ["Various cabinet models"], "default": "4x12 Modern"},
            "Microphone": {"options": ["Dynamic 57", "Dynamic 421", "Condenser 87", "Ribbon 121"], "default": "Dynamic 57"},
            "Dual_Mic": {"options": ["Off", "On"], "default": "Off"},
            "Distance": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Output": {"min": -30, "max": 30, "default": 0, "unit": "dB"}
        },
        "usage_tips": {
            "realism": "Pair with Amp device for complete guitar rig",
            "microphone": "Different mics for different frequency responses",
            "room_sound": "Increase distance for more ambient tone",
            "electronic": "Add cabinet coloration to synthesizers"
        },
        "device_path": "Live/Cabinet"
    },

    "Erosion": {
        "description": "Digital degradation and bit-crushing processor",
        "category": "distortion",
        "genres": ["electronic", "experimental", "industrial", "lo-fi"],
        "presets": {
            "digital": ["Bit Crush", "Sample Rate", "Digital Fuzz", "Glitch"],
            "analog": ["Vinyl", "Tape", "Radio", "Phone"],
            "extreme": ["Heavy Crush", "Aliasing", "Noise", "Broken"],
            "subtle": ["Vintage Digital", "Warm Crush", "Soft Degrade", "Character"]
        },
        "key_parameters": {
            "Frequency": {"min": 100, "max": 18000, "default": 8000, "unit": "Hz"},
            "Width": {"min": 1, "max": 100, "default": 50, "unit": "%"},
            "Amount": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Output": {"min": -30, "max": 30, "default": 0, "unit": "dB"}
        },
        "usage_tips": {
            "lo_fi": "Low sample rates for vintage digital sounds",
            "electronic": "Add digital character to analog sounds",
            "drums": "Bit-crush for industrial drum sounds",
            "vocals": "Subtle degradation for character"
        },
        "device_path": "Live/Erosion"
    }
}