# py-linux-capabilities
Python enum list of Linux Capabilities based on capabilities(7)

## Author
damwiw (github.com)

## Build
python3 -m pip install

## Installation
python3 -m pip install [--break-system-packages] linux_capabilities

## Use
from linux_capabilities import LinuxCapabilities
mycap = LinuxCapabilities.CAP_SYS_ADMIN
