#!/usr/bin/env python3

"""Convert a phrase to its acronym"""

import re


def abbreviate(words: str) -> str:
    """Convert a phrase to its acronym"""
    return ''.join(word[0] for word in re.split('\W+', words)).upper()
