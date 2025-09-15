"""
Samplers Knowledge Base

Comprehensive database of sampler instruments and sampling techniques.
"""

SAMPLERS = {
    "Simpler": {
        "description": "Basic sampler for single samples",
        "category": "sampler",
        "genres": ["all"],
        "presets": {
            "drums": ["One Shot", "Drum Hit", "Percussion", "Impact"],
            "melodic": ["Pitched Sample", "Melodic Loop", "Harmonic", "Tonal"],
            "textural": ["Texture", "Atmosphere", "Background", "Ambience"],
            "vocal": ["Vocal Chop", "Voice", "Spoken", "Sung"]
        },
        "key_parameters": {
            "Start": {"min": 0, "max": 127, "default": 0},
            "Length": {"min": 0, "max": 127, "default": 127},
            "Transpose": {"min": -48, "max": 48, "default": 0},
            "Fine Tune": {"min": -50, "max": 50, "default": 0},
            "Gain": {"min": 0, "max": 127, "default": 100}
        },
        "sample_formats": ["wav", "aiff", "mp3", "flac"],
        "device_path": "Live/Simpler"
    },

    "Sampler": {
        "description": "Advanced multisampling instrument",
        "category": "sampler",
        "genres": ["all"],
        "presets": {
            "multisamples": ["Piano Multisample", "String Section", "Brass Section"],
            "drums": ["Drum Kit", "Percussion Kit", "Electronic Kit"],
            "creative": ["Granular", "Stretched", "Reversed", "Chopped"],
            "realistic": ["Acoustic Guitar", "Electric Guitar", "Bass Guitar"]
        },
        "key_parameters": {
            "Zone Start": {"min": 0, "max": 127, "default": 0},
            "Zone End": {"min": 0, "max": 127, "default": 127},
            "Root Key": {"min": 0, "max": 127, "default": 60},
            "Transpose": {"min": -48, "max": 48, "default": 0},
            "Filter Cutoff": {"min": 0, "max": 127, "default": 127}
        },
        "sample_formats": ["wav", "aiff", "rex", "mp3", "flac"],
        "device_path": "Live/Sampler"
    },

    "Granular_Sampler": {
        "description": "Granular synthesis sampler for textural sounds",
        "category": "sampler",
        "genres": ["ambient", "experimental", "techno", "minimal"],
        "presets": {
            "textural": ["Granular Texture", "Evolving Grain", "Atmospheric"],
            "rhythmic": ["Granular Rhythm", "Stuttered", "Chopped"],
            "melodic": ["Granular Melody", "Pitched Grains", "Harmonic"],
            "experimental": ["Random Grains", "Chaos", "Unpredictable"]
        },
        "key_parameters": {
            "Grain Size": {"min": 1, "max": 1000, "default": 100},
            "Grain Rate": {"min": 1, "max": 100, "default": 20},
            "Position": {"min": 0, "max": 127, "default": 0},
            "Spray": {"min": 0, "max": 127, "default": 0},
            "Pitch": {"min": -48, "max": 48, "default": 0}
        },
        "sample_formats": ["wav", "aiff"],
        "device_path": "Live/Granular Sampler"
    },

    "Rex_Player": {
        "description": "REX loop player with slice manipulation",
        "category": "sampler",
        "genres": ["drum_and_bass", "breakbeat", "jungle", "hip_hop"],
        "presets": {
            "breakbeats": ["Amen Break", "Apache", "Think Break", "Funky Drummer"],
            "electronic": ["Electronic Loop", "Techno Loop", "House Loop"],
            "percussion": ["Percussion Loop", "Conga Loop", "Tribal Loop"],
            "melodic": ["Melodic Loop", "Bass Loop", "Chord Loop"]
        },
        "key_parameters": {
            "Slice": {"min": 0, "max": 127, "default": 0},
            "Pitch": {"min": -48, "max": 48, "default": 0},
            "Filter": {"min": 0, "max": 127, "default": 127},
            "Decay": {"min": 0, "max": 127, "default": 64}
        },
        "sample_formats": ["rex", "rx2"],
        "device_path": "Live/Rex Player"
    }
}

# Sampling techniques by genre
SAMPLING_TECHNIQUES = {
    "hip_hop": {
        "techniques": ["chopping", "time_stretching", "pitch_shifting", "reverse"],
        "typical_sources": ["vinyl records", "soul", "jazz", "funk"],
        "effects": ["low_pass_filter", "compression", "saturation"],
        "characteristics": ["vinyl warmth", "chopped vocals", "drum breaks"]
    },
    "drum_and_bass": {
        "techniques": ["time_stretching", "granular", "slice_editing", "reverse"],
        "typical_sources": ["breakbeats", "jazz", "soul", "jungle"],
        "effects": ["distortion", "filters", "reverb", "delay"],
        "characteristics": ["complex rhythms", "bass emphasis", "chopped breaks"]
    },
    "ambient": {
        "techniques": ["granular", "time_stretching", "reverse", "layering"],
        "typical_sources": ["field_recordings", "acoustic", "nature", "voices"],
        "effects": ["reverb", "delay", "modulation", "filters"],
        "characteristics": ["atmospheric", "evolving", "textural", "spacious"]
    },
    "techno": {
        "techniques": ["time_stretching", "pitch_shifting", "granular", "chopping"],
        "typical_sources": ["industrial", "electronic", "percussion", "vocals"],
        "effects": ["distortion", "filters", "delay", "compression"],
        "characteristics": ["industrial", "repetitive", "driving", "processed"]
    }
}

# Sample library organization
SAMPLE_CATEGORIES = {
    "drums": {
        "subcategories": ["kicks", "snares", "hats", "cymbals", "percussion", "fx"],
        "formats": ["one_shots", "loops", "rex_files"],
        "characteristics": ["punch", "character", "genre_specific"]
    },
    "bass": {
        "subcategories": ["sub_bass", "synth_bass", "acoustic_bass", "processed"],
        "formats": ["one_shots", "loops", "multisamples"],
        "characteristics": ["weight", "character", "harmonic_content"]
    },
    "melodic": {
        "subcategories": ["leads", "pads", "arps", "chords", "stabs"],
        "formats": ["one_shots", "loops", "multisamples"],
        "characteristics": ["musicality", "harmonic_content", "expression"]
    },
    "vocals": {
        "subcategories": ["leads", "chops", "phrases", "fx", "spoken"],
        "formats": ["one_shots", "loops", "phrases"],
        "characteristics": ["emotion", "character", "language"]
    },
    "fx": {
        "subcategories": ["impacts", "sweeps", "atmospheres", "noise", "glitch"],
        "formats": ["one_shots", "loops", "textures"],
        "characteristics": ["impact", "movement", "texture"]
    }
}

def get_sampler_by_technique(technique: str):
    """Get recommended sampler based on technique."""
    technique_mapping = {
        "granular": ["Granular_Sampler"],
        "multisampling": ["Sampler"],
        "simple": ["Simpler"],
        "loop_slicing": ["Rex_Player"],
        "basic": ["Simpler"]
    }
    return technique_mapping.get(technique.lower(), list(SAMPLERS.keys()))

def get_sampling_techniques_by_genre(genre: str):
    """Get sampling techniques used in a specific genre."""
    return SAMPLING_TECHNIQUES.get(genre.lower(), {})

def get_sample_categories():
    """Get sample library organization structure."""
    return SAMPLE_CATEGORIES