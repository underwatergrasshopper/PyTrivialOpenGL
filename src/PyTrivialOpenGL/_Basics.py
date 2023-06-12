"""
Base functionality and support for PyTrivialOpenGL submodules.
"""

__all__ = [
    "clamp",
]

def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)