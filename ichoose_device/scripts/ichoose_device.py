import inquirer

from ichoose_device.colors.colored_text import ColoredText
from ichoose_device.device.adb_device import AdbDevice
from ichoose_device.device.adb_device_connection_type import AdbDeviceConnectionType
from ichoose_device.device.adb_device_fetcher import AdbDeviceFetcher


def __make_prompt(device: AdbDevice) -> str:
    if device.connection_type == AdbDeviceConnectionType.REMOTE:
        connection_type = ColoredText("Remote:", "#5df0f0")
    else:
        connection_type = ColoredText("Local:", "#f0f05d")

    model = ColoredText(f" {device.model}", "#39a4c6")
    manufacturer = ColoredText(f"󰈏 {device.manufacturer}", "#909090")
    android_version = ColoredText(f" {str(device.android_version)}", "#a4c639")
    serial = ColoredText(f"󰁲  {device.serial}", "#cccccc")
    adb_identifier = ColoredText(f" {device.adb_identifier}", "#ff6262")

    return " ".join(
        [str(connection_type), str(model), str(manufacturer), str(android_version), str(serial), str(adb_identifier)]
    )


def main():
    options = [
        inquirer.List(
            "device",
            message="Pick a device",
            choices=[__make_prompt(device) for device in AdbDeviceFetcher.fetch_devices()],
        )
    ]

    choice = inquirer.prompt(options)

    if choice:
        with open("/tmp/ichoose-device-serial-file", "w+") as output:
            output.write(choice["device"].split(" ")[-1])


if __name__ == "__main__":
    main()
