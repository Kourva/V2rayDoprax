#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Proxy cloner: Clone your proxy to many proxies
# Works with both vless & vmess proxies

# Imports
import random, base64, time, json, sys

# Vless cloner
def clone_vless(url: str) -> None:

    # Extract Vless URL information
    target = url.split("@")[1].split("?")[0]
    ipaddr, port = target.split(":")
    remark = url.split("#")[1]

    # Get all IP ranges from file
    with open("ip/all_result.txt", "r") as file:
        iplist = [
            random.choice(file.readlines()).split("\n")[0] for _ in range(20)
        ]

    # Create clones for vless urls
    clones = []
    for index, server in enumerate(iplist, start=1):
        tempvar = (
            url.replace(ipaddr, server)
            .replace(port, "443")
            .replace(remark, remark + "-" + str(index) + "\n\n")
        )
        clones.append(tempvar)

    # Save clones to results
    with open("data/vless_clones.txt", "a") as data:
        for clone in clones:
            data.write(clone)

# Vmess cloner
def clone_vmess(url: str) -> None:

    # Extract Vmess URL information
    encoded_data = url.split("vmess://")[1].strip()
    output = json.loads(
        base64.b64decode(encoded_data).decode("utf-8").replace("'", '"')
    )
    ipaddr, port, remark = (
        output["port"],
        output["add"],
        output["ps"],
    )

    # Get all IP ranges from file
    with open("ip/all_result.txt", "r") as file:
        all_servers = file.readlines()
        iplist = [random.choice(all_servers).split("\n")[0] for _ in range(20)]

    # Create clones for vmess urls
    clones = []
    for index, server in enumerate(iplist, start=1):
        temp = output
        temp["add"] = server
        temp["port"] = "443"
        temp["ps"] = remark + "-" + str(index)

        vmess_config = str(temp).encode("ascii")
        vmess_url = base64.b64encode(vmess_config).decode("ascii")
        result = "vmess://" + vmess_url + "\n\n"
        clones.append(result)

    # Save clones to results
    with open("data/vmess_clones.txt", "a") as data:
        for clone in clones:
            data.write(clone)
            
# Takes arguments
arguments = sys.argv

# Help message
help_message = """
Help: python clones.py [[-h] [-vl url] [-vm url]]
    -h/--help: Show this message and exit.
    -vl url  : Clone vless proxy
    -vm url  : Clone vmess proxy
"""

# Main
if __name__ == "__main__":
    if "-h" in arguments or "--help" in arguments:
        print(help_message)

    elif "-vl" in arguments:
        clone_vless(sys.argv[2])
        print("\033[2;34m* Proxies saved in data/vless_clones.txt\033[m\n")

    elif "-vm" in arguments:
        clone_vmess(sys.argv[2])
        print("\033[2;34m* Proxies saved in data/vmess_clones.txt\033[m\n")

    else:
        print("\033[2;31mError: Incorrect arguments! Use -h or --help\033[m")
