"""
Trance Music Genre Knowledge Base
Based on Beatport categorization and trance music characteristics
"""

# Trance music BPM ranges by subgenre
TRANCE_BPMS = {
    "progressive_trance": (128, 136),
    "uplifting_trance": (132, 140),
    "tech_trance": (130, 138),
    "vocal_trance": (128, 136),
    "psy_trance": (135, 150),
    "hard_trance": (140, 150),
    "ambient_trance": (120, 132),
    "classic_trance": (130, 140)
}

# Common chord progressions for trance music
TRANCE_PROGRESSIONS = {
    "Am": [
        ["Am", "F", "C", "G"],      # Emotional minor progression
        ["Am", "G", "F", "E"],      # Dramatic descending
        ["Am", "Dm", "G", "C"],     # Circle of fifths
        ["Am", "F", "G", "Am"],     # Looping minor
        ["Am", "C", "F", "G"]       # Relative major lift
    ],
    "Em": [
        ["Em", "C", "G", "D"],      # Epic progression
        ["Em", "Am", "D", "G"],     # Modal progression
        ["Em", "C", "Am", "B7"],    # Leading tone resolution
        ["Em", "D", "C", "B7"],     # Descending emotional
        ["Em", "G", "C", "Am"]      # Major lift progression
    ],
    "Dm": [
        ["Dm", "Bb", "F", "C"],     # Classic minor progression
        ["Dm", "Am", "Bb", "F"],    # Relative progression
        ["Dm", "C", "Bb", "A7"],    # Dominant resolution
        ["Dm", "F", "Bb", "C"]      # Uplifting minor
    ],
    "Bm": [
        ["Bm", "G", "D", "A"],      # Epic B minor
        ["Bm", "F#m", "G", "A"],    # Modal B minor
        ["Bm", "Em", "A", "D"],     # Circle progression
        ["Bm", "D", "G", "A"]       # Major relative lift
    ]
}

# Trance music characteristics by subgenre
TRANCE_CHARACTERISTICS = {
    "progressive_trance": {
        "atmosphere": [
            "Building and evolving",
            "Emotional and cinematic",
            "Spacious and atmospheric", 
            "Hypnotic and flowing",
            "Journey-like progression"
        ],
        "instruments": [
            "Evolving pad layers",
            "Melodic basslines",
            "Arpeggiated sequences", 
            "Emotional lead synths",
            "Ethereal vocal elements"
        ],
        "production": [
            "Long filter sweeps",
            "Gradual layering",
            "Spatial reverbs",
            "Side-chain pumping",
            "Smooth transitions"
        ]
    },
    "uplifting_trance": {
        "atmosphere": [
            "Euphoric and emotional",
            "Uplifting and inspirational",
            "Energy building",
            "Peak-time oriented",
            "Hands-in-the-air moments"
        ],
        "instruments": [
            "Supersaw lead stacks",
            "Emotional chord progressions",
            "Arpeggiated plucks",
            "Epic breakdown elements",
            "Uplifting bass patterns"
        ],
        "production": [
            "Wide stereo supersaws",
            "Compression for energy",
            "High-frequency emphasis",
            "Dynamic range for impact",
            "Precise timing and quantization"
        ]
    },
    "psy_trance": {
        "atmosphere": [
            "Psychedelic and trippy",
            "Driving and relentless",
            "Hypnotic and mind-bending",
            "Tribal and primal",
            "Cosmic and otherworldly"
        ],
        "instruments": [
            "Acid-style sequences",
            "Morphing lead sounds",
            "Tribal percussion",
            "Psychedelic effects",
            "Rolling basslines"
        ],
        "production": [
            "Heavy filtering and modulation",
            "Psychoacoustic effects",
            "Stereo manipulation",
            "Complex automation",
            "Frequency modulation synthesis"
        ]
    }
}

# Trance drum patterns (16 steps)
TRANCE_DRUM_PATTERNS = {
    "kick": {
        "four_on_floor": "X...X...X...X...",  # Standard trance kick
        "progressive": "X.......X.......",    # More spacious
        "uplifting": "X...X...X...X...",     # Consistent energy
        "psy": "X..X.X..X..X.X..",           # Syncopated psytrance
        "hard": "X...X.X.X...X.."            # Hard trance pattern
    },
    "snare": {
        "standard": "....X.......X...",      # Classic 2 & 4
        "clap": "....X.......X...",
        "layered": "....XX......XX..",       # Double snare hits
        "reversed": "...RX.......RX..",      # R = reversed snare
        "minimal": "........X......."        # Minimal snare usage
    },
    "hihat": {
        "classic": "..X...X...X...X.",       # Offbeat pattern
        "open": "......X.......X.",         # Open hats
        "closed": "X.X.X.X.X.X.X.X.",       # 8th note closed
        "triplet": "X..X..X.X..X..X.",       # Triplet feel
        "rolling": "XXXXXXXXXXXXXXXX"        # Rolling hi-hats
    },
    "perc": {
        "shaker": "X.X.X.X.X.X.X.X.",       # Constant shaker
        "ride": "X.....X.X.....X.",         # Ride cymbal pattern
        "tambourine": "....X.X.....X.X.",    # Tambourine accents
        "tribal": "X..X.X..X..X.X..",       # Tribal percussion
        "bells": "......X.......X."         # Sparse bells
    }
}

