# V2rayDoprax
V2ray Vless tool to create thousands of vless proxies at ones! and more tools... for Doprax
+ About 27000 proxies
+ Vless proxy
+ UUID version 1 
+ UUID version 4
+ Worker Script
+ Worker check


# Installation
+ clone
```bash
git clone https://github.com/Kourva/V2rayDoprax && cd V2rayDoprax 
```
+ requirements
```bash
pip install requests beautifulsoup4
```

# Tutorial (Persian) by Isegaro
Big thanks to Isegaro for his tutorial and works.
Learn how to create Doprax & CloidFlare account and config it from [here](https://telegra.ph/Free-Hetzner-V2ray-with-iSegaro-01-30).


# Usage
+ **config.conf**
```config
[Worker]
https://test.example.workers.dev/                      <- Your CloudFlare address here
--------------------------------------------------------------------------------------
[Doprax]
example.eu-sadgfhs.dopraxrocks.net                     <- Your Doprax app Adreess here
--------------------------------------------------------------------------------------
[UUID]
F4C....                                                              <- Your UUID here
--------------------------------------------------------------------------------------
[path]
vless                                         <- This is default but you can change it
--------------------------------------------------------------------------------------
[Alias]
test                                                              <- Alias for proxies
--------------------------------------------------------------------------------------
```
+ **check_worker.py**
```bash
Help: python check_worker [url]

Where url looks like:
    https://example.workers.dev
```
+ **getAllIPs.py**
```bash
Help: python getAllIPs.py [arguments]

    for save the IPs -> python getAllIPs.py -s
    for help message -> python getAllIPs.py [-h, --help]
```
+ **getIP.py**
```bash
Help: python getIP.py [arguments]

    for only get IPs -> python getIP.py
    for save the IPs -> python getIP.py -s
    for help message -> python getIp.py [-h, --help] 
 ```
 + **getScript.py**
```bash
Help: python getScript.py [arguments]

    create Script -> python getScript.py [Doprax url without 'https://' and '/' at the end]
    example: 
        python getScript.py test.eu-gacagfhs.dopraxrocks.net
```








