from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='talker_listener',
            executable='talker',
            name='talker_node'
        ),
        Node(
            package='talker_listener',
            executable='listener',
            name='listener_node'
        )
    ])

return LaunchDescription([
    talker,
    listener
])