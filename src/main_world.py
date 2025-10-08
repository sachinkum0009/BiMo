"""
Main script for running the Isaac Sim robot simulation with modular class structure.
"""

import argparse
import sys
from pathlib import Path
import numpy as np

from isaacsim import SimulationApp
CONFIG = {
    "width": 1280,
    "height": 720,
    "window_width": 1920,
    "window_height": 1080,
    "headless": True,
    "hide_ui": False,  # Show the GUI
    "renderer": "RaytracedLighting",
    "display_options": 3286,  # Set display options to show default grid
}
# Initialize simulation app first
simulation_app = SimulationApp(launch_config=CONFIG)

from isaacsim.core.utils.extensions import enable_extension
simulation_app.set_setting("/app/window/drawMouse", True)

# Enable Livestream extension
enable_extension("omni.services.livestream.nvcf")

# Ensure project `src` is searched before system/site packages so local modules
# named like common libraries (e.g. `utils`) are resolved first.
sys.path.insert(0, "/home/asus/backup/zzzzz/isaac/BiMo/src")
# Import our modular classes from the local package
from simulation_world import SimulationWorld
# from utils import Position

geforce3080_usd_path = Path("/home/asus/backup/zzzzz/isaac/revel_hackathon/revel_files/geforce3080/geforce3080.usd")
chess_usd_path = Path("/home/asus/backup/zzzzz/isaac/revel_hackathon/revel_files/chess/chess.usd")
stanley_stand_usd_path = Path("/home/asus/backup/zzzzz/isaac/revel_hackathon/revel_files/stanley_stand/stanley_stand.usd")

def main():
    """Main function to set up and run the simulation."""
    # Parse arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument("usd_path", type=Path)
    # args = parser.parse_args()
    
    # usd_path: Path = args.usd_path.resolve()
    # assert usd_path.exists(), f"USD file not found: {usd_path}"

    # print(f"Loading USD from: {usd_path}")
    
    # Create simulation world
    sim_world = SimulationWorld()

    # add cube
    sim_world.add_cube(
        name="cube1",
        position=np.array([2.0, 0.0, 0.5]),
        size=np.array([1.0, 1.0, 1.0]),
        color=np.array([0.0, 1.0, 0.0])
    )
    
    # Add two robots with different positions and orientations
    # robot1 = sim_world.add_robot(
    #     name="robot1",
    #     usd_path=usd_path,
    #     position=np.array([1.0, 0.0, 0.0]),
    #     orientation=np.array([0.7071, 0.0, 0.0, 0.7071]),  # No rotation
    #     phase_offset=0.0
    # )
    
    
    # Initialize and run simulation
    sim_world.initialize_simulation()
    sim_world.run_simulation()


if __name__ == "__main__":
    main()
