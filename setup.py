from setuptools import setup, find_packages
from lib_version_remla25_team18.version import __version__

setup(
    name='lib_version_remla25_team18',
    version=__version__,
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "lib_version = lib_version:VersionUtil.print_version"
        ]
    }
)