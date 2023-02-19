#!/usr/bin/env python3


# This tool will create random Vmess proxies with random servers


# Imports
import requests
import string
import random
import base64
import time
import sys


# Random server name generator
def random_name() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=6))


# Gets servers
def get_servers():
    names = []
    addrs = []

    # Servers from sudoer.net
    respones = requests.get("http://bot.sudoer.net/result.cf")
    if respones.status_code == 200:
        targets = respones.text.strip().split("\n")
        for i in range(int(sys.argv[2])):
            addrs.append(targets[random.randint(0, len(targets) - 1)])
            names.append(random_name())

        return zip(names, addrs)

    raise SystemExit("Can't get servers")


# Vmess generator
def vmess_generator():
    with open(sys.argv[1].strip(), "r") as config:
        lines = config.read()

        worker = lines.split("\n")[1]
        doprax = lines.split("\n")[4]
        uuid = lines.split("\n")[7]
        path = lines.split("\n")[13]
        alias = lines.split("\n")[16]

    names, addrs = [], []
    result = []

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
    return result


# Main function
def main():
    with open("data/random_result.txt", "a") as result:
        for proxy in vmess_generator():
            result.write(proxy + "\n\n")
    for char in "\033[2;34m{} Servers saved in data/random_result.txt\033[m\n".format(
        int(sys.argv[2])
    ):
        print(char, end="", flush=True)
        time.sleep(0.01)


# Run the program
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


# EOF
