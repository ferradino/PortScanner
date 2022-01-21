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
    print("Welcome to " + np.nmap_version() + " !")
    print("Now Running Basic Scan On All Ports: " + datetime())
    print("-" * 50)

def basic_scan(ip):

    print("/n Beginning Basic Scan!")

    try:
        np.scan_command(ip)
    except:
        print("Failed Scan")
        exit()
    
    original_stdout = sys.stdout 

    sys.stdout = sys.stderr 
    print(np)

    sys.stdout = original_stdout 

    print("Scan Completed! " + datetime())


if ip_add_pattern.search(ip_addr):
    welcome_message()
    basic_scan(ip_addr)
else:
    print("Invalid IPv4 address")
    exit()



