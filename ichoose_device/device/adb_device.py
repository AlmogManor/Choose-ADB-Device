from __future__ import annotations

from dataclasses import dataclass

from .adb_command_runner import AdbCommandRunner
from .adb_device_connection_type import AdbDeviceConnectionType


@dataclass
class AdbDevice:
    model: str
    android_version: str
    manufacturer: str
    serial: str
    adb_identifier: str
    connection_type: AdbDeviceConnectionType

    @staticmethod
    def from_adb_identifier(adb_iderntifier: str) -> AdbDevice:
        return AdbDevice(
            model=AdbCommandRunner.getprop("ro.product.model", adb_iderntifier).strip(),
            android_version=AdbCommandRunner.getprop("ro.build.version.release", adb_iderntifier).strip(),
            manufacturer=AdbCommandRunner.getprop("ro.product.manufacturer", adb_iderntifier).strip(),
            serial=AdbCommandRunner.getprop("ro.serialno", adb_iderntifier).strip(),
            adb_identifier=adb_iderntifier.strip(),
            connection_type=AdbDeviceConnectionType.REMOTE if ":" in adb_iderntifier else AdbDeviceConnectionType.LOCAL,
        )
