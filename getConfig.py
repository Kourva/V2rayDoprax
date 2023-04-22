#!/usr/bin/env python3


# This script gets vmess config from vmess url


# Imports
import base64, time, json, sys


def printer(message: str) -> None:
    pretty_json = json.dumps(message, indent=4)
    for char in pretty_json:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

    print("\n")


def get_config(vmess_url):
    encoded_data = vmess_url.split("vmess://")[1].strip()
    output = json.loads(
        base64.b64decode(encoded_data).decode("utf-8").replace("'", '"')
    )
    return output


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
