"""
Instruments Knowledge Base

This module contains comprehensive information about Ableton Live Suite instruments,
including categorization, presets, parameters, and genre recommendations.
"""

from .synthesizers import SYNTHESIZERS
from .samplers import SAMPLERS
from .drums import DRUMS
from .bass import BASS_INSTRUMENTS
from .pads import PADS
from .leads import LEADS
from .keys import KEYS

# Master instruments database
INSTRUMENTS_DB = {
    "synthesizers": SYNTHESIZERS,
    "samplers": SAMPLERS,
    "drums": DRUMS,
    "bass": BASS_INSTRUMENTS,
    "pads": PADS,
    "leads": LEADS,
    "keys": KEYS
}

# Genre-specific instrument recommendations
GENRE_INSTRUMENTS = {
    "techno": {
        "drums": ["Drum_Kit", "Analog_Kick", "Techno_Hats"],
        "bass": ["Analog_Bass", "FM_Bass", "Wobble_Bass"],
        "leads": ["Acid_Lead", "Distorted_Lead", "Industrial_Lead"],
        "pads": ["Dark_Pad", "Atmospheric_Pad"]
    },
    "house": {
        "drums": ["House_Kit", "Classic_909", "Deep_Kick"],
        "bass": ["House_Bass", "Deep_Bass", "Funky_Bass"],
        "leads": ["Piano_Lead", "Vocal_Lead", "Disco_Lead"],
        "pads": ["Warm_Pad", "String_Pad"]
    },
    "trance": {
        "drums": ["Trance_Kit", "Uplifting_Kick", "Gated_Hats"],
        "bass": ["Trance_Bass", "Rolling_Bass", "Sub_Bass"],
        "leads": ["Trance_Lead", "Supersaw_Lead", "Arpeggiated_Lead"],
        "pads": ["Epic_Pad", "Sweeping_Pad"]
    }
}

def get_instruments_by_category(category: str = None):
    """Get instruments filtered by category."""
    if category:
        return INSTRUMENTS_DB.get(category, {})
    return INSTRUMENTS_DB

def get_instruments_by_genre(genre: str):
    """Get recommended instruments for a specific genre."""
    return GENRE_INSTRUMENTS.get(genre.lower(), {})

def search_instruments(search_term: str):
    """Search instruments by name or description."""
    results = {}
    for category, instruments in INSTRUMENTS_DB.items():
        category_results = {}
        for name, info in instruments.items():
            if (search_term.lower() in name.lower() or 
                search_term.lower() in info.get("description", "").lower()):
                category_results[name] = info
        if category_results:
            results[category] = category_results
    return results