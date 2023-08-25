#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script gets vmess config from vmess url

# Imports
import base64, time, json, sys

# Printer
def printer(message: str) -> None:
    for char in json.dumps(message, indent=4):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# Get config from url
def get_config(vmess_url: str) -> dict:
    encoded_data = vmess_url.split("vmess://")[1].strip()
    return json.loads(
        base64.b64decode(encoded_data).decode("utf-8").replace("'", '"')
    )

# Main
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
        print("No argument specified! run with -h")
