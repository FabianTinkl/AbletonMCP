"""
Lead Instruments Knowledge Base

Comprehensive database of lead instruments for melody and hook elements.
"""

LEADS = {
    "Acid_Lead": {
        "description": "Classic acid lead with filter modulation",
        "category": "leads",
        "genres": ["techno", "acid", "minimal", "trance"],
        "presets": {
            "classic": ["TB-303", "Classic Acid", "Vintage Acid", "Original"],
            "modern": ["Modern Acid", "Digital Acid", "Clean Acid", "Refined"],
            "aggressive": ["Hard Acid", "Distorted Acid", "Industrial Acid", "Heavy"],
            "subtle": ["Soft Acid", "Gentle Acid", "Smooth Acid", "Mellow"]
        },
        "key_parameters": {
            "Filter Cutoff": {"min": 0, "max": 127, "default": 64},
            "Filter Resonance": {"min": 0, "max": 127, "default": 80},
            "Accent": {"min": 0, "max": 127, "default": 50},
            "Decay": {"min": 0, "max": 127, "default": 32},
            "Overdrive": {"min": 0, "max": 127, "default": 16}
        },
        "frequency_range": (200, 2000),
        "device_path": "Live/Leads/Acid Lead"
    },

    "Supersaw_Lead": {
        "description": "Powerful supersaw lead for trance and big room",
        "category": "leads",
        "genres": ["trance", "progressive", "big_room", "techno"],
        "presets": {
            "uplifting": ["Uplifting Saw", "Emotional Saw", "Epic Saw", "Soaring"],
            "dark": ["Dark Saw", "Industrial Saw", "Aggressive Saw", "Heavy"],
            "pluck": ["Saw Pluck", "Punchy Saw", "Sharp Pluck", "Rhythmic"],
            "evolving": ["Evolving Saw", "Moving Saw", "Morphing", "Breathing"]
        },
        "key_parameters": {
            "Detune": {"min": 0, "max": 127, "default": 32},
            "Voices": {"min": 1, "max": 7, "default": 7},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 100},
            "Filter Resonance": {"min": 0, "max": 127, "default": 16},
            "Attack": {"min": 0, "max": 127, "default": 0}
        },
        "frequency_range": (300, 4000),
        "device_path": "Live/Leads/Supersaw Lead"
    },

    "Pluck_Lead": {
        "description": "Percussive pluck lead with sharp attack",
        "category": "leads",
        "genres": ["progressive", "trance", "house", "minimal"],
        "presets": {
            "classic": ["Classic Pluck", "Vintage Pluck", "Analog Pluck", "Retro"],
            "digital": ["Digital Pluck", "Modern Pluck", "Sharp Pluck", "Clean"],
            "filtered": ["Filtered Pluck", "Swept Pluck", "Moving Pluck", "Dynamic"],
            "ambient": ["Soft Pluck", "Gentle Pluck", "Atmospheric", "Floating"]
        },
        "key_parameters": {
            "Attack": {"min": 0, "max": 127, "default": 0},
            "Decay": {"min": 0, "max": 127, "default": 48},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 80},
            "Filter Envelope": {"min": 0, "max": 127, "default": 32},
            "Reverb": {"min": 0, "max": 127, "default": 16}
        },
        "frequency_range": (400, 3000),
        "device_path": "Live/Leads/Pluck Lead"
    },

    "Arp_Lead": {
        "description": "Arpeggiated lead for rhythmic melodies",
        "category": "leads",
        "genres": ["trance", "progressive", "synthwave", "techno"],
        "presets": {
            "classic": ["Classic Arp", "Vintage Arp", "Retro Arp", "80s Arp"],
            "modern": ["Modern Arp", "Digital Arp", "Clean Arp", "Refined"],
            "gated": ["Gated Arp", "Rhythmic Arp", "Choppy Arp", "Stuttered"],
            "flowing": ["Flowing Arp", "Smooth Arp", "Legato Arp", "Connected"]
        },
        "key_parameters": {
            "Arp Rate": {"min": 0, "max": 127, "default": 64},
            "Arp Range": {"min": 1, "max": 4, "default": 2},
            "Gate Time": {"min": 0, "max": 127, "default": 80},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 100},
            "LFO Rate": {"min": 0, "max": 127, "default": 32}
        },
        "frequency_range": (500, 5000),
        "device_path": "Live/Leads/Arp Lead"
    }
}

# Lead usage patterns by genre
LEAD_USAGE = {
    "techno": {
        "role": "main hook, breakdown elements, build-ups",
        "playing_style": "repetitive patterns, filter sweeps",
        "effects": ["distortion", "delay", "reverb", "filters"],
        "frequency_placement": "cut through mix, avoid bass clash",
        "characteristics": ["hypnotic", "driving", "industrial", "repetitive"]
    },
    "trance": {
        "role": "main melody, emotional peaks, breakdowns",
        "playing_style": "melodic phrases, builds and releases",
        "effects": ["reverb", "delay", "chorus", "filters"],
        "frequency_placement": "prominent in mix, wide stereo",
        "characteristics": ["emotional", "uplifting", "melodic", "soaring"]
    },
    "house": {
        "role": "melodic hooks, vocal support, breaks",
        "playing_style": "musical phrases, chord following",
        "effects": ["reverb", "delay", "chorus"],
        "frequency_placement": "supportive, not overpowering",
        "characteristics": ["musical", "soulful", "groovy", "supportive"]
    },
    "minimal": {
        "role": "subtle melodic elements, texture",
        "playing_style": "sparse, evolving, filtered",
        "effects": ["subtle reverb", "filters", "modulation"],
        "frequency_placement": "blended in mix, not dominant",
        "characteristics": ["subtle", "evolving", "textural", "atmospheric"]
    }
}

# Lead recommendations by energy level
LEAD_ENERGY_MAPPING = {
    "low": ["Pluck_Lead", "Arp_Lead"],
    "medium": ["Acid_Lead", "Pluck_Lead"],
    "high": ["Supersaw_Lead", "Acid_Lead"],
    "extreme": ["Supersaw_Lead"]
}

def get_leads_by_energy(energy_level: str):
    """Get lead recommendations based on energy level."""
    return LEAD_ENERGY_MAPPING.get(energy_level.lower(), list(LEADS.keys()))

def get_leads_by_genre(genre: str):
    """Get lead recommendations for a specific genre."""
    return {name: info for name, info in LEADS.items()
            if genre.lower() in info["genres"]}

def get_lead_usage_info(genre: str):
    """Get information about how leads are used in a specific genre."""
    return LEAD_USAGE.get(genre.lower(), {})