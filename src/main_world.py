"""
Main script for running the Isaac Sim robot simulation with modular class structure.
"""

import sys
from pathlib import Path
import numpy as np

from isaacsim import SimulationApp

from config import CONFIG_WEBRTC

# Initialize simulation app first
simulation_app = SimulationApp(launch_config=CONFIG_WEBRTC)

from isaacsim.core.utils.extensions import enable_extension

simulation_app.set_setting("/app/window/drawMouse", True)

# Enable Livestream extension
enable_extension("omni.services.livestream.nvcf")

# enable ROS2 bridge extension
enable_extension("isaacsim.ros2.bridge")

# Ensure project `src` is searched before system/site packages so local modules
# named like common libraries (e.g. `utils`) are resolved first.
# sys.path.insert(0, "/home/asus/backup/zzzzz/isaac/BiMo/src")
# Import our modular classes from the local package
from simulation_world import SimulationWorld
from my_utils import Position, Orientation, Color
from robots import Robot
from environments import Environment


def main():
    """Main function to set up and run the simulation."""

    # world_usd_path = Path("/home/asus/backup/zzzzz/isaac/revel_hackathon/turtlebot3_ros.usd")
    world_usd_path = Environment.OUTDOOR.GREENHOUSE
    # Create simulation world
    sim_world = SimulationWorld(load_ground_plane=True, world_usd_path=world_usd_path)

    # add cube
    # sim_world.add_cube(
    #     name="cube1",
    #     position=Position(2.0, 0.0, 0.5).to_numpy(),
    #     size=np.array([0.5, 0.5, 0.5]),
    #     color=Color.GREEN.as_array(),
    # )

    # sim_world.add_cube(
    #     name="cube2",
    #     position=Position(0.0, 0.0, 0.25).to_numpy(),
    #     size=np.array([0.5, 0.5, 0.5]),
    #     color=Color.BLUE.as_array(),
    # )

    # Add two robots with different positions and orientations
    # robot1 = sim_world.add_robot(
    #     name="robot1",
    #     usd_path=usd_path,
    #     position=np.array([1.0, 0.0, 0.0]),
    #     orientation=np.array([0.7071, 0.0, 0.0, 0.7071]),  # No rotation
    #     phase_offset=0.0
    # )

    # franka = Robot.MANIPULATOR_ROBOT.FRANKA_ROS2

    # res = sim_world.add_robot(
    #     name="franka",
    #     usd_path=franka,
    #     position=Position(0.0, 0.0, 0.5).to_numpy(),
    #     orientation=Orientation.identity().to_numpy(),  # No rotation
    #     phase_offset=np.pi / 2,  # 90 degrees phase offset
    # )

    # if not res:
    #     print("Failed to add robot franka")
    #     return
    # evo_bot = Robot.MOBILE_ROBOT.EVOBOT
    # h1_robot = Robot.LEGGED_ROBOT.H1
    carter = Robot.MOBILE_ROBOT.NOVA_CARTER
    res = sim_world.add_robot(
        name="carter_robot",
        usd_path=carter,
        position=Position(1.0, 0.0, 0.0).to_numpy(),
        orientation=Orientation.from_quaternion(
            np.array([0.7071, 0.0, 0.0, 0.7071])
        ).to_numpy(),  # 90 degrees around x-axis
        phase_offset=0.0,
    )
    if not res:
        print("Failed to add robot carter_robot")
        return

    # Initialize and run simulation
    sim_world.initialize_simulation()
    sim_world.run_simulation()


if __name__ == "__main__":
    main()
