"""
House Music Genre Knowledge Base
Based on Beatport categorization and house music characteristics
"""

# House music BPM ranges by subgenre
HOUSE_BPMS = {
    "deep_house": (118, 125),
    "tech_house": (120, 128), 
    "progressive_house": (120, 130),
    "electro_house": (125, 135),
    "future_house": (120, 128),
    "tropical_house": (100, 118),
    "classic_house": (118, 125),
    "acid_house": (115, 130)
}

# Common chord progressions for house music
HOUSE_PROGRESSIONS = {
    "C": [
        ["C", "Am", "F", "G"],  # vi-IV-I-V classic
        ["C", "F", "Am", "G"],  # I-IV-vi-V pop progression
        ["C", "G", "Am", "F"],  # I-V-vi-IV pop progression
        ["C", "Em", "F", "G"],  # I-iii-IV-V
        ["C", "Dm", "G", "C"]   # I-ii-V-I jazz influenced
    ],
    "Am": [
        ["Am", "F", "C", "G"],  # vi-IV-I-V 
        ["Am", "Dm", "G", "Em"], # i-iv-VII-v
        ["Am", "F", "G", "Am"],  # i-VI-VII-i
        ["Am", "C", "F", "G"]    # i-III-VI-VII
    ],
    "F": [
        ["F", "C", "Dm", "Bb"],  # I-V-vi-IV
        ["F", "Gm", "C", "Am"],  # I-ii-V-iii
        ["F", "Am", "Bb", "C"],  # I-iii-IV-V
        ["F", "Dm", "Gm", "C"]   # I-vi-ii-V
    ],
    "G": [
        ["G", "Em", "C", "D"],   # I-vi-IV-V
        ["G", "C", "Am", "D"],   # I-IV-ii-V
        ["G", "Am", "F", "C"],   # I-ii-bVII-IV
        ["G", "D", "Em", "C"]    # I-V-vi-IV
    ]
}

# House music characteristics by subgenre
HOUSE_CHARACTERISTICS = {
    "deep_house": {
        "atmosphere": [
            "Warm and soulful",
            "Jazzy and sophisticated", 
            "Relaxed and groovy",
            "Minimal and spacious",
            "Emotional and uplifting"
        ],
        "instruments": [
            "Jazz-influenced chords",
            "Smooth basslines",
            "Soulful vocals",
            "Warm pads and strings",
            "Subtle percussion"
        ],
        "production": [
            "Warm compression",
            "Subtle reverb and delay",
            "Side-chain compression",
            "Analog-style filtering",
            "Tape saturation"
        ]
    },
    "tech_house": {
        "atmosphere": [
            "Driving and energetic",
            "Minimal and focused",
            "Underground and raw",
            "Hypnotic and repetitive",
            "Club-oriented"
        ],
        "instruments": [
            "Analog-style basslines",
            "Minimal techno elements",
            "Percussive loops",
            "Filtered house chords",
            "Vocal samples"
        ],
        "production": [
            "Tight compression",
            "High-pass filtering",
            "Percussion layering",
            "Analog modeling",
            "Groove quantization"
        ]
    },
    "progressive_house": {
        "atmosphere": [
            "Epic and uplifting",
            "Emotional and cinematic",
            "Building and evolving",
            "Melodic and harmonic",
            "Festival-oriented"
        ],
        "instruments": [
            "Lush pad progressions",
            "Melodic basslines", 
            "Arpeggiated sequences",
            "Emotional leads",
            "Orchestral elements"
        ],
        "production": [
            "Wide stereo imaging",
            "Long reverb tails",
            "Gradual filtering",
            "Dynamic automation",
            "Harmonic layering"
        ]
    }
}

