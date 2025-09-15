"""
Drum & Bass Genre Knowledge Base
Based on Beatport categorization and D&B characteristics
"""

# Drum & Bass BPM ranges by subgenre
DNB_BPMS = {
    "liquid_dnb": (168, 176),
    "neurofunk": (170, 180),
    "jump_up": (172, 178),
    "minimal_dnb": (168, 174),
    "jungle": (160, 180),
    "hardstep": (174, 180),
    "tech_dnb": (170, 176),
    "ambient_dnb": (160, 170)
}

# Common chord progressions for D&B (often jazz-influenced)
DNB_PROGRESSIONS = {
    "Am": [
        ["Am", "Dm7", "G7", "CM7"],    # Jazz ii-V-I in C
        ["Am7", "F", "C", "G"],        # Smooth progression
        ["Am", "F", "G", "Em"],        # Minor modal
        ["Am7", "Dm7", "GM7", "CM7"],  # Jazz sevenths
        ["Am", "G", "F", "E7"]         # Leading tone resolution
    ],
    "Dm": [
        ["Dm7", "G7", "CM7", "A7"],    # Jazz cycle
        ["Dm", "Bb", "F", "C"],        # Modal interchange
        ["Dm7", "Am7", "BbM7", "FM7"], # Smooth jazz
        ["Dm", "Em", "F", "G"]         # Ascending progression
    ],
    "Em": [
        ["Em7", "A7", "DM7", "GM7"],   # Jazz in D major
        ["Em", "C", "G", "D"],         # Rock progression in Em
        ["Em7", "Am7", "D7", "GM7"],   # ii-V in G
        ["Em", "Bm", "C", "G"]         # Modal Em progression
    ]
}

# D&B characteristics by subgenre
DNB_CHARACTERISTICS = {
    "liquid_dnb": {
        "atmosphere": [
            "Smooth and flowing",
            "Jazz-influenced harmony",
            "Soulful and emotional",
            "Organic and natural",
            "Uplifting and positive"
        ],
        "instruments": [
            "Jazz chord progressions",
            "Smooth sub bass",
            "Vinyl-style drums",
            "Soulful vocal samples",
            "Lush pad sounds"
        ],
        "production": [
            "Warm analog compression",
            "Subtle reverb and delay",
            "Tape saturation",
            "Vintage-style filtering",
            "Smooth automation"
        ]
    },
    "neurofunk": {
        "atmosphere": [
            "Dark and clinical",
            "Precise and technical",
            "Futuristic and cold",
            "Complex and intricate",
            "Mechanical and robotic"
        ],
        "instruments": [
            "Reese bass sounds",
            "Complex drum programming",
            "Synthetic textures",
            "Modulated sequences",
            "Industrial sound design"
        ],
        "production": [
            "Precise timing and quantization",
            "Heavy processing and modulation",
            "Stereo manipulation",
            "Frequency modulation",
            "Complex automation"
        ]
    },
    "jump_up": {
        "atmosphere": [
            "Energetic and bouncy",
            "Party-oriented and fun",
            "Aggressive and in-your-face",
            "Simple and effective",
            "Crowd-pleasing"
        ],
        "instruments": [
            "Hoover-style bass",
            "Simple but effective drums",
            "Rave stabs and shots",
            "Vocal samples",
            "Classic breakbeats"
        ],
        "production": [
            "Compressed and punchy",
            "Distortion and saturation",
            "Simple but effective arrangement",
            "Focus on the drop",
            "High-energy mixing"
        ]
    }
}

# D&B drum patterns (complex breakbeat patterns)
DNB_DRUM_PATTERNS = {
    "amen_break": {
        "pattern": "X..X.X.XX.X.X..X",  # Classic Amen break
        "snare_hits": [4, 6, 8, 10, 12, 15],
        "kick_hits": [0, 3, 9, 14]
    },
    "think_break": {
        "pattern": "X.X.X.X.X.X.X.X.",  # Think break pattern
        "snare_hits": [2, 6, 10, 14],
        "kick_hits": [0, 4, 8, 12]
    },
    "liquid_pattern": {
        "pattern": "X...X.X.X...X.X.",  # Liquid-style pattern
        "snare_hits": [4, 6, 12, 14],
        "kick_hits": [0, 8]
    },
    "neurofunk_pattern": {
        "pattern": "X.X.XX.XX.X.XX.X",  # Complex neurofunk
        "snare_hits": [2, 4, 5, 7, 8, 10, 11, 13],
        "kick_hits": [0, 15]
    }
}

