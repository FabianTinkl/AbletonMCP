"""
Breakbeat Genre Knowledge Base
Based on breakbeat and big beat characteristics
"""

# Breakbeat BPM ranges by subgenre
BREAKBEAT_BPMS = {
    "big_beat": (120, 140),
    "nu_skool_breaks": (125, 135),
    "progressive_breaks": (128, 138),
    "tech_breaks": (130, 140),
    "acid_breaks": (125, 140),
    "jungle_breaks": (160, 180),
    "breakcore": (150, 200)
}

# Common breakbeat patterns (classic breaks)
BREAKBEAT_PATTERNS = {
    "amen_break": "X..X.X.XX.X.X..X",
    "think_break": "X.X.X.X.X.X.X.X.",
    "funky_drummer": "X...X.X.X...X.X.",
    "apache_break": "X.X..X.XX.X..X.X"
}

# Breakbeat characteristics
BREAKBEAT_CHARACTERISTICS = {
    "atmosphere": [
        "Funky and groovy",
        "Hip-hop influenced",
        "Sample-based",
        "Breakbeat-focused",
        "Underground culture"
    ],
    "instruments": [
        "Classic breakbeats",
        "Hip-hop samples",
        "Analog bass sounds",
        "Turntable scratches",
        "Vocal samples"
    ],
    "production": [
        "Sample manipulation",
        "Breakbeat chopping",
        "Analog processing",
        "Turntable techniques",
        "Hip-hop influence"
    ]
}

# Breakbeat scales
BREAKBEAT_SCALES = {
    "minor_pentatonic": [0, 3, 5, 7, 10],
    "blues_scale": [0, 3, 5, 6, 7, 10],
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10]
}

# Production techniques
BREAKBEAT_PRODUCTION_TECHNIQUES = {
    "break_manipulation": [
        "Time-stretching",
        "Chopping and rearranging",
        "Layering breaks",
        "Ghost snare programming",
        "Swing adjustment"
    ],
    "sampling": [
        "Vinyl record sampling",
        "Hip-hop sampling techniques",
        "Vocal chops",
        "Instrumental loops",
        "One-shot samples"
    ]
}