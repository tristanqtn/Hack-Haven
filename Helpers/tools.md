# Tools

## Request Catcher

This tool lighter than Burp allows you to bring a live URL up and you can send some requests to it. The webpage of request catcher will then displays those requests. It's very handy when it comes to forwarding a flag to a public server. 

[Request Catcher](https://requestcatcher.com/)

## NMAP

Nmap (Network Mapper) is a powerful open-source network scanning tool used for network discovery and security auditing. It's widely used by penetration testers and network administrators to map out networks, find open ports, and discover vulnerabilities. Below are some of the most commonly used flags and their typical usage:

### Commonly Used Flags:

```bash
nmap TARGET_IP --flags
```

1. `-sS` or `--syn`

   - **Usage:** Perform SYN scan.
   - **Typical Usage:** Fast and stealthy scan to determine open ports.

2. `-sV`

   - **Usage:** Probe open ports to determine service/version information.
   - **Typical Usage:** Identify running services and their versions.

3. `-A`

   - **Usage:** Enable aggressive mode for deeper inspection and OS detection.
   - **Typical Usage:** Comprehensive scan for advanced information gathering.

4. `-p`

   - **Usage:** Specify port(s) to scan.
   - **Typical Usage:** Narrow down scanning to specific ports or port ranges.

5. `-O`

   - **Usage:** Enable OS detection.
   - **Typical Usage:** Identify the operating system of target hosts.

6. `-T`

   - **Usage:** Set timing template (0-5) for scan speed/stealth.
   - **Typical Usage:** Adjust scan speed according to network conditions and stealth requirements.

7. `-v`

   - **Usage:** Increase verbosity level.
   - **Typical Usage:** Obtain more detailed output during scanning.

8. `-oN`, `-oX`, `-oG`

   - **Usage:** Output scan results in normal, XML, or grepable format.
   - **Typical Usage:** Save scan results in different formats for further analysis.

9. `-script`
   - **Usage:** Execute NSE (Nmap Scripting Engine) scripts.
   - **Typical Usage:** Run specialized scripts for additional functionality such as vulnerability detection.

### Typical Usage of Nmap:

- **Network Discovery**: Identify live hosts and active services on a network.
- **Port Scanning**: Determine open ports and services running on those ports.
- **Service Enumeration**: Gather detailed information about running services and their versions.
- **Operating System Detection**: Determine the operating system of target hosts.
- **Vulnerability Assessment**: Identify potential vulnerabilities by scanning for known issues in services and configurations.

### When to Use Nmap in a Penetration Test:

1. **Reconnaissance Phase**: Use Nmap for initial reconnaissance to gather information about the target network.
2. **Enumeration Phase**: Identify live hosts, open ports, and running services to prepare for further exploitation.
3. **Vulnerability Assessment Phase**: Scan for vulnerabilities in services and configurations to exploit weaknesses.
4. **Post-Exploitation Phase**: Use Nmap to continue gathering information about the compromised network for further exploitation or privilege escalation.

Nmap is a versatile tool that provides valuable insights into network environments, making it an essential component of any penetration testing toolkit. Always ensure that you have proper authorization before conducting any penetration tests.

## Burp Suite

Burp Suite is a leading cybersecurity tool for web application security testing. It offers a range of features designed to help identify vulnerabilities in web applications. Below are some of the key features and functionalities along with their typical usage:

### Key Features:

1. **Proxy Intercept:**

   - **Usage:** Intercept and modify HTTP/S requests and responses between your browser and the target application.
   - **Typical Usage:** Analyze and manipulate web traffic to identify vulnerabilities such as XSS, SQLi, and CSRF.

2. **Scanner:**

   - **Usage:** Automated vulnerability scanner to identify common security issues in web applications.
   - **Typical Usage:** Discover vulnerabilities such as SQL injection, cross-site scripting (XSS), and insecure direct object references (IDOR).

3. **Intruder:**

   - **Usage:** Automated attack tool for performing customizable attacks against web applications.
   - **Typical Usage:** Test web application parameters and payloads for vulnerabilities such as brute force attacks, fuzzing, and injection attacks.

4. **Repeater:**

   - **Usage:** Manually manipulate and resend individual HTTP/S requests.
   - **Typical Usage:** Test the impact of parameter manipulation, input validation bypass, and other manual testing scenarios.

5. **Sequencer:**

   - **Usage:** Analyze the randomness and predictability of session tokens and other data.
   - **Typical Usage:** Assess the strength of session tokens and other randomness-dependent functionalities.

6. **Decoder:**

   - **Usage:** Decode and encode data formats such as Base64, URL, and hex.
   - **Typical Usage:** Analyze and manipulate encoded data within web requests and responses.

7. **Comparer:**

   - **Usage:** Compare two HTTP/S requests or responses to identify differences.
   - **Typical Usage:** Identify variations in application behavior based on different inputs or conditions.

8. **Extender:**
   - **Usage:** Customize and extend Burp Suite's functionality with custom-written plugins.
   - **Typical Usage:** Integrate additional features and tools into Burp Suite for specific testing requirements.

### Typical Workflow with Burp Suite:

1. **Configuration:**

   - Configure browser to use Burp Suite as a proxy.
   - Configure Burp Suite settings based on testing requirements.

2. **Proxy Intercept:**

   - Intercept requests and responses to analyze and manipulate web traffic.

3. **Scanner:**

   - Perform automated vulnerability scans to identify common security issues.

4. **Intruder:**

   - Perform targeted attacks against web application parameters and payloads.

5. **Repeater:**

   - Manually manipulate and resend individual requests for in-depth testing.

6. **Analysis and Reporting:**
   - Analyze findings, prioritize vulnerabilities, and generate comprehensive reports.

Burp Suite is an essential tool for web application security testing, offering a wide range of features to support various testing scenarios. It is widely used by penetration testers, security researchers, and web developers to identify and remediate security vulnerabilities in web applications.

## Metasploit

Metasploit Framework (`msfconsole`) is a powerful penetration testing tool used for exploiting vulnerabilities in various systems. It offers an extensive database of exploits, payloads, and auxiliary modules. Below is a guide on how to search for, use, set parameters, and run exploits within `msfconsole`.

### Searching for an Exploit:

To search for an exploit in Metasploit Framework, follow these steps:

1. Open `msfconsole` by typing `msfconsole` in your terminal.

2. Use the `search` command followed by a keyword to search for exploits. For example:

```bash
search <keyword>
```

3. Review the search results to find the exploit that matches your target system and vulnerability.

### Using an Exploit:

Once you've found the desired exploit, follow these steps to use it:

1. Note the name of the exploit you want to use from the search results.

2. Use the `use` command followed by the name of the exploit. For example:

```bash
use exploit/<exploit_name>
```

3. Set any required options using the `set` command. You can view the available options and their descriptions using the `show options` command.

4. Once all required options are set, you can run the exploit using the `exploit` command.

### Setting Parameters:

Many exploits require specific parameters to be set before they can be executed. Here's how to set parameters for an exploit:

1. Use the `show options` command after selecting the exploit to view the available parameters.

2. Use the `set` command followed by the parameter name and its value to set the required parameters. For example:

```bash
set RHOST <target_ip>
set RPORT <target_port>

```

3. Verify that all required parameters are correctly set using the `show options` command.

## Running the Exploit:

After setting all required parameters, you can run the exploit using the `exploit` command. For example:

```bash
exploit
```

Metasploit Framework provides a powerful arsenal of exploits for various systems and services, making it a valuable tool for penetration testers and security professionals.

## Mimikatz

Mimikatz is a powerful post-exploitation tool that allows users to extract plaintext passwords, hashes, PIN codes, and Kerberos tickets from memory, as well as perform pass-the-hash, pass-the-ticket, and overpass-the-hash attacks. Below are some common commands and their typical usage:

### Common Commands:

1. **`privilege::debug`**

   - **Usage:** Enable debug privilege to access and modify process memory.
   - **Typical Usage:** Gain access to process memory for extracting sensitive information.

2. **`sekurlsa::logonpasswords`**

   - **Usage:** Extract plaintext passwords and hashes from memory.
   - **Typical Usage:** Retrieve user credentials from memory for further exploitation.

3. **`sekurlsa::tickets`**

   - **Usage:** Extract Kerberos tickets from memory.
   - **Typical Usage:** Obtain Kerberos tickets for pass-the-ticket attacks.

4. **`sekurlsa::pth /user:<username> /domain:<domain> /ntlm:<ntlm_hash>`**

   - **Usage:** Perform pass-the-hash attack using NTLM hash.
   - **Typical Usage:** Authenticate to a system using extracted NTLM hash.

5. **`lsadump::sam`**

   - **Usage:** Dump SAM (Security Account Manager) database from the registry.
   - **Typical Usage:** Extract local user account information and password hashes.

6. **`lsadump::dcsync /domain:<domain> /user:<username>`**

   - **Usage:** Perform DCSync attack to extract password hashes from domain controller.
   - **Typical Usage:** Extract password hashes of domain users from domain controller.

### Typical Usage of Mimikatz:

1. **Credential Extraction:**

   - Use Mimikatz to extract plaintext passwords, hashes, and Kerberos tickets from memory.

2. **Pass-the-Hash Attack:**

   - Perform pass-the-hash attack using extracted NTLM hashes to authenticate to a system.

3. **Pass-the-Ticket Attack:**

   - Use extracted Kerberos tickets to perform pass-the-ticket attack for authentication.

4. **DCSync Attack:**

   - Perform DCSync attack to extract password hashes from domain controller.

Mimikatz is a powerful tool for post-exploitation activities, allowing penetration testers and security professionals to extract sensitive information from memory and perform various credential-based attacks. Always ensure that you have proper authorization before using Mimikatz in any testing or assessment scenarios.

## SQLMap

SQLMap is a popular open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities in web applications. It offers a wide range of features for identifying and exploiting SQL injection flaws. Below are some common commands and their typical usage:

### Common Commands:

1. **`-u` or `--url`**

   - **Usage:** Specify the target URL to test for SQL injection.
   - **Typical Usage:** Provide the URL of the web application to be tested.

2. **`-p` or `--param`**

   - **Usage:** Specify the parameter to be tested for SQL injection.
   - **Typical Usage:** Identify the parameter in the URL that is vulnerable to SQL injection.

3. **`--data`**

   - **Usage:** Specify the data to be sent via POST request for testing.
   - **Typical Usage:** Provide the POST data for testing SQL injection vulnerabilities.

4. **`--cookie`**

   - **Usage:** Specify the cookie to be used for the request.
   - **Typical Usage:** Provide the cookie value for authenticated testing.

5. **`--level`**

   - **Usage:** Set the level of tests to perform (1-5).
   - **Typical Usage:** Adjust the level of tests based on the complexity of the target application.

6. **`--risk`**

   - **Usage:** Set the risk of tests to perform (1-3).
   - **Typical Usage:** Adjust the risk level based on the potential impact of the tests.

7. **`--dbms`**

   - **Usage:** Specify the database management system to be tested.
   - **Typical Usage:** Identify the type of database used by the target application.

8. **`--dump`**

   - **Usage:** Dump the database contents to a file.
   - **Typical Usage:** Extract the contents of the database after successful exploitation.

### Typical Usage of SQLMap:

1. **URL Testing:**

   - Use SQLMap to test a target URL for SQL injection vulnerabilities.

2. **Parameter Identification:**

   - Identify the vulnerable parameter in the URL that is susceptible to SQL injection.

3. **POST Data Testing:**

   - Provide POST data for testing SQL injection vulnerabilities in web applications.

4. **Cookie-Based Testing:**

   - Use SQLMap to test for SQL injection vulnerabilities in authenticated sessions using cookies.

5. **Database Enumeration:**

   - Enumerate the database management system and extract database contents after successful exploitation.

SQLMap is a valuable tool for automating the process of identifying and exploiting SQL injection vulnerabilities in web applications. It is widely used by penetration testers and security professionals to assess the security of web applications and databases.

## Dirb

Dirb is a web content scanner used for discovering hidden directories and files on web servers. It is commonly used by penetration testers and security professionals to identify potential entry points and sensitive information within web applications. Below are some common commands and their typical usage:

### Common Commands:

1. **`-u` or `--url`**

   - **Usage:** Specify the target URL to scan for hidden directories and files.
   - **Typical Usage:** Provide the URL of the web application to be scanned.

2. **`-o` or `--output`**

   - **Usage:** Specify the output file to save the scan results.
   - **Typical Usage:** Save the scan results to a file for further analysis.

3. **`-r` or `--recursive`**

   - **Usage:** Enable recursive scanning of subdirectories.
   - **Typical Usage:** Perform a comprehensive scan of the target web server.

4. **`-X` or `--extensions`**

   - **Usage:** Specify file extensions to be scanned.
   - **Typical Usage:** Limit the scan to specific file types such as .php, .html, .asp, etc.

5. **`-S` or `--case`**

   - **Usage:** Enable case-sensitive scanning.
   - **Typical Usage:** Perform case-sensitive scanning for hidden directories and files.

6. **`-t` or `--timeout`**

   - **Usage:** Set the request timeout for scanning.
   - **Typical Usage:** Adjust the request timeout based on network conditions.

### Typical Usage of Dirb:

1. **URL Scanning:**

   - Use Dirb to scan a target URL for hidden directories and files.

2. **Output File:**

   - Save the scan results to a file for further analysis and reporting.

3. **Recursive Scanning:**

   - Enable recursive scanning to perform a comprehensive scan of the target web server.

4. **File Extension Filtering:**

   - Limit the scan to specific file types by specifying file extensions.

5. **Case-Sensitive Scanning:**

   - Perform case-sensitive scanning for hidden directories and files.

Dirb is a valuable tool for discovering hidden directories and files on web servers, providing valuable insights for penetration testers and security professionals. It is widely used to identify potential entry points and sensitive information within web applications.

# Nikto

Nikto is an open-source web server scanner used for identifying potential security vulnerabilities in web servers and web applications. It is commonly used by penetration testers and security professionals to perform comprehensive security assessments of web servers. Below are some common commands and their typical usage:

### Common Commands:

1.  **`-h` or `--host`**

    - **Usage:** Specify the target host to scan for vulnerabilities.
    - **Typical Usage:** Provide the IP address or domain name of the web server to be scanned.

2.  **`-p` or `--port`**

    - **Usage:** Specify the target port to scan for vulnerabilities.
    - **Typical Usage:** Identify the port number of the web server to be scanned.

3.  **`-ssl`**

    - **Usage:** Enable SSL scanning for HTTPS web servers.
    - **Typical Usage:** Perform comprehensive security assessments of HTTPS web servers.

4.  **`-o` or `--output`**

    - **Usage:** Specify the output file to save the scan results.
    - **Typical Usage:** Save the scan results to a file for further analysis and reporting.

5.  **`-Tuning`**

    - **Usage:** Enable tuning options for specific vulnerability checks.
    - **Typical Usage:** Customize the scan based on specific vulnerability checks and tuning options.

6.  **`-id` or `--id`**

        - **Usage:** Specify the scan ID to be used for tracking and reporting.
        - **Typical Usage:** Assign a unique scan ID for tracking and reporting purposes.

### Typical Usage of Nikto:

1.  **Host Scanning:**

    - Use Nikto to scan a target host for potential security vulnerabilities in web servers and web applications.

2.  **Port Identification:**

    - Identify the port number of the web server to be scanned.

3.  **SSL Scanning:**

    - Enable SSL scanning for comprehensive security assessments of HTTPS web servers.

4.  **Output File:**

    - Save the scan results to a file for further analysis and reporting.

5.  **Tuning Options:**

        - Customize the scan based on specific vulnerability checks and tuning options.

Nikto is a valuable tool for identifying potential security vulnerabilities in web servers and web applications, providing valuable insights for penetration testers and security professionals. It is widely used to perform comprehensive security assessments of web servers.

# John the Ripper

John the Ripper is a powerful password cracking tool used for identifying weak passwords and performing password audits. It is commonly used by penetration testers and security professionals to assess the strength of user passwords and identify potential security weaknesses. Below are some common commands and their typical usage:

### Common Commands:

1.  **`-wordlist`**

    - **Usage:** Specify the wordlist file to be used for password cracking.
    - **Typical Usage:** Provide a wordlist file containing potential passwords to be tested.

2.  **`-rules`**

    - **Usage:** Enable word mangling rules for password cracking.
    - **Typical Usage:** Apply word mangling rules to generate variations of potential passwords.

3.  **`-format`**

    - **Usage:** Specify the hash format of the password file.
    - **Typical Usage:** Identify the hash format of the password file to be cracked.

4.  **`-show`**

    - **Usage:** Display cracked passwords during the cracking process.
    - **Typical Usage:** View cracked passwords in real-time during the cracking process.

5.  **`-pot`**

    - **Usage:** Specify the pot file to save cracked passwords.
    - **Typical Usage:** Save cracked passwords to a pot file for further analysis and reporting.

6.  **`-incremental`**
    - **Usage:** Enable incremental mode for password cracking.
    - **Typical Usage:** Perform incremental password cracking to test various password lengths and character sets.

### Typical Usage of John the Ripper:

1.  **Wordlist Selection:**

    - Specify the wordlist file to be used for password cracking.

2.  **Word Mangling Rules:**

    - Enable word mangling rules to generate variations of potential passwords.

3.  **Hash Format Identification:**

    - Identify the hash format of the password file to be cracked.

4.  **Cracked Password Display:**

    - View cracked passwords in real-time during the cracking process.

5.  **Pot File Saving:**

    - Save cracked passwords to a pot file for further analysis and reporting.

6.  **Incremental Password Cracking:**
    - Perform incremental password cracking to test various password lengths and character sets.

John the Ripper is a versatile password cracking tool that provides valuable insights into the strength of user passwords and potential security weaknesses. It is widely used by penetration testers and security professionals to assess the security of user passwords.

# Hydra

Hydra is a powerful online password cracking tool used for performing brute force attacks against various online services. It is commonly used by penetration testers and security professionals to identify weak passwords and perform password audits. Below are some common commands and their typical usage:

### Common Commands:

1.  **`-l` or `--login`**

    - **Usage:** Specify the username or user list for the brute force attack.
    - **Typical Usage:** Provide the username or a list of usernames to be tested.

2.  **`-P` or `--password`**

    - **Usage:** Specify the password or password list for the brute force attack.
    - **Typical Usage:** Provide the password or a list of potential passwords to be tested.

3.  **`-t` or `--threads`**

        - **Usage:** Set the number of parallel threads for the brute force attack.
        - **Typical Usage:** Adjust the number of parallel threads based on network conditions and target service.

4.  **`-vV`**

    - **Usage:** Enable verbose mode for detailed output during the brute force attack.
    - **Typical Usage:** Obtain detailed output during the brute force attack for analysis and reporting.

5.  **`-o` or `--output`**

    - **Usage:** Specify the output file to save the scan results.
    - **Typical Usage:** Save the scan results to a file for further analysis and reporting.

6.  **`-f` or `--force`**

    - **Usage:** Enable brute force mode for the attack.
    - **Typical Usage:** Perform brute force attack to test potential passwords.

### Typical Usage of Hydra:

1.  **Username Selection:**

    - Specify the username or user list for the brute force attack.

2.  **Password Selection:**

    - Specify the password or password list for the brute force attack.

3.  **Thread Adjustment:**

    - Adjust the number of parallel threads based on network conditions and target service.

4.  **Verbose Mode:**

    - Enable verbose mode for detailed output during the brute force attack.

5.  **Output File:**

    - Save the scan results to a file for further analysis and reporting.

6.  **Brute Force Mode:**

    - Perform brute force attack to test potential passwords.

Hydra is a versatile online password cracking tool that provides valuable insights into the strength of user passwords and potential security weaknesses. It is widely used by penetration testers and security professionals to assess the security of online services.
