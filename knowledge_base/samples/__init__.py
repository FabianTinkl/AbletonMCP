"""
Samples Knowledge Base

This module contains comprehensive information about sample libraries,
one-shots, loops, and audio content for music production.
"""

from .drums import DRUM_SAMPLES
from .bass import BASS_SAMPLES
from .melodic import MELODIC_SAMPLES
from .percussion import PERCUSSION_SAMPLES
from .vocals import VOCAL_SAMPLES
from .fx import FX_SAMPLES
from .loops import LOOP_SAMPLES
from .genres import GENRE_SAMPLE_PACKS

# Master samples database
SAMPLES_DB = {
    "drums": DRUM_SAMPLES,
    "bass": BASS_SAMPLES,
    "melodic": MELODIC_SAMPLES,
    "percussion": PERCUSSION_SAMPLES,
    "vocals": VOCAL_SAMPLES,
    "fx": FX_SAMPLES,
    "loops": LOOP_SAMPLES
}

# Genre-specific sample recommendations
GENRE_SAMPLES = {
    "techno": {
        "kicks": ["909_Kick", "808_Kick", "Industrial_Kick", "Sub_Kick"],
        "hats": ["909_Hat", "Industrial_Hat", "Metallic_Hat", "Filtered_Hat"],
        "snares": ["Industrial_Snare", "909_Snare", "Clap", "Rim_Shot"],
        "bass": ["Acid_Bass", "Sub_Bass", "Distorted_Bass", "FM_Bass"],
        "percussion": ["Industrial_Perc", "Metallic_Perc", "Noise_Perc", "Tribal_Perc"],
        "fx": ["Noise_Sweep", "Industrial_Riser", "Reverb_Tail", "Distorted_Hit"]
    },
    "house": {
        "kicks": ["House_Kick", "Deep_Kick", "Classic_Kick", "Punchy_Kick"],
        "hats": ["House_Hat", "Swing_Hat", "Open_Hat", "Closed_Hat"],
        "snares": ["House_Snare", "Clap", "Snap", "Rim"],
        "bass": ["House_Bass", "Deep_Bass", "Sub_Bass", "Slap_Bass"],
        "percussion": ["Shaker", "Conga", "Bongo", "Tambourine"],
        "vocals": ["Vocal_Chop", "Vocal_Stab", "Vocal_Phrase", "Vocal_Ad_Lib"]
    },
    "minimal": {
        "kicks": ["Minimal_Kick", "Dry_Kick", "Filtered_Kick", "Sub_Kick"],
        "hats": ["Minimal_Hat", "Tick", "Click", "Short_Hat"],
        "percussion": ["Minimal_Perc", "Click", "Tick", "Short_Hit"],
        "bass": ["Minimal_Bass", "Sub_Bass", "Filtered_Bass", "Short_Bass"],
        "fx": ["Minimal_FX", "Click", "Pop", "Short_Noise"]
    },
    "industrial": {
        "drums": ["Industrial_Kit", "Metal_Drums", "Distorted_Drums", "Noise_Drums"],
        "percussion": ["Metal_Hit", "Pipe_Hit", "Chain_Rattle", "Machinery"],
        "bass": ["Industrial_Bass", "Distorted_Bass", "Noise_Bass", "Metal_Bass"],
        "fx": ["Machine_Noise", "Metal_Scrape", "Factory_Ambient", "Industrial_Riser"]
    }
}

def get_samples_by_category(category: str = None):
    """Get samples filtered by category."""
    if category:
        return SAMPLES_DB.get(category, {})
    return SAMPLES_DB

def get_samples_by_genre(genre: str):
    """Get recommended samples for a specific genre."""
    return GENRE_SAMPLES.get(genre.lower(), {})

def search_samples(search_term: str):
    """Search samples by name, description, or tags."""
    results = {}
    for category, samples in SAMPLES_DB.items():
        category_results = {}
        for name, info in samples.items():
            if (search_term.lower() in name.lower() or 
                search_term.lower() in info.get("description", "").lower() or
                any(search_term.lower() in tag.lower() for tag in info.get("tags", []))):
                category_results[name] = info
        if category_results:
            results[category] = category_results
    return results

def get_sample_pack_by_genre(genre: str):
    """Get sample packs recommended for a specific genre."""
    return GENRE_SAMPLE_PACKS.get(genre.lower(), [])