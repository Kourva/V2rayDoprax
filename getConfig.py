#!/usr/bin/env python3


# Get vmess config from vmess url


# Imports
import base64
import time
import json
import sys


def printer(message: str) -> None:
    message = message.replace("'", '"')
    parsed_json = json.loads(message)
    pretty_json = json.dumps(parsed_json, indent=4)
    for char in pretty_json:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

    print("\n")


def get_config(vmess_url):
    target = vmess_url.split("vmess://")[1].strip()

    tempvar = target.encode("ascii")
    message = base64.b64decode(tempvar)
    configs = message.decode("ascii")

    return configs


# Run the program
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python getConfig.py [argumentss]

    for extracting config    -> python getConfig.py [vmess  url]
    for showing help message -> python getConfig.py [-h, --help] 
"""
            )
        else:
            printer(get_config(sys.argv[1]))
    else:
        print("No argument! run with -h")


# EOF
