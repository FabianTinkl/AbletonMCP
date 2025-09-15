"""
Genre Sample Packs Knowledge Base

Comprehensive database of sample packs organized by genre with
detailed descriptions and usage recommendations.
"""

GENRE_SAMPLE_PACKS = {
    "techno": [
        {
            "name": "Underground Techno Essentials",
            "description": "Raw, underground techno samples with industrial character",
            "contents": ["kicks", "hats", "snares", "bass", "leads", "fx"],
            "bpm_range": [128, 135],
            "style": "underground",
            "tags": ["industrial", "raw", "analog", "dark"]
        },
        {
            "name": "Peak Time Techno",
            "description": "High-energy samples for peak-time dancefloor moments",
            "contents": ["kicks", "hats", "snares", "bass", "risers", "impacts"],
            "bpm_range": [130, 140],
            "style": "peak_time",
            "tags": ["energy", "aggressive", "loud", "crowd_pleasing"]
        },
        {
            "name": "Minimal Techno Toolkit",
            "description": "Subtle, precise samples for minimal techno production",
            "contents": ["kicks", "minimal_perc", "clicks", "sub_bass", "textures"],
            "bpm_range": [125, 132],
            "style": "minimal",
            "tags": ["subtle", "precise", "clean", "micro"]
        },
        {
            "name": "Acid Techno Collection",
            "description": "Classic acid sounds with TB-303 character",
            "contents": ["acid_bass", "acid_leads", "909_drums", "fx"],
            "bpm_range": [128, 135],
            "style": "acid",
            "tags": ["303", "acid", "resonant", "classic"]
        }
    ],
    
    "house": [
        {
            "name": "Classic House Foundations",
            "description": "Timeless house samples with vintage character",
            "contents": ["house_kicks", "hats", "claps", "bass", "piano", "vocals"],
            "bpm_range": [120, 128],
            "style": "classic",
            "tags": ["vintage", "warm", "groove", "soulful"]
        },
        {
            "name": "Deep House Essentials",
            "description": "Warm, deep house sounds with jazz influences",
            "contents": ["deep_kicks", "smooth_bass", "jazz_chords", "vocal_chops", "pads"],
            "bpm_range": [118, 125],
            "style": "deep",
            "tags": ["warm", "jazz", "smooth", "emotional"]
        },
        {
            "name": "Tech House Weapons",
            "description": "Modern tech house with underground edge",
            "contents": ["tech_kicks", "rolling_bass", "minimal_perc", "vocal_stabs", "fx"],
            "bpm_range": [124, 130],
            "style": "tech",
            "tags": ["modern", "underground", "rolling", "groove"]
        }
    ],
    
    "industrial": [
        {
            "name": "Industrial Warfare",
            "description": "Harsh, metallic sounds for industrial music",
            "contents": ["metal_drums", "industrial_bass", "noise_fx", "machinery", "distorted_vocals"],
            "bpm_range": [120, 140],
            "style": "harsh",
            "tags": ["metal", "harsh", "aggressive", "noise"]
        },
        {
            "name": "Factory Floor",
            "description": "Mechanical sounds and rhythms",
            "contents": ["machine_drums", "factory_perc", "steam_fx", "motor_bass"],
            "bpm_range": [115, 135],
            "style": "mechanical",
            "tags": ["mechanical", "rhythmic", "factory", "steam"]
        }
    ],
    
    "minimal": [
        {
            "name": "Micro Elements",
            "description": "Tiny, precise sounds for microhouse and minimal",
            "contents": ["micro_kicks", "clicks", "pops", "minimal_bass", "space"],
            "bpm_range": [125, 130],
            "style": "micro",
            "tags": ["tiny", "precise", "space", "minimal"]
        },
        {
            "name": "Deep Minimal",
            "description": "Deeper minimal sounds with subtle warmth",
            "contents": ["warm_kicks", "subtle_perc", "deep_bass", "textures"],
            "bpm_range": [122, 128],
            "style": "deep_minimal",
            "tags": ["warm", "subtle", "deep", "textural"]
        }
    ],
    
    "experimental": [
        {
            "name": "Sound Design Lab",
            "description": "Abstract sounds for experimental electronic music",
            "contents": ["abstract_percussion", "noise_textures", "granular_fx", "modular_sequences"],
            "bpm_range": [80, 160],
            "style": "abstract",
            "tags": ["abstract", "experimental", "modular", "granular"]
        },
        {
            "name": "Glitch Toolkit",
            "description": "Digital artifacts and glitch effects",
            "contents": ["glitch_drums", "bit_crushed", "stutters", "digital_noise"],
            "bpm_range": [100, 150],
            "style": "glitch",
            "tags": ["digital", "glitch", "artifacts", "stutter"]
        }
    ],
    
    "ambient": [
        {
            "name": "Atmospheric Textures",
            "description": "Evolving pads and atmospheric sounds",
            "contents": ["ambient_pads", "field_recordings", "drones", "textures", "reverb_tails"],
            "bpm_range": [60, 120],
            "style": "atmospheric",
            "tags": ["evolving", "atmospheric", "natural", "spacious"]
        },
        {
            "name": "Dark Ambient",
            "description": "Ominous and mysterious ambient sounds",
            "contents": ["dark_drones", "disturbing_textures", "industrial_ambience", "horror_fx"],
            "bpm_range": [50, 100],
            "style": "dark",
            "tags": ["dark", "ominous", "mysterious", "disturbing"]
        }
    ]
}