"""
Electronic Music Genre Knowledge Base

This module contains comprehensive information about electronic music genres,
including BPM ranges, chord progressions, typical instruments, drum patterns,
and production techniques for each genre.

Based on Beatport's genre categorization system.
"""

from .techno import *
from .house import *
from .trance import *
from .drum_and_bass import *
from .dubstep import *
from .ambient import *
from .breakbeat import *

# Master genre registry
GENRES = {
    'techno': 'techno',
    'house': 'house', 
    'deep_house': 'house',
    'tech_house': 'house',
    'trance': 'trance',
    'progressive_trance': 'trance',
    'drum_and_bass': 'drum_and_bass',
    'dubstep': 'dubstep',
    'ambient': 'ambient',
    'breakbeat': 'breakbeat',
    'big_beat': 'breakbeat'
}

# Cross-genre BPM reference
GENRE_BPM_RANGES = {
    'techno': (125, 150),
    'house': (120, 130),
    'deep_house': (118, 125),
    'tech_house': (120, 128),
    'trance': (128, 140),
    'progressive_trance': (130, 136),
    'drum_and_bass': (160, 180),
    'dubstep': (138, 142),
    'ambient': (60, 120),
    'breakbeat': (120, 140),
    'big_beat': (120, 140)
}