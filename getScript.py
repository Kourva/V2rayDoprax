#!/usr/bin/env python3


# This Script gets CloudFlare worker script from your Doprax url


# Imports
import time, sys, re


# Script
script = """
addEventListener(

    "fetch", event => {

        let url = new URL(event.request.url);

        url.hostname = "target";

        url.protocol = "https";

        let request = new Request(url, event.request);

        event.respondWith(

            fetch(request)

        )
    }
)
"""


# Worker script
def worker_script(doprax):
    if "https://" in doprax:
        doprax = doprax.split("/")[2]
    temp = re.sub("target", doprax, script)
    return temp


# Run the program
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python getScript.py [arguments]

    create Script -> python getScript.py [Doprax url without 'https://' and '/' at the end]
    example: 
        python getScript.py test.eu-gacagfhs.dopraxrocks.net
"""
            )
        elif sys.argv[1]:
            for char in worker_script(sys.argv[1]):
                print(char, end="", flush=True)
                time.sleep(0.01)
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")


# EOF
