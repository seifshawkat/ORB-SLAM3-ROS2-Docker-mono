import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Set environment variables
    robot_namespace = "robot_0"
    robot_x = "0.0"
    robot_y = "0.0"

    orb_slam3_launch_file_dir = os.path.join(
        get_package_share_directory('orb_slam3_ros2_wrapper'), 'launch')

    orb_slam3_launch_file_path = os.path.join(
            orb_slam3_launch_file_dir, 'mono.launch.py')

    # Launch the rgbd.launch.py file
    orb_slam3_launch_description = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(orb_slam3_launch_file_path),
            launch_arguments={"robot_namespace": robot_namespace,
                            "robot_x": robot_x,
                            "robot_y": robot_y}.items(),
    )

    return LaunchDescription([
        # SetEnvironmentVariable(name='ROBOT_NAMESPACE', value=robot_namespace),
        # SetEnvironmentVariable(name='ROBOT_X', value=robot_x),
        # SetEnvironmentVariable(name='ROBOT_Y', value=robot_y),
        orb_slam3_launch_description
    ])


if __name__ == '__main__':
    generate_launch_description()
