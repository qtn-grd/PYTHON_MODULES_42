"""Alchemy package - Sacred Scroll
Controls which elemental functions are exposed at the package level.
"""

__version__ = "1.O.O"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water

__all__ = ["create_fire", "create_water"]
