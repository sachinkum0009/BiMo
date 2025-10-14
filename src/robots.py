"""
Robot class for managing robot entities in the simulation.
"""

from enum import Enum
from dataclasses import dataclass
from pathlib import Path

from isaacsim.storage.native import get_assets_root_path

ASSETS_ROOT = get_assets_root_path()

class ManipulatorRobot:
    """Enum for predefined manipulator USD file paths."""
    FRANKA = Path(f"{ASSETS_ROOT}/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd")
    FRANKA_ROS2 = Path("/home/asus/backup/zzzzz/isaac/native/Files/franka_ros2.usd")
    ROBOT2 = Path(f"{ASSETS_ROOT}/Isaac/Robots/Robot2/robot2.usd")
    ROBOT3 = Path(f"{ASSETS_ROOT}/Isaac/Robots/Robot3/robot3.usd")

class MobileRobot:
    """Enum for predefined mobile robot USD file paths."""
    NOVA_CARTER = Path(f"{ASSETS_ROOT}/Isaac/Robots/NVIDIA/NovaCarter/nova_carter.usd")
    ROBOT2 = Path(f"{ASSETS_ROOT}/Isaac/Robots/MobileRobot2/mobile_robot2.usd")
    ROBOT3 = Path(f"{ASSETS_ROOT}/Isaac/Robots/MobileRobot3/mobile_robot3.usd")

class Robot:
    """Enum for predefined robot USD file paths."""
    MANIPULATOR_ROBOT = ManipulatorRobot
    MOBILE_ROBOT = MobileRobot