# House drum patterns (16 steps)
HOUSE_DRUM_PATTERNS = {
    "kick": {
        "four_on_floor": "X...X...X...X...",  # Classic house kick
        "classic": "X...X...X...X...",
        "deep": "X.......X.......",  # More spaced out
        "tech": "X..X....X..X....",  # Tech house variation
        "progressive": "X...X...X...X..."  # Standard 4/4
    },
    "snare": {
        "standard": "....X.......X...",  # On beats 2 and 4
        "clap": "....X.......X...",
        "deep": "........X.......",  # Minimal snare
        "layered": "....XX......XX.."  # Double hits
    },
    "hihat": {
        "classic": "..X...X...X...X.",  # Offbeat
        "open": "......X.......X.",  # Open hats on offbeat
        "closed": "X.X.X.X.X.X.X.X.",  # 8th note pattern
        "shuffle": "X..X..X.X..X..X."  # Shuffled groove
    },
    "perc": {
        "shaker": "X.X.X.X.X.X.X.X.",  # Constant shaker
        "conga": "..X.....X.X.....",  # Latin percussion
        "tambourine": "....X.X.....X.X.",  # Accent pattern
        "cowbell": "......X.......X."   # Sparse cowbell
    }
}

# House music scales (semitones from root)
HOUSE_SCALES = {
    "major": [0, 2, 4, 5, 7, 9, 11],      # Natural major
    "minor": [0, 2, 3, 5, 7, 8, 10],      # Natural minor
    "dorian": [0, 2, 3, 5, 7, 9, 10],     # Popular in house
    "mixolydian": [0, 2, 4, 5, 7, 9, 10], # Dominant 7th sound
    "pentatonic_major": [0, 2, 4, 7, 9],   # Safe melodic choice
    "pentatonic_minor": [0, 3, 5, 7, 10]   # Bluesy feel
}

# House chord types and voicings
HOUSE_CHORD_TYPES = {
    "major": [0, 4, 7],           # Basic triad
    "minor": [0, 3, 7],           # Basic minor
    "major7": [0, 4, 7, 11],      # Jazz influence
    "minor7": [0, 3, 7, 10],      # Smooth minor
    "dominant7": [0, 4, 7, 10],   # Bluesy edge
    "sus2": [0, 2, 7],            # Open sound
    "sus4": [0, 5, 7],            # Tension and release
    "add9": [0, 4, 7, 14],        # Extended harmony
    "6": [0, 4, 7, 9],            # Vintage house sound
    "minor6": [0, 3, 7, 9]        # Sophisticated minor
}

# Common house song structures (in bars)
HOUSE_SONG_STRUCTURES = {
    "classic": {     # 128 bars - classic house length
        "intro": 16,
        "verse": 16,
        "buildup": 16,
        "drop": 32,
        "breakdown": 16,
        "buildup2": 16,
        "drop2": 32,
        "outro": 16
    },
    "club": {        # 96 bars - club mix
        "intro": 16,
        "buildup": 16,
        "drop": 32,
        "breakdown": 16,
        "drop2": 32,
        "outro": 16
    },
    "radio": {       # 64 bars - radio edit
        "intro": 8,
        "verse": 16,
        "chorus": 16,
        "verse2": 8,
        "chorus2": 16,
        "outro": 8
    }
}

# Typical house instruments and sounds
HOUSE_INSTRUMENTS = {
    "bass": [
        "Deep sub bass",
        "Filtered analog bass",
        "Reese-style bass",
        "Plucked bass synth",
        "808-style sub"
    ],
    "chords": [
        "Vintage electric piano",
        "Analog string machine",
        "Warm pad synthesizer",
        "Hammond organ",
        "Jazz guitar samples"
    ],
    "lead": [
        "Analog synthesizer lead",
        "Vocal chops",
        "Piano melody",
        "String section",
        "Brass stabs"
    ],
    "percussion": [
        "Analog drum machine",
        "Live percussion samples",
        "Vinyl crackle",
        "Shaker loops",
        "Conga rhythms"
    ]
}

# Production techniques specific to house
HOUSE_PRODUCTION_TECHNIQUES = {
    "swing_and_groove": [
        "16th note swing (8-15%)",
        "Micro-timing adjustments",
        "Velocity humanization",
        "Groove templates from classic tracks"
    ],
    "filtering": [
        "High-pass filter sweeps",
        "Low-pass filter for breakdown",
        "Resonant filter for emphasis",
        "Notch filtering for space"
    ],
    "compression": [
        "Side-chain compression to kick",
        "Vintage-style bus compression",
        "Parallel compression on drums",
        "Multiband compression on master"
    ],
    "effects": [
        "Tape delay for depth",
        "Plate reverb for warmth",
        "Phaser on hi-hats", 
        "Chorus on chords"
    ]
}