from setuptools import find_packages, setup

package_name = "map_saver"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="sumagnadas",
    maintainer_email="sumagnadas@gmail.com",
    description="TODO: Package description",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["auto_map_saver = map_saver.map_saver:main"],
        "console_scripts": ["voice_teleop = scripts.voice:main"],
    },
)