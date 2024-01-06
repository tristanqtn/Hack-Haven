# CTF Content & Tools

In this repository, you'll find a comprehensive table documenting various Capture The Flag (CTF) challenges I've completed and uploaded. For each CTF, I provide detailed insights into the tools I utilized and their specific purposes. The table serves as a valuable reference to understand the toolkit employed in each challenge, facilitating a transparent and informative overview of the techniques applied. Explore the README files linked in the table to delve into the specifics of each CTF, gaining insights into the tools employed and their roles in overcoming the challenges.

## Try Hack Me

| README Link                                        | NMAP        | DIRB/NIKTO  | BURP                                  | Metasploit             | SQLMap | Hydra                   | John                    | Reverse                                                  | Escalation                            |
| -------------------------------------------------- | ----------- | ----------- | ------------------------------------- | ---------------------- | ------ | ----------------------- | ----------------------- | -------------------------------------------------------- | ------------------------------------- |
| [Mr Robot](./try_hack_me/mr_robot/)                | recognition | recognition | to obtain WP requets format fro login |                        |        | to brute force WP login | hash translation        | upload a php reverse shell script to WP apperance editor | escalation with nmap running as root  |
| [Pickle Rick](./try_hack_me/pickle_rick/README.md) | recognition | recognition |                                       |                        |        |                         |                         | creating a python reverse shell                          |                                       |
| [Root Me ](./try_hack_me/rootme/README.md)         | recognition | recognition |                                       |                        |        |                         |                         | upload a php5 reverse shell script into an open deposit  | esclation with python running as root |
| [Tom Ghost](./try_hack_me/tomghost/README.md)      | recognition | recognition |                                       | use AJP Tomcat exploit |        |                         | PGP message translation | SSH                                                      | escalation with 7ZIP running as root  |

## VulnHub

| README Link                             | NMAP        | DIRB/NIKTO  | BURP | Metasploit                      | SQLMap | Hydra | John                                     | Reverse                                               | Escalation                                      |
| --------------------------------------- | ----------- | ----------- | ---- | ------------------------------- | ------ | ----- | ---------------------------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| [Earth](./vuln_hub/earth/README.md)     | recognition | recognition |      |                                 |        |       | CyberChief and John for message decoding | NetCat                                                | with a reset root password missing dependencies |
| [Sedna](./vuln_hub/sedna/README.md)     | recognition | recognition |      | Builder Engine Exploit          |        |       |                                          |                                                       | Metasploit exploit with chkrootkit              |
| [Thales](./vuln_hub/thales_1/README.md) | recognition | recognition |      | Gaining access to Tomcat Server |        |       | RSA key decryption                       | upload a php5 reverse shell script into Apache Server |                                                 |
