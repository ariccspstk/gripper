import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg = get_package_share_directory('gripper')
    urdf_file = os.path.join(pkg, 'urdf', 'gripper_with_camera.urdf.xacro')

    robot_description = ParameterValue(
        Command(['xacro ', urdf_file]), value_type=str
    )

    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('realsense2_camera'),
                'launch', 'rs_launch.py'
            )
        ),
        launch_arguments={
            'camera_name': 'camera',
            'camera_namespace': 'camera',
            'publish_tf': 'true',
            'enable_depth': 'true',
            'align_depth.enable': 'true',
        }.items()
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
                    package='joint_state_publisher_gui',
                    executable='joint_state_publisher_gui',
                ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(pkg, 'config', 'view_robot.rviz')],
        ),
        realsense_launch,
    ])