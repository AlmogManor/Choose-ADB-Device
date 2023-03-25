from subprocess import PIPE, Popen

from .exceptions.adb_command_exception import AdbCommandException


class AdbCommandRunner:
    @staticmethod
    def run(command: str, adb_id: str) -> str:
        with Popen(f"adb -s {adb_id} shell {command}", shell=True, stdout=PIPE, stderr=PIPE) as adb_command:
            adb_command.wait()

            if adb_command.returncode != 0 or not adb_command.stdout:
                raise AdbCommandException(
                    adb_command.stderr.read().decode() if adb_command.stderr else "Couldn't get stderr"
                )

            return adb_command.stdout.read().decode()

    @staticmethod
    def getprop(prop: str, adb_id: str) -> str:
        return AdbCommandRunner.run(f"getprop {prop}", adb_id)
