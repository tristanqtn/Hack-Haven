# JTR Cheatsheet

Reference: https://cheatsheet.haax.fr/passcracking-hashfiles/john_cheatsheet/

## Cracking Modes

```bash
# Dictionnary attack
./john --wordlist=password.lst hashFile

# Dictionnary attack using default or specific rules
./john --wordlist=password.lst --rules=rulename hashFile
./john --wordlist=password.lst --rules mypasswd

# Incremental mode
./john --incremental hashFile

# Loopback attack (password are taken from the potfile)
./john --loopback hashFile

# Mask bruteforce attack
./john --mask=?1?1?1?1?1?1 --1=[A-Z] hashFile --min-len=8

# Dictionnary attack using masks
./john --wordlist=password.lst -mask='?l?l?w?l' hashFile
```

## MISC & Tricks

```bash
# Show hidden options
./john --list=hidden-options

# Using session and restoring them
./john hashes --session=name
./john --restore=name
./john --session=allrules --wordlist=all.lst --rules mypasswd &
./john status

# Show the potfile
./john hashes --pot=potFile --show

# Search if a root/uid0 have been cracked
john --show --users=0 mypasswdFile
john --show --users=root mypasswdFile

# List OpenCL devices and get their id
./john --list=opencl-devices

# List format supported by OpenCL
./john --list=formats --format=opencl

# Using multiples GPU
./john hashes --format:openclformat --wordlist:wordlist --rules:rules --dev=0,1 --fork=2

# Using multiple CPU (eg. 4 cores)
./john hashes --wordlist:wordlist --rules:rules --dev=2 --fork=4
```

## Wordlists & Incremental

```bash
# Sort a wordlist for the wordlist mode
tr A-Z a-z < SOURCE | sort -u > TARGET

# Use a potfile to generate a new wordlist
cut -d ':' -f 2 john.pot | sort -u pot.dic

# Generate candidate password for slow hashes
./john --wordlist=password.lst --stdout --rules:Jumbo | ./unique -mem=25 wordlist.uniq
--incremental:Lower # 26 char
--incremental:Alpha # 52 char
--incremental:Digits # 10 char
--incremental:Alnum # 62 char

# Create a new charset
./john --make-charset=charset.chr

# Then set the following in the John.conf
# Incremental modes
[Incremental:charset]
File = $JOHN/charset.chr
MinLen = 0
MaxLen = 31
CharCount = 95

# Using a specific charset
./john --incremental:charset hashFile
```

## Rules

```bash
# Predefined rules
--rules:Single
--rules:Wordlist
--rules:Extra
--rules:Jumbo # All the above
--rules:KoreLogic
--rules:All # All the above
```

# RAR

```bash
/usr/share/john/rar2john file.rar > rar_hashes.txt
john --wordlist=passwords.txt rar_hashes.txt
```

# ZIP

```bash
/usr/share/john/zip2john file.rar > zip_hashes.txt
john --wordlist=passwords.txt zip_hashes.txt
```

# ZIP Using fcrackzip

```bash
/usr/share/john/fcrackzip -u -D -p rockyou.txt recup.zip
```

## SSH

```bash
/usr/share/john/ssh2john.py id_rsa > translate.txt
john --wordlist=/usr/share/wordlists/rockyou.txt translate.txt
```
