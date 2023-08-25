#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This tool will create Vmess proxies with popular servers

# Imports
import requests, base64, time, sys

# Printer
def printer(message: str) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# Gets servers
def get_servers() -> zip:
    names, addrs = [], []

    try:
        # Servers from Isegaro (https://twitter.com/iSegaro)
        for addrss, name in [
            ("isegaro.ddns.net", "Isegaro1"),
            ("ip.isegaro.click", "Isegaro2"),
        ]:
            addrs.append(addrss)
            names.append(name)

        # Other servers (You need more? run randomVmess.py)
        servers_list = [
            ("Atlanta.v2ray.online", "Altania"),
            ("Seattle.v2ray.online", "Seattle"),
            ("Helsinki.v2ray.online", "Helsinki"),
            ("Phoenix.v2ray.online", "Phoenix"),
            ("Vienna.v2ray.online", "Vienna"),
            ("Amsterdam.v2ray.online", "Amesterdam"),
            ("LosAngeles.v2ray.online", "LosAngeles"),
            ("Tokyo.v2ray.online", "Tokyo"),
        ]
        for addrss, name in servers_list:
            addrs.append(addrss)
            names.append(name)

        return zip(names, addrs)

    except Exception as ex:
        raise SystemExit(f"Can't get servers due to '{ex}'!")


# Vmess generator
def vmess_generator() -> list:

    # Open config file and extract config
    with open(sys.argv[1].strip(), "r") as config:
        lines = config.read().split("\n")

        worker = lines[1]
        doprax = lines[4]
        uuid = lines[7]
        path = lines[13]
        alias = lines[16]

    names, addrs, result = [], [], []

    # Make vmess urls
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
    with open("data/result.txt", "a") as result:
        for proxy in vmess_generator():
            result.write(proxy + "\n\n")
    printer("\033[2;34mResults saved in data/result.txt\033[m\n")

# Main
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python getVmess.py [arguments]
    create proxy -> python getVmess.py config.conf
    help message -> python getVmess.py -h/--help 
"""
            )
        elif sys.argv[1]:
            main()
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")
