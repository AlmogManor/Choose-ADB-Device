class AdbCommandException(Exception):
    def __init__(self, stderr: str):
        super().__init__(f"stderr: {stderr}")
