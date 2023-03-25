from subprocess import DEVNULL, PIPE, Popen
from typing import List

from .adb_device import AdbDevice
from .exceptions.failed_to_get_adb_devices import FailedToGetAdbDevices


class AdbDeviceFetcher:
    @staticmethod
    def fetch_devices() -> List[AdbDevice]:
        return [
            AdbDevice.from_adb_identifier(adb_identifier) for adb_identifier in AdbDeviceFetcher.__get_online_devices()
        ]

    @staticmethod
    def __get_online_devices() -> List[str]:
        raw_devices = AdbDeviceFetcher.__extract_device_lines(AdbDeviceFetcher.__get_raw_adb_output())

        online_devices = []
        for device_line in raw_devices:
            adb_identifier, status = device_line.split("\t")

            if status == "device":
                online_devices.append(adb_identifier)

        return online_devices

    @staticmethod
    def __extract_device_lines(raw_adb_output: str) -> List[str]:
        return [device.strip() for device in raw_adb_output.split("\n") if device][1:]

    @staticmethod
    def __get_raw_adb_output() -> str:
        with Popen("adb devices", shell=True, stdout=PIPE, stderr=DEVNULL) as adb_process:
            adb_process.wait()

            if adb_process.returncode != 0 or not adb_process.stdout:
                raise FailedToGetAdbDevices()

            return adb_process.stdout.read().decode()
