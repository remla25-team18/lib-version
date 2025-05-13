from setuptools import setup, find_packages
import os
import re

def read_version():
    with open(os.path.join("lib_version", "version.py")) as f:
        match = re.search(r'^__version__ = ["\']([^"\']*)["\']', f.read(), re.M)
        if match:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")

setup(
    name="lib-version",
    version=read_version(),
    packages=find_packages(),
)