# Trance-specific scales and modes
TRANCE_SCALES = {
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],    # Most common in trance
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],   # Dramatic sound
    "dorian": [0, 2, 3, 5, 7, 9, 10],           # Progressive trance
    "aeolian": [0, 2, 3, 5, 7, 8, 10],          # Natural minor mode
    "phrygian": [0, 1, 3, 5, 7, 8, 10],         # Dark, exotic sound
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],       # Dominant 7th sound
    "pentatonic_minor": [0, 3, 5, 7, 10],        # Emotional melodies
    "hungarian_minor": [0, 2, 3, 6, 7, 8, 11]   # Exotic, dramatic
}

# Trance chord types and extensions
TRANCE_CHORD_TYPES = {
    "minor": [0, 3, 7],           # Basic minor triad
    "major": [0, 4, 7],           # Basic major triad
    "minor7": [0, 3, 7, 10],      # Minor seventh
    "major7": [0, 4, 7, 11],      # Major seventh
    "sus2": [0, 2, 7],            # Suspended second
    "sus4": [0, 5, 7],            # Suspended fourth
    "add9": [0, 4, 7, 14],        # Added ninth
    "minor_add9": [0, 3, 7, 14],  # Minor with added ninth
    "dominant7": [0, 4, 7, 10],   # Dominant seventh
    "diminished": [0, 3, 6],      # Diminished triad
    "augmented": [0, 4, 8],       # Augmented triad
    "minor_major7": [0, 3, 7, 11] # Minor with major seventh
}

# Trance song structures (in bars)
TRANCE_SONG_STRUCTURES = {
    "classic": {      # 128-160 bars - full trance journey
        "intro": 32,
        "buildup1": 16,
        "breakdown1": 32,
        "buildup2": 16,
        "climax": 32,
        "breakdown2": 16,
        "buildup3": 16,
        "outro": 32
    },
    "progressive": {  # 160-192 bars - long form progression
        "intro": 32,
        "section1": 32,
        "transition1": 16,
        "section2": 32,
        "breakdown": 32,
        "buildup": 32,
        "climax": 48,
        "outro": 32
    },
    "uplifting": {    # 128 bars - peak time energy
        "intro": 16,
        "buildup1": 32,
        "breakdown": 32,
        "buildup2": 32,
        "drop": 32,
        "outro": 16
    },
    "radio": {        # 64-80 bars - radio edit
        "intro": 8,
        "verse": 16,
        "buildup": 8,
        "chorus": 24,
        "breakdown": 8,
        "outro": 8
    }
}

# Typical trance instruments and sounds
TRANCE_INSTRUMENTS = {
    "bass": [
        "Deep rolling bassline",
        "Acid-style TB-303",
        "Supersaw bass layer",
        "Sub bass foundation",
        "Modulated bass synth"
    ],
    "lead": [
        "Supersaw lead stack",
        "Emotional lead synth",
        "Plucked arpeggiator",
        "Acid lead sequence",
        "Vocal-like lead pad"
    ],
    "pads": [
        "Lush string pad",
        "Evolving ambient pad",
        "Choir-like pad",
        "Analog string machine",
        "Atmospheric texture"
    ],
    "fx": [
        "Reverse reverb sweeps",
        "White noise risers",
        "Impact sounds",
        "Vocal chops",
        "Atmospheric textures"
    ],
    "percussion": [
        "Analog drum machine",
        "Ethnic percussion",
        "Shaker and tambourine",
        "Ride cymbals",
        "Tribal drums"
    ]
}

# Trance production techniques
TRANCE_PRODUCTION_TECHNIQUES = {
    "layering": [
        "Supersaw lead stacking",
        "Multiple pad layers",
        "Harmonic bassline layers",
        "Percussion layering"
    ],
    "filtering": [
        "Low-pass filter sweeps",
        "High-pass filter builds",
        "Resonant filter emphasis",
        "Automated filter movements"
    ],
    "effects": [
        "Gate/trance gate on pads",
        "Reverb for space and depth",
        "Delay for rhythm and space",
        "Chorus for width and movement",
        "Phaser for sweeping effects"
    ],
    "arrangement": [
        "32-bar phrase structures",
        "Energy curve management",
        "Breakdown/buildup dynamics",
        "Layered arrangement builds",
        "Smooth transitions between sections"
    ],
    "mixing": [
        "Side-chain compression",
        "Wide stereo imaging",
        "Frequency separation",
        "Dynamic range for impact",
        "Parallel compression"
    ]
}

# Trance energy curve templates
TRANCE_ENERGY_CURVES = {
    "progressive": [
        (0, 30),    # Intro - low energy
        (32, 50),   # Building
        (64, 70),   # First peak
        (96, 40),   # Breakdown
        (128, 85),  # Main climax
        (160, 60),  # Wind down
        (192, 20)   # Outro
    ],
    "uplifting": [
        (0, 40),    # Intro
        (16, 60),   # Quick build
        (32, 90),   # First drop
        (64, 30),   # Breakdown
        (96, 95),   # Main drop
        (128, 25)   # Outro
    ]
}