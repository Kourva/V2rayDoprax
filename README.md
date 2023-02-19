<p>
    <img align="left" src="https://i0.wp.com/img.aapks.com/imgs/c/9/5/c95d7d8f2388afd94a20fd5004105246_icon.png?w=140">
    <h1> V2rayDoprax v2 </h1>
    <p> V2ray is a tool to create thousands of Vless/Vmess proxies at ones! includes more tools... for Doprax </p>
</p>
<br>

# Features
+ About 27000 proxies
+ Vless proxy
+ Vmess proxy
+ UUID version 1 
+ UUID version 4
+ Worker Script
+ Worker check
+ Get vmess Config

# What's new in version 2?
+ Supports vmess proxy
+ Create vmess for Iran **(getVmess.py)**
+ Create random vmess **(randomVmess.py)**
+ Extract vmess config **(getConfig.py)**

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
[Path vless]
vless                                         <- This is default but you can change it
--------------------------------------------------------------------------------------
[Path Vmess]
vmess                                         <- This is default but you can change it
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
+ **getVmess.py**
```bash
Help: python getVmess.py [config]

    create proxy -> python getVmess.py config.conf
    help message -> python getVmess.py -h/--help 
```
+ **randomVmess.py**
```bash
Help: python randomVmess.py [config] [How many proxy]

    create proxy -> python randomVmess.py config.conf 10
    help message -> python randomVmess.py -h/--help 
```

# Needed tools
###### 1:  You need to fork this [repository](https://github.com/Kourva/V2ray-for-Doprax)
###### 2:  An E-mail Address for creating account
###### 3:  Account in [Doprax](https://www.doprax.com/)
###### 4:  Account in [CloudFlare](https://cloudflare.com)
###### 5:  Then you can work with this tool to create proxies 

# Tutorial (Persian)
Thanks to [Isegaro](https://twitter.com/iSegaro) for his greate tutorial and works.
Learn how to create Doprax & CloidFlare account and config it from [here](https://telegra.ph/Free-Hetzner-V2ray-with-iSegaro-01-30).

# FreeNode
Websites to get UUID:
+ [getafreenode](https://getafreenode.com)
+ [awesome tools](https://www.v2fly.org/en_US/awesome/tools.html)
<br>

<p>
    <img align="left" src="https://user-images.githubusercontent.com/118578799/219364816-7bb81cac-2cb5-4e52-bbc7-9bf907d016b1.png" width=140 height=140 />
    <h1> V2Paste </h1>
    <p><b> Create Vless/Vmess proxies via given config with this simple app in Android </b></p>
</p>
<br>
###### There is an android app to create vmess/vless proxy. you can check it out :]
###### V2Paste: https://github.com/Kourva/V2Paste
###### So I'm trying to work on both linux and android verions. Hope you enjoy

<br><br>
# Hope you enjoy :D
> Don't forget the star
