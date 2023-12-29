```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nmap 172.20.10.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-25 15:55 CET
Nmap scan report for 172.20.10.1
Host is up (0.0063s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
21/tcp    open  ftp
53/tcp    open  domain
49152/tcp open  unknown
62078/tcp open  iphone-sync

Nmap scan report for 172.20.10.3
Host is up (0.013s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT      STATE SERVICE
49152/tcp open  unknown
62078/tcp open  iphone-sync

Nmap scan report for 172.20.10.4
Host is up (0.00074s latency).
All 1000 scanned ports on 172.20.10.4 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap scan report for 172.20.10.6
Host is up (0.0012s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 256 IP addresses (4 hosts up) scanned in 5.56 seconds
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nmap -A 172.20.10.6
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-25 15:56 CET
Nmap scan report for 172.20.10.6
Host is up (0.0024s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 8d:53:65:83:52:52:c4:12:72:49:be:33:5d:d1:e7:1c (RSA)
|   256 06:61:0a:49:86:43:64:ca:b0:0c:0f:09:17:7b:33:ba (ECDSA)
|_  256 9b:8d:90:47:2a:c1:dc:11:28:7d:57:e0:8a:23:b4:69 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Hacked By Red &#8211; Your site has been Hacked! You\xE2\x80\x99ll neve...
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 1 disallowed entry
|_/wp-admin/
|_http-generator: WordPress 5.8.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.24 seconds
```
