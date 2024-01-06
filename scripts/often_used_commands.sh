# open a shell via python
python3 -c 'import pty;pty.spawn("/bin/bash")'
# to open a proper shell in a meterpreter
execute -f /bin/bash -i -a "-i"
# list files with root permissions
find / -perm -u=s -type f 2>/dev/null