#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This tool will create random Vmess proxies with random servers

# Imports
import requests, string, random, base64, time, sys

# Printer
def printer(message: str) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# Random server name generator
def random_name() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=6))

# Gets servers
def get_servers() -> zip:
    names = []
    addrs = []

    try: 
        # Get servers from database
        with open("ip/all_result.txt") as data:
            targets = [url.split("\n")[0] for url in data.readlines()]
            for i in range(int(sys.argv[2])):
                addrs.append(targets[random.randint(0, len(targets) - 1)])
                names.append(random_name())

            return zip(names, addrs)
    
    # Handle exceptions
    except Exception as ex:
        raise SystemExit(f"Can't get servers due to '{ex}' (run with -h)!")

# Vmess generator
def vmess_generator() -> list:

    # Get config file and extract config
    with open(sys.argv[1].strip(), "r") as config:
        lines = config.read().split("\n")

        worker = lines[1]
        doprax = lines[4]
        uuid = lines[7]
        path = lines[13]
        alias = lines[16]

    names, addrs, result = [], [], []

    # Make vless proxies
    worker_host = worker.split("/")[2]
    for name, addrs in get_servers():
        vmess_config = {
            "v": "2",
            "ps": alias + "-" + name,
            "add": addrs,
            "port": "443",
            "id": uuid,
            "aid": "0",
            "net": "ws",
            "type": "none",
            "host": worker_host,
            "path": path,
            "tls": "tls",
            "alpn": "http/1.1",
            "sni": worker_host,
            "utls": "chrome",
        }
        message = str(vmess_config).encode("ascii")
        vmess_url = base64.b64encode(message).decode("ascii")
        result.append("vmess://" + vmess_url)

    # Return result
    return result

# Main function
def main():
    with open("data/random_result.txt", "a") as result:
        for proxy in vmess_generator():
            result.write(proxy + "\n\n")
    printer(
        f"\033[2;34m{int(sys.argv[2])} Servers saved in data/random_result.txt\033[m\n"
    )

# Main
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python randomVmess.py [config] [How many proxy]

    create proxy -> python randomVmess.py config.conf 10
    help message -> python randomVmess.py -h/--help 
"""
            )
        elif sys.argv[1]:
            main()
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")
