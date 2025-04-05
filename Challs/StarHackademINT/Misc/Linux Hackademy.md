# Linux Hackademy : SSH

This super simple challenge explains you how to connect using SSH to a distant device : 

```powershell
ssh kittycat@challenges.hackademint.org -p 30022
```

Then by using some basic linux commands you can read the flag : 

``` bash
kittycat@linux-hackademy-6b4545cb6f-gw49h:~$ ls
flag.txt
kittycat@linux-hackademy-6b4545cb6f-gw49h:~$ cat flag.txt
Star{1sn7_mY_c@t_k@wA1ii1???}
```

# Linux Hackademy : Fichier Caché 

```bash
cachecache@linux-hackademy-6b4545cb6f-2fg6z:~$ ls
cachecache@linux-hackademy-6b4545cb6f-2fg6z:~$ ls -a
.  ..  .bash_logout  .bashrc  .flag.txt  .profile
cachecache@linux-hackademy-6b4545cb6f-2fg6z:~$ cat .flag.txt
Star{H0_nO_17_W@s_s0o0o0_w311_H1D3n_bUt_I_f0und_17}
```
# Linux Hackademy : Manual

In bash the console has a manual  containing the documentation of each command. The pitch of the challenge let us understand that we should look into the manual for the command `manflag` : 

```bash
kthxman@linux-hackademy-6b4545cb6f-2fg6z:~$ manflag
"Hummm... There isn't much here. Maybe check the man page for this command?"
kthxman@linux-hackademy-6b4545cb6f-2fg6z:~$ man manflag
```

```plaintext

manflag(1)                       General Commands Manual                       manflag(1)

NAME
       manflag

       What is this command? Well, it is pretty useless, but it had the benefit of making
       you use man!  man is the system's manual, it is super useful! Whenever  you  don't
       know how to use a tool, you can look at its man page, and learn about it.

       E.g. to learn about the options for ls:
       man ls

FLAG
       Ok, I guess you are here for the flag, right?  Here you go:

       Star{M@n_1z_l1k3_@_sUp3r_POwEr_f0r_7hOz3_wh0_r3memb3R_tO_uzE_1t}

COPYRIGHT
       Nahhh, no copyright here.

CREDITS
       Manpage by Smyler

                                                                               manflag(1)
```
# Linux Hackademy : Find

Thanks to the challenge pitch we know the exact size of the desired file : `54 octets`. So by using some basic find command we find the flag very easily : 

```bash
oukilest@linux-hackademy-6b4545cb6f-s7q28:~$ ls
a  b  c  d  e  f  flag.txt  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
oukilest@linux-hackademy-6b4545cb6f-s7q28:~$ find * -type f -size 54c
s/t/a/flag.txt
oukilest@linux-hackademy-6b4545cb6f-s7q28:~$ cat s/t/a/flag.txt
Star{F1nD_1z_sUp3r_p0weRful_bU7_1t_isNt_7h3_onLy_w@y}
```
# Linux Hackademy : Sudo

After SSHing into the remote device, we enumerate the privileges of our current session using `sudo -l` : 

```bash
suuuudoo@linux-hackademy-6b4545cb6f-h8gkl:~$ sudo -l
[sudo] password for suuuudoo:
Matching Defaults entries for suuuudoo on linux-hackademy-6b4545cb6f-h8gkl:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User suuuudoo may run the following commands on linux-hackademy-6b4545cb6f-h8gkl:
    (sudoku : sudoku) ALL
```

The last line of our privileges means that we can change our current session (`suuuudoo`) to session `sudoku` without entering any password. Thus we can obtain the flag stored in the sudoku home directory : 

```bash
suuuudoo@linux-hackademy-6b4545cb6f-h8gkl:~$ sudo -u sudoku -i
sudoku@linux-hackademy-6b4545cb6f-h8gkl:~$ ls
flag.txt
sudoku@linux-hackademy-6b4545cb6f-h8gkl:~$ cat flag.txt
Star{SUd0_1z_n07_@lOn3_th3rE_1z_@lz0_rUn0_4nd_d0aS}
```