# D&B specific scales (jazz-influenced)
DNB_SCALES = {
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],        # Very common in D&B
    "minor_pentatonic": [0, 3, 5, 7, 10],     # Simple melodies
    "blues_scale": [0, 3, 5, 6, 7, 10],       # Bluesy flavor
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],     # Dominant sound
    "chromatic": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Full chromatic
}

# D&B chord types (often extended jazz chords)
DNB_CHORD_TYPES = {
    "minor7": [0, 3, 7, 10],          # Most common in D&B
    "major7": [0, 4, 7, 11],          # Jazz influence
    "dominant7": [0, 4, 7, 10],       # Blues/jazz sound
    "minor9": [0, 3, 7, 10, 14],      # Extended minor
    "major9": [0, 4, 7, 11, 14],      # Extended major
    "sus2": [0, 2, 7],                # Open sound
    "sus4": [0, 5, 7],                # Tension
    "dim7": [0, 3, 6, 9],            # Diminished tension
    "half_dim7": [0, 3, 6, 10],       # Jazz chord
    "add9": [0, 4, 7, 14]             # Added ninth
}

# D&B song structures (typically longer builds)
DNB_SONG_STRUCTURES = {
    "classic": {      # 128-160 bars
        "intro": 32,
        "buildup": 32,
        "drop": 64,
        "breakdown": 32,
        "drop2": 64,
        "outro": 32
    },
    "liquid": {       # Smoother structure
        "intro": 32,
        "section1": 64,
        "breakdown": 32,
        "section2": 64,
        "outro": 32
    },
    "neurofunk": {    # Technical structure
        "intro": 16,
        "buildup": 32,
        "drop": 64,
        "switch": 16,
        "drop2": 64,
        "outro": 16
    }
}

# Bass sound types in D&B
DNB_BASS_SOUNDS = {
    "sub_bass": [
        "Deep sine wave sub",
        "Filtered sub bass",
        "Modulated sub frequency",
        "808-style sub kick"
    ],
    "reese_bass": [
        "Detuned saw wave stack",
        "Low-pass filtered reese",
        "Modulated reese bass",
        "Distorted reese sound"
    ],
    "neurofunk_bass": [
        "Complex modulated bass",
        "Granular synthesis bass",
        "FM synthesis bass",
        "Multi-layered bass stack"
    ],
    "liquid_bass": [
        "Smooth sine bass",
        "Jazz-style upright bass",
        "Warm analog bass",
        "Filtered vintage bass"
    ]
}

# D&B production techniques
DNB_PRODUCTION_TECHNIQUES = {
    "breakbeat_manipulation": [
        "Time-stretching breaks",
        "Chopping and rearranging",
        "Layering multiple breaks",
        "Ghost note programming",
        "Swing and groove adjustment"
    ],
    "bass_design": [
        "Reese bass creation",
        "Sub bass layering", 
        "Modulation and automation",
        "Distortion and saturation",
        "Frequency splitting"
    ],
    "arrangement": [
        "32-bar intro sections",
        "Energy curve management",
        "Drop timing and impact",
        "Breakdown effectiveness",
        "Smooth transitions"
    ],
    "mixing": [
        "Frequency separation",
        "Parallel compression",
        "Stereo width management",
        "Dynamic range preservation",
        "Transient shaping"
    ],
    "effects": [
        "Gating and chopping",
        "Reverb for space",
        "Delay for rhythm",
        "Distortion for character",
        "Filtering for movement"
    ]
}

# Tempo change techniques in D&B
DNB_TEMPO_TECHNIQUES = {
    "half_time": {
        "description": "Drums play at half tempo feeling",
        "kick_pattern": "X.......X.......",
        "snare_pattern": "........X......."
    },
    "double_time": {
        "description": "Drums play at double tempo feeling", 
        "kick_pattern": "X.X.X.X.X.X.X.X.",
        "snare_pattern": "..X...X...X...X."
    },
    "switch_up": {
        "description": "Tempo switches within the track",
        "common_switches": ["170->85->170", "174->87->174"]
    }
}