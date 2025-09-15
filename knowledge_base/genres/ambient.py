"""
Ambient Music Genre Knowledge Base
Based on ambient and downtempo characteristics
"""

# Ambient BPM ranges by subgenre
AMBIENT_BPMS = {
    "ambient": (60, 100),
    "dark_ambient": (60, 90),
    "drone": (50, 80),
    "new_age": (70, 110),
    "chillout": (90, 120),
    "downtempo": (80, 110),
    "trip_hop": (85, 115),
    "lofi": (70, 95)
}

# Ambient chord progressions (extended and atmospheric)
AMBIENT_PROGRESSIONS = {
    "C": [
        ["CM7", "Am7", "FM7", "GM7"],    # Smooth jazz progression
        ["C", "F", "Am", "G"],          # Simple and open
        ["CM9", "Am9", "FM9", "GM9"],   # Extended ninths
        ["C", "Em", "F", "G"]           # Basic progression
    ],
    "Am": [
        ["Am7", "Dm7", "GM7", "CM7"],   # Minor jazz
        ["Am", "F", "C", "G"],          # Relative major
        ["Am9", "FM9", "CM9", "GM9"],   # Extended harmony
        ["Am", "Em", "F", "C"]          # Natural minor
    ]
}

# Ambient characteristics
AMBIENT_CHARACTERISTICS = {
    "atmosphere": [
        "Spacious and ethereal",
        "Meditative and calming",
        "Textural and evolving",
        "Non-rhythmic focus",
        "Immersive soundscapes"
    ],
    "instruments": [
        "Lush pad synthesizers",
        "Field recordings",
        "Processed acoustic instruments",
        "Granular textures",
        "Reverb-heavy elements"
    ],
    "production": [
        "Long reverb tails",
        "Subtle compression",
        "Wide stereo imaging",
        "Slow parameter automation",
        "Organic movement"
    ]
}

# Ambient scales
AMBIENT_SCALES = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "pentatonic": [0, 2, 4, 7, 9],
    "whole_tone": [0, 2, 4, 6, 8, 10]
}

# Ambient production techniques
AMBIENT_PRODUCTION_TECHNIQUES = {
    "texture_creation": [
        "Granular synthesis",
        "Reverse reverb",
        "Pitch shifting",
        "Time stretching",
        "Field recording processing"
    ],
    "arrangement": [
        "Slow evolution",
        "Minimal structure",
        "Continuous flow",
        "Subtle layering",
        "Natural dynamics"
    ]
}