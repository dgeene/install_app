# Install App
Installs an .apk or .ipa file onto a phone.

## Problem Statement
I have a build of a mobile app and many phones connected to my computer. I want to point an app file to a phone and have it installed without remembering which command flags to use.

## Install
Install in the user's ~/bin folder with pipx

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