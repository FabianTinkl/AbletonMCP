"""
Effects Knowledge Base

This module contains comprehensive information about Ableton Live Suite effects,
including categorization, presets, parameters, and genre-specific usage patterns.
"""

from .dynamics import DYNAMICS_EFFECTS
from .eq import EQ_EFFECTS
from .filters import FILTER_EFFECTS
from .reverb import REVERB_EFFECTS
from .delay import DELAY_EFFECTS
from .modulation import MODULATION_EFFECTS
from .distortion import DISTORTION_EFFECTS
from .utility import UTILITY_EFFECTS

# Master effects database
EFFECTS_DB = {
    "dynamics": DYNAMICS_EFFECTS,
    "eq": EQ_EFFECTS,
    "filters": FILTER_EFFECTS,
    "reverb": REVERB_EFFECTS,
    "delay": DELAY_EFFECTS,
    "modulation": MODULATION_EFFECTS,
    "distortion": DISTORTION_EFFECTS,
    "utility": UTILITY_EFFECTS
}

# Effect chains by genre
GENRE_EFFECT_CHAINS = {
    "techno": {
        "drums": ["EQ", "Compressor", "Saturator", "Filter"],
        "bass": ["EQ", "Compressor", "Saturator", "Utility"],
        "leads": ["EQ", "Distortion", "Delay", "Reverb"],
        "master": ["EQ", "Multiband Compressor", "Limiter"]
    },
    "house": {
        "drums": ["EQ", "Compressor", "Saturator"],
        "bass": ["EQ", "Compressor", "Chorus"],
        "keys": ["EQ", "Chorus", "Reverb"],
        "master": ["EQ", "Compressor", "Limiter"]
    },
    "trance": {
        "leads": ["EQ", "Chorus", "Delay", "Reverb"],
        "pads": ["EQ", "Chorus", "Reverb"],
        "bass": ["EQ", "Compressor", "Phaser"],
        "master": ["EQ", "Multiband Compressor", "Limiter"]
    }
}

def get_effects_by_category(category: str = None):
    """Get effects filtered by category."""
    if category:
        return EFFECTS_DB.get(category, {})
    return EFFECTS_DB

def get_effect_chain_by_genre(genre: str, track_type: str = None):
    """Get recommended effect chain for genre and track type."""
    genre_chains = GENRE_EFFECT_CHAINS.get(genre.lower(), {})
    if track_type:
        return genre_chains.get(track_type, [])
    return genre_chains

def search_effects(search_term: str):
    """Search effects by name or description."""
    results = {}
    for category, effects in EFFECTS_DB.items():
        category_results = {}
        for name, info in effects.items():
            if (search_term.lower() in name.lower() or 
                search_term.lower() in info.get("description", "").lower()):
                category_results[name] = info
        if category_results:
            results[category] = category_results
    return results