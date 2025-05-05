class VersionUtil:

    def __init__(self):
        pass

    @staticmethod
    def get_version():
        try:
            with open("VERSION", "r") as f:
                return f.read().strip()
        except Exception:
            return "unknown"

print(VersionUtil.get_version())