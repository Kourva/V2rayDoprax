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
+ **getUUID.py**
```bash
Help: python getUUID.py [[-h] [-v1] [-v4]]
    -h  : Show this message and exit.
    -v1 : get version 1 UUID
    -v4 : get version 4 UUID

* What is a Version 1 UUID?
    A Version 1 UUID is a universally unique identifier that 
    is generated using a timestamp and the MAC address of 
    the computer on which it was generated.

* What is a version 4 UUID?
    A Version 4 UUID is a universally unique identifier that 
    is generated using random numbers.using a secure random 
    number generator.
```
+ **getVless.py**
```bash
Help: python getVless.py [arguments]

    create proxy -> python getVless.py config.conf
    help message -> python getVless.py -h/--help
```
+ **randomVless.py**
```bash
Help: python randomVless.py [config] [How many proxy]

    create proxy -> python randomVless.py config.conf 10
    help message -> python randomVless.py -h/--help 
```

# Needed tools
###### 1:  You need to fork this [repository](https://github.com/Kourva/V2ray-for-Doprax)
###### 2:  An E-mail Address for creating account
###### 3:  Account in [Doprax](https://www.doprax.com/)
###### 4:  Account in [CloudFlare](https://cloudflare.com)

##### Tutorial (Persian)
Big thanks to Isegaro for his tutorial and works.
Learn how to create Doprax & CloidFlare account and config it from [here](https://telegra.ph/Free-Hetzner-V2ray-with-iSegaro-01-30).

##### FreeNode
Websites to get UUID:
+ [getafreenode](https://getafreenode.com)
+ [awesome tools](https://www.v2fly.org/en_US/awesome/tools.html)

# Screenshots
###### You can download V2rayN app from their official [Github](github.com/2dust/v2rayN) account.
![V2rayN](https://user-images.githubusercontent.com/118578799/218227327-dcdbb6ab-2a76-44b7-9400-55b9f65f86f1.png)
###### You can create so many proxies each day. tested download speed is about 0.5 Mb/s
![terminal](https://user-images.githubusercontent.com/118578799/218227440-012640e1-50fd-4b6d-a2a2-19d3ec15a7ba.png)

<br><br>
# Hope you enjoy :D
> Don't forget the star
