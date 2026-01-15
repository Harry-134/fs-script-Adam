# Project script for login monitoring

## Purpose / Goal
* This project aims to be an automated script that logs most things upon user login.

## Features
* It logs network services like local ip, public ip and network status.
* System logging such as time of login, system load and uptime.
* This while adding ease of use commands such as -h for help and -v for version.
* Pre check to see if permissions and OS are correct.

## System requirements
* **OS:** Linux-based enviroment
* **Python:** Python 3.10 or higher (Not recommended to run lower versions)
* **Dependencies:** Requests library for public ip lookup. installed via `pip install requests` for linux or `sudo apt install python3-requests` for Kali linux.

## Installation / Usage
* Clone my repository at `git clone https://github.com/AdamosRG/fs-script.git`
* Locate the correct folder which would be `cd fs-script/projekt`
* Make the file executable with `chmod +x login_monitor.py`
* Launch it with `sudo ./login_monitor.py`

### Arguments / Flags
* `-h` for help
* `-v` for version

