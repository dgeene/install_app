# Install App
Installs an .apk or .ipa file onto a phone.

## Problem Statement
I have a build of a mobile app and many phones connected to my computer. I want to point an app file to a phone and have it installed without remembering which command flags to use for the platform specific utilities.

## Requirements
`install-app` uses `ios-deploy` and `adb` to install app files onto a phone.

These utilities must be installed and available in PATH.

ios-deploy: https://github.com/ios-control/ios-deploy

adb: https://developer.android.com/tools/adb

## Install
Installing using pipx

```bash
pipx install git+https://github.com/dgeene/install_app.git
```
And you're done

## Run
install-app ~/app-builds/com.dave.myapp-v8.1.3-staging-release.apk

## TODO
- Handle multiple phone connections
- Handle android unauthorzed devices
- handle when no devices are returned
- handle non phone adb devices
- output device names in addition to uid
- handle uninstalling the app first
- progress bar for installs



ios-deploy -j outputs invalid json when multiple devices are present