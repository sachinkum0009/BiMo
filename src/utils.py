#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility functions for data processing and analysis.
"""

from dataclasses import dataclass
from enum import Enum
import numpy as np
 

class Color(Enum):
    # Use simple tuples as Enum values to avoid ambiguous truth-value
    # behavior when NumPy arrays are used as Enum members.
    RED = (1.0, 0.0, 0.0)
    GREEN = (0.0, 1.0, 0.0)
    BLUE = (0.0, 0.0, 1.0)

    def as_array(self) -> np.ndarray:
        """Return the color as a numpy array (float dtype)."""
        return np.array(self.value, dtype=float)

@dataclass
class Position:
    x: float
    y: float
    z: float

    def to_numpy(self) -> np.ndarray:
        """Return the position as a numpy array of shape (3,)."""
        return np.array([self.x, self.y, self.z], dtype=float)

    # Allow direct conversion via np.array(Position(...))
    def __array__(self, dtype=None):
        arr = self.to_numpy()
        if dtype is not None:
            return arr.astype(dtype)
        return arr

    def __iter__(self):
        # Support unpacking and iteration
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self) -> str:
        return f"Position(x={self.x!r}, y={self.y!r}, z={self.z!r})"



def preprocess_data(data):
    # Implement data preprocessing steps
    pass


def analyze_data(data):
    # Implement data analysis steps
    pass
