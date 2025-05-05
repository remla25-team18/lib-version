import os

class VersionUtil:

    def __init__(self):
        pass

    @staticmethod
    def get_version():
        try:
            with open("version.txt", "r") as f:
                return f.read().strip()
        except Exception:
            return "unknown"