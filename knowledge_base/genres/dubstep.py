"""
Dubstep Genre Knowledge Base
Based on Beatport categorization and dubstep characteristics
"""

# Dubstep BPM ranges by subgenre
DUBSTEP_BPMS = {
    "classic_dubstep": (138, 142),
    "brostep": (140, 145),
    "future_garage": (130, 140),
    "melodic_dubstep": (138, 142),
    "riddim": (140, 150),
    "chillstep": (120, 140),
    "dubstyle": (140, 150),
    "trapstep": (140, 160)
}

# Dubstep chord progressions (often minor and dramatic)
DUBSTEP_PROGRESSIONS = {
    "Em": [
        ["Em", "C", "G", "D"],          # Epic progression
        ["Em", "Am", "C", "G"],         # Emotional build
        ["Em", "C", "Am", "B7"],        # Leading tone drama
        ["Em", "D", "C", "B7"],         # Descending tension
        ["Em", "G", "C", "Am"]          # Relative major lift
    ],
    "Am": [
        ["Am", "F", "C", "G"],          # Classic minor
        ["Am", "G", "F", "E"],          # Dramatic descent  
        ["Am", "Dm", "G", "C"],         # Circle progression
        ["Am", "F", "G", "Am"],         # Looping minor
        ["Am", "C", "F", "G"]           # Major resolution
    ],
    "Bm": [
        ["Bm", "G", "D", "A"],          # Epic B minor
        ["Bm", "Em", "A", "D"],         # Modal progression
        ["Bm", "D", "G", "A"],          # Major lift
        ["Bm", "F#m", "G", "A"]         # Chromatic approach
    ],
    "Dm": [
        ["Dm", "Bb", "F", "C"],         # Classic Dm
        ["Dm", "Am", "Bb", "F"],        # Relative approach
        ["Dm", "C", "Bb", "A"],         # Dominant resolution
        ["Dm", "F", "Bb", "C"]          # Uplifting minor
    ]
}

# Dubstep characteristics by subgenre
DUBSTEP_CHARACTERISTICS = {
    "classic_dubstep": {
        "atmosphere": [
            "Dark and underground",
            "Minimal and spacious",
            "Sub-bass focused",
            "UK garage influenced",
            "Halfstep rhythms"
        ],
        "instruments": [
            "Deep sub bass",
            "Sparse percussion",
            "Vinyl crackle",
            "Dub-style delays",
            "Minimal melodic elements"
        ],
        "production": [
            "Sub bass emphasis",
            "Spacious arrangement",
            "Dub-style effects",
            "Minimal compression",
            "Analog warmth"
        ]
    },
    "brostep": {
        "atmosphere": [
            "Aggressive and heavy",
            "Festival and party oriented",
            "Maximum energy drops",
            "In-your-face attitude",
            "Crowd-focused impact"
        ],
        "instruments": [
            "Aggressive wobble bass",
            "Distorted lead synths",
            "Heavy drum sounds",
            "Vocal chops and samples",
            "Metallic and harsh textures"
        ],
        "production": [
            "Heavy compression and limiting",
            "Distortion and saturation",
            "Wide stereo imaging",
            "Maximum loudness",
            "Aggressive side-chaining"
        ]
    },
    "melodic_dubstep": {
        "atmosphere": [
            "Emotional and uplifting",
            "Melodic and harmonic",
            "Epic and cinematic",
            "Journey-like progression",
            "Feel-good energy"
        ],
        "instruments": [
            "Emotional lead melodies",
            "Lush pad progressions",
            "Clean vocal elements",
            "Orchestral components",
            "Smooth bass design"
        ],
        "production": [
            "Clean and polished sound",
            "Wide stereo field",
            "Dynamic range preservation",
            "Harmonic layering",
            "Smooth transitions"
        ]
    }
}

# Dubstep drum patterns (halfstep focus)
DUBSTEP_DRUM_PATTERNS = {
    "classic_halfstep": {
        "kick": "X.......X.......",      # Halfstep kick pattern
        "snare": "........X.......",     # Snare on 3
        "hihat": "..X...X...X...X.",     # Sparse hi-hats
        "perc": "....X.......X..."      # Minimal percussion
    },
    "brostep": {
        "kick": "X.......X.......",      # Heavy kick
        "snare": "........X.......",     # Snare hit
        "crash": "........X.......",     # Crash with snare
        "build": "X.X.X.X.X.X.X.X."     # Build-up pattern
    },
    "melodic": {
        "kick": "X.......X.......",      # Standard halfstep
        "snare": "........X.......",     # Clean snare
        "hihat": "..X.X.X...X.X.X.",     # More complex hats
        "ride": "X.....X.X.....X."      # Ride pattern
    },
    "riddim": {
        "kick": "X.X.....X.X.....",      # Syncopated kick
        "snare": "........X.......",     # Standard snare
        "hihat": "X.X.X.X.X.X.X.X.",     # Driving hats
        "perc": "..X...X...X...X."      # Riddim percussion
    }
}

