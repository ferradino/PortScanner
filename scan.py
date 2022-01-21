#!/bin/python3

import nmap3
import sys
import re
import socket
from datetime import datetime

np = nmap3.Nmap()
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ip_addr = socket.gethostbyname(sys.argv[1])

print("/n" + ip_addr)

def welcome_message():

    print("-" * 50)
    print("Welcome to " + str(np.nmap_version_detection) + " !")
    print("Nmap Will Run A Basic Port Scan Followed By An Advance Port Scan On Target: ")
    print("-" * 50)

def basic_scan(ip):

    print("Beginning Basic Scan!: " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    try:
        np.scan_command(ip, "T4", "-p-", "-oN", "basic-scan.txt")
    except:
        print("Failed Scan")
        exit()

    print("Scan Completed: " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print(" - " * 50)
    
def advance_scan(ip, ports):
    
    print("Beginning Advance Scan!: " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    try:
        np.scan_command(ip, "T4", "-A", ports, "-oN", "basic-scan.txt")
    except:
        print("Failed Scan")
        exit()

    print("Scan Completed: " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print(" - " * 50)


open_ports = None


if ip_add_pattern.search(ip_addr):
    welcome_message()
    basic_scan(ip_addr)
    advance_scan(ip_addr, open_ports)
else:
    print("Invalid IPv4 address")
    exit()
