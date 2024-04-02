import re
import subprocess


def list_ios_devices(ios_deploy: str) -> list:
    """ Use ios-deploy -c to list out connected devices

    Parse the string output. ios-deploy outputs malformed json
     when using the -j flag when multiple devices are connected
     thus why we use string parsing.
    """
    devices = []
    uid_pattern = r"Found\s(.*?)\("
    completed = subprocess.run([ios_deploy, '-c'], capture_output=True, text=True)
    if completed.returncode > 0:
        # error 255 here if no devices connected
        print('Error listing connected ios devices')
        print(completed.stderr)
    else:
        out = completed.stdout.splitlines()
        for line in out:
            uid_match = re.search(uid_pattern, line)
            if uid_match:
                devices.append(uid_match[1].strip())
    return devices

def list_android_devices(adb: str) -> list:
    """ Use adb devices to get a list of android devices

    Skips unauthorized devices
    """
    devices = []
    completed = subprocess.run([adb, 'devices'], capture_output=True, text=True)
    if completed.returncode > 0:
        print('Error listing connected android devices')
        print(completed.stderr)
        return None
    lines = completed.stdout.splitlines()
    for line in lines:
        if '\tdevice' in line: # few gotchas like 'unauthorized'
            devices.append(line.split('\t')[0])
    return devices

def install_ios_device(ios_deploy: str, ios_device: str, app: str) -> None:
    """ Use ios-deploy to install the app

    """
    print(f'Attemping install of {app} onto {ios_device}')
    completed = subprocess.run([ios_deploy, '-i', ios_device, '-b', app], capture_output=True, text=True)
    if completed.returncode > 0:
        print('Error installing onto ios device')
        print(completed.stderr)
    else:
        print('Successfully installed ios app')

def install_android_device(adb: str, android_device: str, app: str) -> None:
    """ Use adb to install the app

    """
    print(f'Attemping install of {app} onto {android_device}')
    completed = subprocess.run([adb, '-s', android_device, 'install', app], capture_output=True, text=True)
    if completed.returncode > 0:
        print('Error installing onto android device')
        print(completed.stderr)
    else:
        print('Successfully installed android app')

def handle_device_selection(device_list: list) -> str:
    """ Prompt to select which device to install the app to

    """
    if len(device_list) > 1:
        prompt = "Select a mobile device to install to:\n"
        for i, d in enumerate(device_list):
            prompt += f"{i} :: {d}\n"
        print(prompt)
        while True:
            try:
                answer = int(input('-->'))
                device_list[answer]
                break
            except:
                print('Invalid option')
        return device_list[answer]
    else:
        return device_list.pop()
