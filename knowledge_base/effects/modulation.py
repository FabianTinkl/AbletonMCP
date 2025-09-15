"""
Modulation Effects Knowledge Base

Comprehensive database of modulation effects including chorus, flanger, phaser,
tremolo, and other modulation processors.
"""

MODULATION_EFFECTS = {
    "Chorus": {
        "description": "Multi-voice chorus with delay and pitch modulation",
        "category": "modulation",
        "genres": ["pop", "rock", "jazz", "ambient", "synthwave"],
        "presets": {
            "classic": ["Vintage Chorus", "80s Chorus", "Jazz Chorus", "Clean Chorus"],
            "modern": ["Wide Chorus", "Shimmer Chorus", "Deep Chorus", "Subtle Chorus"],
            "creative": ["Detune Chorus", "Vibrato Chorus", "Ensemble", "Doubling"],
            "instrument": ["Guitar Chorus", "Vocal Chorus", "Synth Chorus", "Bass Chorus"]
        },
        "key_parameters": {
            "Rate": {"min": 0.1, "max": 20, "default": 0.5, "unit": "Hz"},
            "Amount": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "HiCut": {"min": 1000, "max": 20000, "default": 10000, "unit": "Hz"},
            "DryWet": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Delay1": {"min": 1, "max": 50, "default": 7, "unit": "ms"},
            "Delay2": {"min": 1, "max": 50, "default": 21, "unit": "ms"}
        },
        "usage_tips": {
            "vocals": "Subtle settings for natural doubling",
            "guitars": "Classic 80s sound with medium settings",
            "synths": "Wide stereo image with higher amounts",
            "bass": "Very subtle to avoid muddiness"
        },
        "device_path": "Live/Chorus"
    },

    "Flanger": {
        "description": "Classic flanger with feedback and stereo options",
        "category": "modulation",
        "genres": ["rock", "electronic", "experimental", "psychedelic"],
        "presets": {
            "classic": ["Vintage Flange", "Jet Flange", "Slow Flange", "Fast Flange"],
            "stereo": ["Stereo Flange", "Wide Flange", "Ping Pong", "Counter Rotate"],
            "feedback": ["Metallic", "Resonant", "Harsh", "Gentle"],
            "creative": ["Reverse Flange", "Envelope", "Random", "Stepped"]
        },
        "key_parameters": {
            "Rate": {"min": 0.01, "max": 10, "default": 0.5, "unit": "Hz"},
            "Amount": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Feedback": {"min": -100, "max": 100, "default": 25, "unit": "%"},
            "DryWet": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Delay": {"min": 0.1, "max": 10, "default": 2, "unit": "ms"},
            "HiCut": {"min": 1000, "max": 20000, "default": 15000, "unit": "Hz"}
        },
        "usage_tips": {
            "whoosh": "High feedback for jet-like sweeps",
            "subtle": "Low amounts for gentle movement",
            "stereo": "Different L/R rates for width",
            "drums": "Automation for build-ups"
        },
        "device_path": "Live/Flanger"
    },

    "Phaser": {
        "description": "Multi-stage phaser with envelope following options",
        "category": "modulation",
        "genres": ["funk", "rock", "electronic", "psychedelic"],
        "presets": {
            "classic": ["Vintage Phase", "4-Stage", "6-Stage", "8-Stage"],
            "envelope": ["Envelope Follow", "Auto Wah", "Dynamic Phase", "Touch Phase"],
            "lfo": ["Slow Phase", "Fast Phase", "Triplet Phase", "Random Phase"],
            "feedback": ["Resonant", "Gentle", "Extreme", "Notch"]
        },
        "key_parameters": {
            "Rate": {"min": 0.01, "max": 20, "default": 0.5, "unit": "Hz"},
            "Amount": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Feedback": {"min": -95, "max": 95, "default": 0, "unit": "%"},
            "DryWet": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Frequency": {"min": 200, "max": 8000, "default": 1000, "unit": "Hz"},
            "Env_Amount": {"min": 0, "max": 100, "default": 0, "unit": "%"}
        },
        "usage_tips": {
            "funk": "Medium rate with envelope following",
            "psychedelic": "Slow rate with high feedback",
            "electronic": "Sync to tempo for rhythmic effects",
            "subtle": "Low amounts for gentle movement"
        },
        "device_path": "Live/Phaser"
    },

    "Auto_Pan": {
        "description": "Stereo panning with multiple waveform options",
        "category": "modulation",
        "genres": ["electronic", "ambient", "experimental", "pop"],
        "presets": {
            "basic": ["Sine Pan", "Triangle Pan", "Square Pan", "Random Pan"],
            "sync": ["1/4 Pan", "1/8 Pan", "1/16 Pan", "Triplet Pan"],
            "stereo": ["Wide Pan", "Narrow Pan", "Offset Pan", "Counter Pan"],
            "creative": ["Tremolo", "Gate Pan", "Envelope Pan", "Stepped Pan"]
        },
        "key_parameters": {
            "Rate": {"min": 0.01, "max": 20, "default": 1, "unit": "Hz"},
            "Amount": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Offset": {"min": -180, "max": 180, "default": 0, "unit": "degrees"},
            "Invert": {"options": ["Off", "On"], "default": "Off"},
            "Shape": {"options": ["Sine", "Triangle", "Saw Up", "Saw Down", "Square", "Random"], "default": "Sine"}
        },
        "usage_tips": {
            "movement": "Slow sine waves for gentle movement",
            "rhythmic": "Sync to tempo for musical panning",
            "stereo": "Create width with offset settings",
            "automation": "Use for build-ups and breakdowns"
        },
        "device_path": "Live/Auto Pan"
    },

    "Frequency_Shifter": {
        "description": "Frequency shifter with ring modulation capabilities",
        "category": "modulation",
        "genres": ["experimental", "electronic", "ambient", "industrial"],
        "presets": {
            "shift": ["Up Shift", "Down Shift", "Subtle Shift", "Extreme Shift"],
            "ring_mod": ["Bell Ring", "Metallic Ring", "Harsh Ring", "Subtle Ring"],
            "creative": ["Alien Voice", "Robot Voice", "Shimmer", "Detuned"],
            "wide": ["Wide Shift", "Stereo Shift", "Counter Shift", "Ping Shift"]
        },
        "key_parameters": {
            "Coarse": {"min": -500, "max": 500, "default": 0, "unit": "Hz"},
            "Fine": {"min": -100, "max": 100, "default": 0, "unit": "cents"},
            "Drive": {"min": 0, "max": 100, "default": 0, "unit": "%"},
            "DryWet": {"min": 0, "max": 100, "default": 50, "unit": "%"},
            "Wide": {"min": 0, "max": 100, "default": 0, "unit": "%"}
        },
        "usage_tips": {
            "vocals": "Small shifts for character changes",
            "bells": "Ring modulation for metallic sounds",
            "pads": "Wide stereo shifting for movement",
            "special_fx": "Extreme settings for alien sounds"
        },
        "device_path": "Live/Frequency Shifter"
    }
}