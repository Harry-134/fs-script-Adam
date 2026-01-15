#!/usr/bin/env python3
import os
import sys
import argparse
import platform
from datetime import datetime

# Current version
VERSION = "1.0.0"

#Checks if the current OS is linux based
def check_os():
    current_os = platform.system()
    if current_os != "Linux":
        print(f"Error: This script is only for Linux based systems. Currently on {current_os}")
        sys.exit(1)

#Flags and arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="System & Network monitoring script")
    parser.add_argument("-v", "--version", action="version", version=f"LoginMonitor v{VERSION}")
    return parser.parse_args()

#If no command is given, gives user, time and startup message 
def main():

    check_os()
    args = parse_arguments()

    user = os.getenv('USER') or "Unknown"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- Login Monitor Started ---")
    print(f"User: {user}")
    print(f"Time: {current_time}")
    print(f"OS: {platform.system()} {platform.release()}")
    print("--------------------------------")

if __name__ == "__main__":
#Failsafe if user does CTRL + C
    try:
     main()
    except KeyboardInterrupt:
     print("\nAborted by user.")
     sys.exit(0)