# Dubstep bass design types
DUBSTEP_BASS_TYPES = {
    "wobble_bass": {
        "characteristics": ["LFO modulated filter", "Sawtooth wave base", "Low-pass filtering"],
        "modulation_rates": ["1/4 note", "1/8 note", "1/16 note", "Triplets"],
        "filter_types": ["Low-pass", "Band-pass", "High-pass", "Notch"]
    },
    "sub_bass": {
        "characteristics": ["Sine wave foundation", "40-80Hz frequency range", "Minimal modulation"],
        "techniques": ["Side-chain to kick", "Subtle filtering", "Octave doubling"]
    },
    "neuro_bass": {
        "characteristics": ["Complex modulation", "Multiple oscillators", "Granular synthesis"],
        "techniques": ["FM synthesis", "Wavetable scanning", "Complex automation"]
    },
    "growl_bass": {
        "characteristics": ["Distorted and aggressive", "Formant filtering", "Vocal-like qualities"],
        "techniques": ["Vocal formants", "Distortion chaining", "Dynamic filtering"]
    }
}

# Dubstep song structures
DUBSTEP_SONG_STRUCTURES = {
    "classic": {          # Standard dubstep structure
        "intro": 32,
        "verse": 32,
        "buildup": 16,
        "drop": 32,
        "breakdown": 16,
        "buildup2": 16, 
        "drop2": 32,
        "outro": 16
    },
    "festival": {         # Festival/brostep structure
        "intro": 16,
        "buildup": 32,
        "drop": 32,
        "breakdown": 16,
        "buildup2": 32,
        "drop2": 32,
        "outro": 8
    },
    "melodic": {          # Melodic dubstep structure
        "intro": 32,
        "verse": 32,
        "chorus": 32,
        "verse2": 16,
        "chorus2": 32,
        "bridge": 16,
        "final_chorus": 32,
        "outro": 16
    }
}

# Dubstep production techniques
DUBSTEP_PRODUCTION_TECHNIQUES = {
    "bass_design": [
        "LFO modulation on filters",
        "Distortion and saturation",
        "Multiple oscillator layering",
        "Side-chain compression",
        "Frequency splitting and processing"
    ],
    "buildup_techniques": [
        "White noise sweeps",
        "Filter automation",
        "Percussion rolls",
        "Reverse reverb",
        "Tension and release dynamics"
    ],
    "arrangement": [
        "32-bar sections",
        "Call and response structure", 
        "Energy curve management",
        "Impact timing",
        "Space and silence usage"
    ],
    "mixing": [
        "Sub bass management",
        "Mid-range clarity",
        "Stereo width control",
        "Dynamic range",
        "Frequency separation"
    ],
    "effects": [
        "Dub-style delays",
        "Reverb for space",
        "Distortion for character",
        "Filtering for movement",
        "Gating and chopping"
    ]
}

# Dubstep scales (often dark and minor)
DUBSTEP_SCALES = {
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],     # Most common
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],    # Dramatic sound
    "dorian": [0, 2, 3, 5, 7, 9, 10],            # Slightly brighter minor
    "phrygian": [0, 1, 3, 5, 7, 8, 10],          # Dark and exotic
    "minor_pentatonic": [0, 3, 5, 7, 10],         # Simple and effective
    "blues_scale": [0, 3, 5, 6, 7, 10],           # Bluesy edge
    "chromatic": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Full chromatic
}

# Dubstep chord types
DUBSTEP_CHORD_TYPES = {
    "minor": [0, 3, 7],           # Basic minor
    "major": [0, 4, 7],           # Basic major  
    "sus2": [0, 2, 7],            # Open sound
    "sus4": [0, 5, 7],            # Tension
    "minor7": [0, 3, 7, 10],      # Minor seventh
    "major7": [0, 4, 7, 11],      # Major seventh
    "add9": [0, 4, 7, 14],        # Added ninth
    "power": [0, 7],              # Power chord
    "diminished": [0, 3, 6],      # Diminished tension
    "augmented": [0, 4, 8]        # Augmented tension
}

# Drop design templates
DUBSTEP_DROP_TEMPLATES = {
    "classic": {
        "bar_1": "Kick + Sub bass",
        "bar_2": "Add snare",
        "bar_3": "Introduce wobble",
        "bar_4": "Full arrangement",
        "repeat": "Vary wobble pattern"
    },
    "melodic": {
        "bar_1": "Kick + melodic lead",
        "bar_2": "Add harmony",
        "bar_3": "Introduce bass",
        "bar_4": "Full orchestration",
        "repeat": "Develop melody"
    },
    "riddim": {
        "bar_1": "Syncopated kick pattern",
        "bar_2": "Add riddim bass",
        "bar_3": "Introduce percussion",
        "bar_4": "Full riddim groove",
        "repeat": "Vary bass modulation"
    }
}