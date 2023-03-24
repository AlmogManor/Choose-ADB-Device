#!/bin/zsh

__get_available_devices() {
	adb_devices=$(adb devices 2>/dev/null)
	if [[ "$?" -ne 0 ]]; then
		echo ""
	else
		adb_output="$(adb devices | tail -n +2)"

		while IFS= read -r adb_line; do
			echo "$adb_line" | cut -f1
		done <<< "$adb_output"
	fi
}

__get_device_model() {
	adb -s "$1" shell getprop ro.product.model
}

__get_device_manufacturer() {
	adb -s "$1" shell getprop ro.product.manufacturer
}

__get_device_android_version() {
	adb -s "$1" shell getprop ro.build.version.release
}

__get_device_serial() {
	adb -s "$1" shell getprop ro.serialno
}

__is_device_local_or_remote() {
	if [[ "$1" == *":"* ]]; then
		echo -n "Remote"
	else
		echo -n "Local"
	fi
}

__display_device() {
	export adb_id="$1"
	# local/remote, model (marketing name), manufacturer, android, serial, adb id (serial/host:ip)
	echo "$(__is_device_local_or_remote $adb_id):  $(__get_device_model $adb_id) 󰈏 $(__get_device_manufacturer $adb_id)  $(__get_device_android_version $adb_id) 󰁲  $(__get_device_serial $adb_id)  $adb_id"
}

__generate_available_devices_message() {
	devices="$(__get_available_devices)"
	
	while IFS= read -r adb_id ; do
		export adb_id
		(__display_device $adb_id < /dev/null)
	done <<< "$devices"
}

_chd() {
	local output="$(__generate_available_devices_message)"

	# Split on line breaks.
	local -a values=( "${(f)output}" )
	compadd -a values
}

chd() {
	export AUTOCOMPLETE_LINE="$@"
	export ANDROID_SERIAL="$(echo "$AUTOCOMPLETE_LINE" | rev | cut -d " " -f1 | rev)"
	export ANDROID_MODEL="$(echo "$AUTOCOMPLETE_LINE" | cut -d " " -f3)"
}

compdef _chd chd
