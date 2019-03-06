#!/usr/bin/env python
#
#This program was created following the tutorials on Udemy for the course
# Learn Python & Ethical Hacking From Scratch

import subprocess

interface = input("Interface to change:")
newMAC = input("New MAC:")

print("[+} Changing MAC address for " + interface + " to " + newMAC)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMAC])
subprocess.call(["ifconfig", interface, "up"])

