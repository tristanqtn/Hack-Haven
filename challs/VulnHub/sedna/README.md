# Sedna  - VulnHub

Reference: [Sedna](https://www.vulnhub.com/entry/hackfest2016-sedna,181/)

Level: Medium

# Enumeration

We will be starting this CTF by enumerating running services:

![](./images/nmap_1.png)
![](./images/nmap_2.png)

It seems like there's a webserver running on this VM so let's enumerate it with Nikto and Dirb.

![](./images/nikto.png)

The dirb scan didn't gave anything interesting. But thanks to the Nikto enumeration, we've found a /licence.txt file. In this [file](./license.txt) the engine powering the webserver is `BuilderEngine`. 

# Exploit

The exploit is pretty simple when using metasploit.

![](./images/msf_1.png)
![](./images/msf_2.png)
![](./images/exploit.png)
![](./images/flag_1.png)

# Escalation

I spent hours figuring out this escalation, and i found the solution with a the check root kit (chkrootkit). With metasploit once again the exploit is super simple.

![](./images/escalation.png)
![](./images/root.png)