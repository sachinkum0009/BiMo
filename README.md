# BiMo
Bi-Manual Mobile Robot

## Overview

This repo uses isaac sim to simulate a bi-manual mobile robot with two Franka Panda arms mounted on a mobile base. The robot can be controlled via ROS2 topics.

## Isaac Sim Franka ROS2

![franka_ros2](media/isaac_sim_franka_ros2.png)

## Robot Joint Controller to Control Franka Panda Arms

![rqt_joint_command_publisher](media/robot_joint_controller.png)

# Architecture

```mermaid
classDiagram
    class SimulationWorld {
        -World world
        -List~Robot~ robots
        -CameraManager camera_manager
        +__init__()
        -_setup_world()
        +add_cube(name, position, size, color) DynamicCuboid
        +add_robot(name, usd_path, position, orientation, phase_offset) bool
        +initialize_simulation()
        +run_simulation(slowdown_factor)
    }

    class Robot {
        -World world
        -Path usd_path
        -str prim_path
        -str name
        -ndarray position
        -ndarray orientation
        -float phase_offset
        -SingleArticulation articulation
        -XFormPrim xform
        +__init__(world, usd_path, prim_path, name, position, orientation, phase_offset)
        -_setup_robot()
        +set_pose(position, orientation)
        +initialize()
        +animate(frame, slowdown_factor)
        +get_joint_positions() ndarray
    }

    class CameraManager {
        -str prim_path
        -Tuple position
        -Camera camera
        +__init__(prim_path, position)
        -_setup_camera()
        +capture_and_save_images(frame_number, save_interval)
        -_save_rgb_image(rgb_img, frame_number)
        -_save_depth_image(depth_image, frame_number)
    }

    class Position {
        +float x
        +float y
        +float z
        +to_numpy() ndarray
        +__array__(dtype)
        +__iter__()
        +__repr__() str
    }

    class Orientation {
        +float roll
        +float pitch
        +float yaw
        +to_quaternion() ndarray
        +to_numpy() ndarray
        +__array__(dtype)
        +__iter__()
        +__repr__() str
        +from_quaternion(quaternion)$ Orientation
        +identity()$ Orientation
    }

    class Color {
        <<enumeration>>
        RED
        GREEN
        BLUE
        ORANGE
        YELLOW
        PURPLE
        WHITE
        BLACK
        GRAY
        CYAN
        MAGENTA
        +as_array() ndarray
    }

    class ManipulatorRobot {
        <<enumeration>>
        +Path FRANKA
        +Path FRANKA_ROS2
        +Path ROBOT2
        +Path ROBOT3
    }

    class MobileRobot {
        <<enumeration>>
        +Path NOVA_CARTER
        +Path TURTLEBOT3
        +Path ROBOT2
        +Path ROBOT3
    }

    class RobotEnum {
        <<enumeration>>
        +ManipulatorRobot MANIPULATOR_ROBOT
        +MobileRobot MOBILE_ROBOT
    }

    SimulationWorld "1" *-- "0..*" Robot : contains
    SimulationWorld "1" *-- "0..1" CameraManager : manages
    SimulationWorld ..> Position : uses
    SimulationWorld ..> Orientation : uses
    SimulationWorld ..> Color : uses
    SimulationWorld ..> RobotEnum : uses
    Robot ..> Position : uses
    Robot ..> Orientation : uses
    RobotEnum *-- ManipulatorRobot
    RobotEnum *-- MobileRobot
```