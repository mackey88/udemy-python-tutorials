#!/usr/bin/env python
#
#This program was created following the tutorials on Udemy for the course
# Learn Python & Ethical Hacking From Scratch

import subprocess
import optparse
import re

#Get options provided by user via the command line
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an MAC, use --help for more info")
    return options


#Take in an interface and a MAC then change the passed interface's MAC to new MAC
def change_mac(interface, new_mac):
    print("[+} Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


#Return the MAC of the passed interface
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_match = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())
    if mac_match:
        return mac_match.group(0)
    else:
        print("[-] Could not read MAC address.")

#Get user inputs
options = get_arguments()

#Check the MAC address at the start of the program
current_mac = get_current_mac(options.interface)
print("Current MAC " + str(current_mac))

#change MAC address based on user input
change_mac(options.interface, options.new_mac)

#Check if the MAC has been changed
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address successfully changed to " + str(current_mac))
else:
    print("[-] Failed to change MAC address")




