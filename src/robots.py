"""
Robot class for managing robot entities in the simulation.
"""

from enum import Enum
from dataclasses import dataclass
from pathlib import Path

from isaacsim.storage.native import get_assets_root_path

from my_utils import get_omniverse_content_url

ASSETS_ROOT = get_assets_root_path()
OMNIVERSE_CONTENT_URL = get_omniverse_content_url()


class ManipulatorRobot:
    """Enum for predefined manipulator USD file paths."""

    FRANKA = Path(f"{ASSETS_ROOT}/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd")
    FRANKA_ROS2 = Path("/home/asus/backup/zzzzz/isaac/native/Files/franka_ros2.usd")
    ROBOT2 = Path(f"{ASSETS_ROOT}/Isaac/Robots/Robot2/robot2.usd")
    ROBOT3 = Path(f"{ASSETS_ROOT}/Isaac/Robots/Robot3/robot3.usd")


class MobileRobot:
    """Enum for predefined mobile robot USD file paths."""

    NOVA_CARTER = Path(f"{ASSETS_ROOT}/Isaac/Samples/ROS2/Robots/Nova_Carter_ROS.usd")
    TURTLEBOT3 = Path(
        f"{ASSETS_ROOT}/Isaac/Samples/ROS2/Robots/turtlebot3_burger_ROS.usd"
    )
    ROBOT2 = Path(f"{ASSETS_ROOT}/Isaac/Robots/MobileRobot2/mobile_robot2.usd")
    ROBOT3 = Path(f"{ASSETS_ROOT}/Isaac/Robots/MobileRobot3/mobile_robot3.usd")


class LeggedRobot:
    """Enum for predefined legged robot USD file paths."""

    H1 = Path(
        f"{OMNIVERSE_CONTENT_URL}/Assets/Isaac/5.0/Isaac/Robots/Unitree/H1/h1.usd"
    )
    GO2 = Path(
        f"{OMNIVERSE_CONTENT_URL}/Assets/Isaac/5.0/Isaac/Robots/Unitree/Go2/go2.usd"
    )


class Robot:
    """Enum for predefined robot USD file paths."""

    MANIPULATOR_ROBOT = ManipulatorRobot
    MOBILE_ROBOT = MobileRobot
    LEGGED_ROBOT = LeggedRobot
