# Gripper Package

ROS 2 Gripper package to drive dynamixel motors.

## Prerequisites

- ROS 2 Jazzy installed
- Setups done for dynamixel motors ID's 1 & 2

## Setup

### 1. Clone the repository

```bash
cd ~/ros2_ws/src

# Gripper package
git clone https://github.com/ariccspstk/gripper.git

# Robotis dynamixel packages
mkdir robotis
cd robotis
git clone -b jazzy https://github.com/ROBOTIS-GIT/DynamixelSDK.git
git clone -b jazzy https://github.com/ROBOTIS-GIT/dynamixel_hardware_interface.git
git clone -b jazzy https://github.com/ROBOTIS-GIT/dynamixel_interfaces.git
cd ..
```

### 2. Install dependencies

From the workspace root:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

### 3. Build

```bash
colcon build
source install/setup.bash
```

### Usage

#### Bringup (Real)

```bash
ros2 launch gripper gripper_bringup.launch.py
```

#### View urdf model

```bash
ros2 launch gripper gripper_display.launch.py
```

#### Control joints with rqt_joint_trajectory_controller

With the gripper bringup running, open a new terminal:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run rqt_joint_trajectory_controller rqt_joint_trajectory_controller
```

In the rqt window:

1. Select the appropriate **Controller Manager ns** (namespace) for your robot.
2. Select the **Controller** (e.g. `joint_trajectory_controller`) from the dropdown.
3. Enable the controller/joints and use the sliders to move each joint.

Frame tree:

![Gripper TF frame tree](gripper/assets/gripper_with_camera_frames.png)