#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility functions for data processing and analysis.
"""

import os

from dataclasses import dataclass
from enum import Enum
import numpy as np

# from tf_transformations import quaternion_from_euler, euler_from_quaternion
from transforms3d.euler import euler2quat, quat2euler


class Color(Enum):
    # Use simple tuples as Enum values to avoid ambiguous truth-value
    # behavior when NumPy arrays are used as Enum members.
    RED = (1.0, 0.0, 0.0)
    GREEN = (0.0, 1.0, 0.0)
    BLUE = (0.0, 0.0, 1.0)
    ORANGE = (1.0, 0.647, 0.0)
    YELLOW = (1.0, 1.0, 0.0)
    PURPLE = (0.5, 0.0, 0.5)
    WHITE = (1.0, 1.0, 1.0)
    BLACK = (0.0, 0.0, 0.0)
    GRAY = (0.5, 0.5, 0.5)
    CYAN = (0.0, 1.0, 1.0)
    MAGENTA = (1.0, 0.0, 1.0)

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


@dataclass
class Orientation:
    """
    Orientation class that stores Euler angles in radians and provides quaternion output.

    Euler angles are in the order: roll (x), pitch (y), yaw (z) in radians.
    Quaternion output is in the format [w, x, y, z] (scalar-first).
    """

    roll: float  # Rotation around x-axis in radians
    pitch: float  # Rotation around y-axis in radians
    yaw: float  # Rotation around z-axis in radians

    def to_quaternion(self) -> np.ndarray:
        """
        Convert Euler angles to quaternion representation.

        Returns:
            np.ndarray: Quaternion in [w, x, y, z] format (scalar-first)
        """
        # tf_transformations.quaternion_from_euler returns [x, y, z, w] (scalar-last)
        quat = euler2quat(self.roll, self.pitch, self.yaw)
        # Convert to [w, x, y, z] format (scalar-first) as commonly used in robotics
        return np.array([quat[3], quat[0], quat[1], quat[2]], dtype=float)

    def to_numpy(self) -> np.ndarray:
        """Return the orientation as a quaternion numpy array."""
        return self.to_quaternion()

    # Allow direct conversion via np.array(Orientation(...))
    def __array__(self, dtype=None):
        arr = self.to_quaternion()
        if dtype is not None:
            return arr.astype(dtype)
        return arr

    def __iter__(self):
        # Support unpacking and iteration - returns quaternion components
        quat = self.to_quaternion()
        yield from quat

    def __repr__(self) -> str:
        return (
            f"Orientation(roll={self.roll!r}, pitch={self.pitch!r}, yaw={self.yaw!r})"
        )

    @classmethod
    def from_quaternion(cls, quaternion: np.ndarray) -> "Orientation":
        """
        Create an Orientation from a quaternion.

        Args:
            quaternion: Quaternion in [w, x, y, z] format (scalar-first)

        Returns:
            Orientation: New Orientation instance with Euler angles
        """
        # Convert from [w, x, y, z] to [x, y, z, w] for tf_transformations
        quat_tf = [quaternion[1], quaternion[2], quaternion[3], quaternion[0]]
        roll, pitch, yaw = quat2euler(quat_tf)
        return cls(roll=roll, pitch=pitch, yaw=yaw)

    @classmethod
    def identity(cls) -> "Orientation":
        """Create an identity orientation (no rotation)."""
        return cls(roll=0.0, pitch=0.0, yaw=0.0)


def preprocess_data(data):
    # Implement data preprocessing steps
    pass


def analyze_data(data):
    # Implement data analysis steps
    pass


def get_omniverse_content_url():
    return os.getenv(
        "OMNIVERSE_CONTENT_URL",
        "https://omniverse-content-production.s3-us-west-2.amazonaws.com",
    )
