# Install App
Installs an .apk or .ipa file onto a phone.

## Problem Statement
I have a build of a mobile app and many phones connected to my computer. I want to point an app file to a phone and have it installed without remembering which command flags to use.

## Install
Installing using pipx

First build the package in this directory:
```bash
python setup.py sdist
```

Then run pipx install on it
```bash
pipx install install_app/dist/install_app-1.0.0.tar.gz
```

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
- add as command line util https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point or https://python-poetry.org/docs/pyproject/#scripts



ios-deploy -j outputs invalid json when multiple devices are present