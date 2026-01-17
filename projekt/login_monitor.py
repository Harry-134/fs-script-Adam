#!/usr/bin/env python3
import os
import sys
import argparse
import platform
import logging
import socket
import requests
import shutil
import subprocess
from datetime import datetime

# Current version
VERSION = "1.0.0 - By Adam"

LOG_FILE = "system_monitor.log"

def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

#Checks if the current OS is linux based
def check_os():

    current_os = platform.system()
    if current_os != "Linux":
        print(f"Error: This script is only for Linux based systems. Currently on {current_os}")
        sys.exit(1)

#Gets my public and local ip then saves to log file
def get_network_info():

    print("\n--- Network Information---")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        print(f"Local IP: {local_ip}")
        logging.info(f"Local IP: {local_ip}")
    except Exception as e:
        print(f"Could not get Local IP: {e}")
        logging.error(f"Local IP error: {e}")
    try:
        response = requests.get('https://api.ipify.org', timeout=3)
        if response.status_code == 200:
            public_ip = response.text
            print(f"Public IP: {public_ip}")
            logging.info(f"Public IP: {public_ip}")
    except requests.RequestException as e:
        print(f"Offline or timeout: {e}")
        logging.warning(f"Could not fetch Public IP {e}")

#Checks for listening TCP and UDP ports, then writes out the first 6
    try:
        print("\n[Active ports]")
        result = subprocess.check_output(["ss", "-tuln"], text=True)
        lines = result.splitlines()
        for line in lines[:6:]:
         print(line)
         logging.info(f"Active port {line}")

        if len(lines) > 6:
         print(f"...(and {len(lines)-6} more lines)")
         logging.info(f"...(and {len(lines)-6} more lines)")
    except Exception as e:
        print("Could not get ports: {e}")
        logging.error(f"Port scan error: {e}")

#Gets storage and cpu load info
def get_system_info():
    print ("\n--- System info ---")
    try:
        total, used, free = shutil.disk_usage("/")
        #2**30 turns bytes to GB
        freegb = free // (2**30)
        totalgb = total // (2**30)

        print(f"Disk space: {freegb} GB free / {totalgb} GB total")
        logging.info(f"Disk storage: {freegb}GB free of {totalgb}GB")
    except Exception as e:
        print(f"Disk check failed: {e}")
        logging.error(f"Disk check error: {e}")

    try:
        load1, load5, load15 = os.getloadavg()
        print(f"CPU load (1, 5, 15 min): {load1}, {load5}, {load15}")
        logging.info(f"CPU load: {load1}, {load5}, {load15}")
    except Exception as e:
        print(f"Load check failed: {e}")

#Checks RAM usage
    try:
        result = subprocess.check_output(["free", "-h"], text=True)
        lines = result.splitlines()
        for line in lines:
         if "Mem:" in line:
          print(f"RAM usage: {line}")
          logging.info(f"RAM usage: {line.strip()}")
    except Exception as e:
        print(f"RAM check failed: {e}")

#Flags and arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="System & Network monitoring script")
    parser.add_argument("-v", "--version", action="version", version=f"LoginMonitor v{VERSION}")
    return parser.parse_args()

#Checks if you have root priviledges
def check_priviledges():

    try:
        is_root = os.getuid() == 0

        if is_root:
         msg = "Running with ROOT priviledges."
         print(f"Warning: {msg}")
         logging.warning(msg)
        else:
         msg = "Running as a standard user."
         print(f"Priviledge: {msg}")
         logging.info(msg)

    except AttributeError:
        pass

#If no command is given, gives user, time and startup message 
def main():

    setup_logging()
    check_os()
    args = parse_arguments()

    user = os.getenv('USER') or "Unknown"
    hostname = platform.node() or "Unknown" #harry adition

    logging.info(f"Script started by {user}")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- Login Monitor Started ---")
    print(f"User: {user}")
    print(f"Hostname: {hostname}") #harryatition
    print(f"Time: {current_time}")
    print(f"OS: {platform.system()} {platform.release()}")
    #Calls the network funktion to get ip's
    get_network_info()
    #Calls the system info function for cpu/storage info
    get_system_info()
    #Calls the priviledge check function
    check_priviledges()

    print("--------------------------------")

    logging.info("System checks passed.")

if __name__ == "__main__":
#Failsafe if user does CTRL + C
    try:
     main()
    except KeyboardInterrupt:
     print("\nAborted by user.")
     sys.exit(0)
