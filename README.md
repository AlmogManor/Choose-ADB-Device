# Welcome to Ichoose-device

## What is this Project?

Ichoose-device allows you to interactively select a connected adb device,
to avoid using the `-s` flag in adb every command, while displaying useful information.

## Installation

In your shell, run:
```shell
	pip install ichoose-device
```

And then add the following to your shell's rc file (e.g:`~/.zshrc`):
```
	alias ichd="choose-adb-serial;export ANDROID_SERIAL=\$(cat '/tmp/ichoose-device-serial-file')"
```

## How do I Use this Project?

The project ships a script called `choose-adb-serial`.  
Running this script will prompt you to select a device, and
save the output to `/tmp/ichoose-device-serial-file`.  
You can then set the environment variable `ANDROID_SERIAL` to the file's contents,
and adb will choose the device when running commands.  
To put this all into one command, simply paste this into your `.zshrc` (or any other rc) file:
```
	alias ichd="choose-adb-serial;export ANDROID_SERIAL=\$(cat '/tmp/ichoose-device-serial-file')"
```
