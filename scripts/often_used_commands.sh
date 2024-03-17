# open a shell via python
python3 -c 'import pty;pty.spawn("/bin/bash")'

# to open a proper shell in a meterpreter (Linux)
execute -f /bin/bash -i -a "-i"

# obtain sudo permissions
sudo -l

# list files with root permissions
find / -perm -u=s -type f 2>/dev/null

# search for a file
find ./ -type f -name "file.txt"

# search for a string in a file
grep -r "string" /path/to/search

# search for a string in a file and ignore case
grep -r -i "string" /path/to/search

# Check rights, cron tasks, env variables, writable files of the current user:

whoami
id
sudo -l
sudo su
ps aux | grep root
find /etc/ -writable -type f 2>/dev/null
crontab -l; ls -alh /var/spool/cron; ls -al /etc/ | grep cron; ls -
cat /etc/profile; cat /etc/bashrc; cat ~/.bash_profile; cat ~/.bashrc; cat ~/.bash_logout; env;

# Check for Kernel vulnerabilities:

uname -a
cat /etc/issue
cat /etc/*-release
cat /proc/version

# SUID and GUID files:

find / -perm -4000 -type f 2>/dev/null
find / -perm -2000 -type f 2>/dev/null
