"""
Techno Genre Knowledge Base
"""

# Typical BPM ranges for different techno substyles
TECHNO_BPMS = {
    "minimal": (125, 132),
    "detroit": (130, 140), 
    "berlin": (128, 136),
    "industrial": (128, 140),
    "peak_time": (130, 138),
    "underground": (128, 135),
    "hard_techno": (140, 150)
}

# Common chord progressions for techno music
TECHNO_PROGRESSIONS = {
    "Am": [
        ["Am", "F", "C", "G"],
        ["Am", "Dm", "G", "C"], 
        ["Am", "F", "G", "Am"],
        ["Am", "C", "F", "G"],
        ["Am", "F", "Dm", "G"],
        ["Am", "Em", "F", "G"]
    ],
    "Dm": [
        ["Dm", "Bb", "F", "C"],
        ["Dm", "Gm", "C", "F"],
        ["Dm", "Bb", "C", "Dm"],
        ["Dm", "F", "Bb", "C"],
        ["Dm", "Am", "Bb", "F"]
    ],
    "Em": [
        ["Em", "C", "G", "D"],
        ["Em", "Am", "D", "G"],
        ["Em", "C", "D", "Em"],
        ["Em", "G", "C", "D"],
        ["Em", "Bm", "C", "D"]
    ],
    "Gm": [
        ["Gm", "Eb", "Bb", "F"],
        ["Gm", "Cm", "F", "Bb"],
        ["Gm", "Eb", "F", "Gm"],
        ["Gm", "Dm", "Eb", "F"]
    ]
}

# Industrial techno characteristics
INDUSTRIAL_ELEMENTS = {
    "atmosphere": [
        "Dark and heavy",
        "Mechanical and cold", 
        "Dystopian and aggressive",
        "Spatial and reverberant",
        "Distorted and harsh"
    ],
    "sounds": [
        "Metal hits and clangs",
        "Factory machinery samples",
        "Distorted drum machines",
        "Analog synthesizer leads",
        "Reverb-heavy percussion"
    ],
    "effects": [
        "Heavy reverb and delay",
        "Distortion and saturation", 
        "Filtering and resonance",
        "Compression for punch",
        "Stereo widening"
    ]
}

# Song structure templates (in bars)
SONG_STRUCTURES = {
    "short": {  # 32-48 bars
        "intro": 8,
        "buildup": 8,
        "drop": 16,
        "outro": 8
    },
    "medium": {  # 64 bars
        "intro": 8,
        "buildup": 8, 
        "drop": 24,
        "breakdown": 8,
        "drop2": 8,
        "outro": 8
    },
    "long": {  # 96+ bars
        "intro": 16,
        "buildup": 16,
        "drop": 32,
        "breakdown": 16,
        "buildup2": 16,
        "drop2": 24,
        "outro": 16
    }
}

# Drum patterns (16 steps, X = hit, . = rest)
DRUM_PATTERNS = {
    "kick": {
        "four_on_floor": "X...X...X...X...",
        "syncopated": "X...X..XX..X....",
        "minimal": "X.......X.......",
        "industrial": "X..XX...X.X.X..."
    },
    "snare": {
        "standard": "....X.......X...",
        "offbeat": "..X...X.....X...",
        "industrial": "....X.X.....X.X.",
        "minimal": "........X......."
    },
    "hihat": {
        "steady": "..X...X...X...X.",
        "driving": "X.X.X.X.X.X.X.X.",
        "minimal": "..X.....X.......",
        "complex": "X.XX..X.X.X..XX."
    }
}

# Scale and chord information
SCALES = {
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],  # W-H-W-W-H-W-W
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11], 
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10]
}

# Common techno chord types
CHORD_TYPES = {
    "minor": [0, 3, 7],
    "major": [0, 4, 7], 
    "minor7": [0, 3, 7, 10],
    "major7": [0, 4, 7, 11],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "add9": [0, 4, 7, 14],  # 14 = 2 + 12 (octave)
    "power": [0, 7]  # Root and fifth only
}