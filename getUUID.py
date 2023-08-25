#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Get both version1 or version4 UUID from https://www.uuidgenerator.net
# GitHub: https://github.com/Kourva/getUUID

# Imports
import requests, time, sys, bs4

# Gets version 1 UUID
def get_version1():
    response = requests.get("https://www.uuidgenerator.net/version1")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup.find(id="generated-uuid").text.upper()

# Gets version 4 UUID
def get_version4():
    response = requests.get("https://www.uuidgenerator.net/version4")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup.find(id="generated-uuid").text.upper()

# Takes arguments
arguments = sys.argv

# Help message
help_message = """
Help: python getUUID.py [[-h] [-v1] [-v4]]
    -h  : Show this message and exit.
    -v1 : get version 1 UUID
    -v4 : get version 4 UUID

* What is a Version 1 UUID?
    A Version 1 UUID is a universally unique identifier that 
    is generated using a timestamp and the MAC address of 
    the computer on which it was generated.

* What is a version 4 UUID?
    A Version 4 UUID is a universally unique identifier that 
    is generated using random numbers.using a secure random 
    number generator.
"""


# Main
if __name__ == "__main__":
    if "-h" in arguments:
        print(help_message)
        sys.exit()

    if "-v1" in arguments:
        for char in "\033[2;34m* Getting version1 UUID for you...\033[m\n":
            print(char, end="", flush=True)
            time.sleep(0.01)
        print(f"Version1 UUID: \033[2;32m{get_version1()}\033[m\n")

    if "-v4" in arguments:
        for char in "\033[2;34m* Getting version4 UUID for you...\033[m\n":
            print(char, end="", flush=True)
            time.sleep(0.01)
        print(f"Version4 UUID: \033[2;32m{get_version4()}\033[m\n")

    if len(sys.argv) == 1:
        print("\033[2;31mError: no argument found! Use -h\033[m")
