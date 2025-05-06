from .version import __version__

class VersionUtil:

    @staticmethod
    def get_version():
        return __version__

    @staticmethod
    def print_version():
        print(__version__)
