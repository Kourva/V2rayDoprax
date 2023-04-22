#!/usr/bin/env python3


# This tool will create random Vless proxies with random servers


# Imports
import requests, string, random, time, sys


# Random server name generator
def random_name() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=6))


# Gets servers
def get_servers():
    names = []
    addrs = []

    # Servers from database
    with open("ip/all_result.txt") as data:
        targets = [url.split("\n")[0] for url in data.readlines()]
        for i in range(int(sys.argv[2])):
            addrs.append(targets[random.randint(0, len(targets) - 1)])
            names.append(random_name())

        return zip(names, addrs)

    raise SystemExit("Can't get servers")


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
    with open("data/random_result.txt", "a") as result:
        for proxy in vless_generator():
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
Help: python randomVless.py [config] [How many proxy]

    create proxy -> python randomVless.py config.conf 10
    help message -> python randomVless.py -h/--help 
"""
            )
        elif sys.argv[1]:
            main()
        else:
            print("Invalid argument! run with -h")
    else:
        print("No argument! run with -h")


# EOF
