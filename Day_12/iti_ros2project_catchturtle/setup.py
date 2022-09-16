from setuptools import setup

package_name = 'iti_ros2project_catchturtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='h3esawy',
    maintainer_email='h3esawy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "node_chaseControl=iti_ros2project_catchturtle.node_chaseControl:main",
            "node_turSpawn=iti_ros2project_catchturtle.node_turSpawn:main",
        ],
    },
)
