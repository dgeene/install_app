import os
import argparse
from shutil import which
import install_app

def main() -> None:
    ios_deploy_path = which('ios-deploy')
    adb_path = which('adb')
    if not ios_deploy_path:
        print('ios-deploy needs to be installed and available on PATH')
        exit(1)
    if not adb_path:
        print('adb needs to be installed and available on PATH')
        exit(1)

    parser = argparse.ArgumentParser(prog="mobile_installer", 
                                     description="Utility function to install an app on android or ios")
    parser.add_argument('appfile', help='The path to either .ios or .apk file')
    args = parser.parse_args()
    app_path = args.appfile

    if not os.path.exists(app_path):
        print('The app path provided does not exist')
        exit(1)
    file_ext = os.path.splitext(app_path)
    if file_ext[1] not in ['.ipa', '.apk']:
        print('Invalid file type. Must be .apk or .ipa')
        exit(1)

    if file_ext[1] == '.ipa':
        devices = install_app.list_ios_devices(ios_deploy_path)
        choice = install_app.handle_device_selection(devices)
        install_app.install_ios_device(ios_deploy_path, choice, app_path)
    elif file_ext[1] == '.apk':
        devices = install_app.list_android_devices(adb_path)
        choice = install_app.handle_device_selection(devices)
        install_app.install_android_device(adb_path, choice, app_path)
    else:
        print('Invalid platform')
