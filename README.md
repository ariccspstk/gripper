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
git clone https://github.com/ariccspstk/gluon_gripper.git
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

## Usage

### Bringup (Real)

```bash
ros2 launch gripper gripper_bringup.launch.py
```
### View urdf model

```bash
ros2 launch gripper gripper_display.launch.py
```