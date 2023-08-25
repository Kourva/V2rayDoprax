#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Get free random proxies from 'yebekhe's scanner'

# Imports
import random, requests, time, sys

# Printer
def printer(message: str) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# Get random free v2ray configs
def V2ray_Proxies(length: int) -> None:
    try:
        length = 20 if length > 20 else length

        # Base url to request
        base_url = f"https://raw.githubusercontent.com/yebekhe/ConfigCollector/main/json/configs.json?v1.{int(time.time())}"

        # Make request to fetch proxies
        response = requests.get(base_url).json()

        # Get random proxies from main result
        random_proxies = random.choices(response, k=length)

        # Return true and proxy list in success
        if random_proxies:
            with open("data/free_v2ray.txt", "a") as data:
                for proxy in random_proxies:
                    data.write(proxy['config'] + "\n")
            printer(f"\33[2;32m{length} Proxies saved to data/free_v2ray.txt!\33[m")

    # Handle exception and raise SystemError
    except Exception as ex:
        raise SystemExit(f"\33[2;31mError due to {ex}\33[m")

# Main
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python freeV2ray.py [arguments]
    get free proxies -> python freeV2ray.py 2
    help message     -> python freeV2ray.py -h/--help 
                """.strip()
            )
        elif sys.argv[1].isnumeric():
            V2ray_Proxies(int(sys.argv[1]))
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")