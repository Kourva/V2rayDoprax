#!/usr/bin/env python3


# This tool will create Vless proxies with popular servers


# Imports
import requests, time, sys


# Gets servers
def get_servers():
    names = []
    addrs = []

    # Servers from sudoer.net
    respones = requests.get("http://bot.sudoer.net/best.cf.iran")
    if respones.status_code == 200:
        for server in respones.text.split("\n"):
            try:
                names.append(server.split()[0])
                addrs.append(server.split()[1])
            except:
                continue

        # Servers from Isegaro : Thank you so much for your help <3
        # Follow him on Twitter: https://twitter.com/iSegaro
        for addrss, name in [
            ("isegaro.ddns.net", "Isegaro1"),
            ("ip.isegaro.click", "Isegaro2"),
        ]:
            addrs.append(addrss)
            names.append(name)

        # Other servers (You need more? run randomVless.py)
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
    raise SystemExit("Can't get servers!")


# Vless generator
def vless_generator():
    with open(sys.argv[1].strip(), "r") as config:
        lines = config.read()

        worker = lines.split("\n")[1]
        doprax = lines.split("\n")[4]
        uuid = lines.split("\n")[7]
        path = lines.split("\n")[10]
        alias = lines.split("\n")[16]

    vless_url = "vless://{uuid}@{addrs}:443?encryption=none&security=tls&sni={worker_host}&alpn=http%2F1.1&type=ws&host={worker_host}&path={path}#{alias}"
    names, addrs = [], []
    result = []

    worker_host = worker.split("/")[2]
    for name, addrs in get_servers():
        result.append(
            vless_url.format(
                uuid=uuid,
                addrs=addrs,
                worker_host=worker_host,
                path=path,
                alias=alias + "-" + name,
            )
        )
    return result


# Main function
def main():
    with open("data/result.txt", "a") as result:
        for proxy in vless_generator():
            result.write(proxy + "\n\n")
    for char in "\033[2;34mResults saved in data/result.txt\033[m\n":
        print(char, end="", flush=True)
        time.sleep(0.01)


# Run the program
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python getVless.py [arguments]

    create proxy -> python getVless.py config.conf
    help message -> python getVless.py -h/--help 
"""
            )
        elif sys.argv[1]:
            main()
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")


# EOF
