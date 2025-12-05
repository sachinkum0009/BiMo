"""
SimulationWorld class for managing the overall simulation environment in Isaac Sim.
"""

from pathlib import Path
import numpy as np
from typing import Optional, List

from isaacsim.core.api import World
from isaacsim.core.api.objects import DynamicCuboid
from isaacsim.core.utils.stage import add_reference_to_stage

from robot import Robot
from camera_manager import CameraManager


class SimulationWorld:
    """Main class to manage the simulation world and coordinate all components."""

    def __init__(
        self, load_ground_plane: bool = True, world_usd_path: Optional[Path] = None
    ):
        """
        Initialize the simulation world.

        """
        self.world = World()
        self.robots: List[Robot] = []
        self.camera_manager: Optional[CameraManager] = None

        self._setup_world(load_ground_plane, world_usd_path)

    def _setup_world(
        self, load_ground_plane: bool = True, world_usd_path: Optional[Path] = None
    ):
        """Set up the basic world environment."""
        # Add default ground plane
        if load_ground_plane:
            self.world.scene.add_default_ground_plane()  # type: ignore

        if world_usd_path:
            add_reference_to_stage(str(world_usd_path), "/World/Environment")

        # Set up camera
        self.camera_manager = CameraManager()

        print("Robots positioned using Core API")

    def add_cube(
        self, name: str, position: np.ndarray, size: np.ndarray, color: np.ndarray
    ) -> DynamicCuboid:
        # Add a cube object
        cube = self.world.scene.add(  # type: ignore
            DynamicCuboid(
                prim_path=f"/World/{name}",
                name=name,
                position=position,
                scale=size,
                color=color,
            )
        )
        return cube

    def _add_environment(self, usd_path: Path) -> bool:
        """
        Add an environment to the simulation from a USD file.

        Args:
            usd_path: Path to the USD file for the environment
        Returns:
            bool: True if added successfully, False otherwise
        """
        try:
            self.world.scene.add_usd(  # type: ignore
                usd_path,
                prim_path="/World/Environment",
            )
            return True
        except Exception as e:
            print(f"Failed to add environment from {usd_path}: {e}")
            return False

    def add_robot(
        self,
        name: str,
        usd_path: Path,
        position: np.ndarray,
        orientation: np.ndarray,
        phase_offset: float = 0.0,
    ) -> bool:
        """
        Add a robot to the simulation.

        Args:
            name: Name identifier for the robot
            position: 3D position as numpy array [x, y, z]
            orientation: Quaternion orientation as numpy array [w, x, y, z]
            phase_offset: Phase offset for animation

        Returns:
            Robot instance
        """
        prim_path = f"/World/{name}"
        robot = Robot(
            world=self.world,
            usd_path=usd_path,
            prim_path=prim_path,
            name=name,
            position=position,
            orientation=orientation,
            phase_offset=phase_offset,
        )
        self.robots.append(robot)
        return True

    def initialize_simulation(self):
        """Initialize the simulation and all robots."""
        self.world.reset()
        for robot in self.robots:
            robot.initialize()

    def run_simulation(self, slowdown_factor: int = 30):
        """
        Run the main simulation loop.

        Args:
            slowdown_factor: Factor to slow down robot animations
        """
        # frame = 0

        while True:
            # Step the simulation
            self.world.step(render=True)

            # # Capture and save images
            # if self.camera_manager:
            #     self.camera_manager.capture_and_save_images(frame)

            # # Animate all robots
            # for robot in self.robots:
            #     robot.animate(frame, slowdown_factor)

            # frame += 1
