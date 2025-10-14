"""
SimulationWorld class for managing the overall simulation environment in Isaac Sim.
"""

from pathlib import Path
import numpy as np
from typing import Optional, List

from isaacsim.core.api import World
from isaacsim.core.api.objects import DynamicCuboid

from robot import Robot
from camera_manager import CameraManager


class SimulationWorld:
    """Main class to manage the simulation world and coordinate all components."""
    
    def __init__(self):
        """
        Initialize the simulation world.
        
        """
        self.world = World()
        self.robots: List[Robot] = []
        self.camera_manager: Optional[CameraManager] = None
        
        self._setup_world()
    
    def _setup_world(self):
        """Set up the basic world environment."""
        # Add default ground plane
        self.world.scene.add_default_ground_plane()  # type: ignore
        
        
        
        # Set up camera
        self.camera_manager = CameraManager()
        
        print("Robots positioned using Core API")
    
    def add_cube(self, name: str, position: np.ndarray, size: np.ndarray, color: np.ndarray) -> DynamicCuboid:
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
    
    def add_robot(self, name: str, usd_path: Path, position: np.ndarray, orientation: np.ndarray, 
                  phase_offset: float = 0.0) -> bool:
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
            phase_offset=phase_offset
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