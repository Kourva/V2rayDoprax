#!/sut/bin/env python3


# Get daily IPs from http://bot.sudoer.net


# Imports
import requests
import time
import sys


# Gets IPs from target website
def get_ip():
    respones = requests.get("http://bot.sudoer.net/result.cf")
    if respones.status_code == 200:
        return respones.text.strip()


# Save the IPs into txt file
def save_ip():
    temp = get_ip()
    with open("ip/all_result.txt", "w") as file:
        file.write(temp)

    for char in "\033[2;34mResults saved in ip/all_result.txt\033[m\n":
        print(char, end="", flush=True)
        time.sleep(0.01)


# Run the program
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python getAllIPs.py [arguments]

    for save the IPs -> python getAllIPs.py -s
    for help message -> python getAllIPs.py [-h, --help] 
"""
            )
        elif sys.argv[1] == "-s":
            save_ip()
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")


# EOF
