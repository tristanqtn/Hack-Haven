# WrapPeas Scripts

The goal of this tool is to automate the PrivEsc vulnerabilities on a remote machine. This tool should be used in a defensive way in order to patch you servers and bring there security to the next level.

This repository contains two wrapper scripts for the PEAS (Privilege Escalation Awesome Scripts) tool. These scripts automate the process of connecting to a remote machine via SSH, determining the operating system, and downloading and executing the appropriate PEAS script.

## Scripts

1. **WrapPeas.sh**: A Bash script that uses SSH with username and password for authentication.
2. **WrapPeas.ps1**: A PowerShell script that uses SSH with username and password for authentication.

## Prerequisites

### For `wrappeas.sh`

- `sshpass`: A non-interactive ssh password authentication utility.
- `ssh`: OpenSSH client for connecting to remote machines.
- Internet connection on the remote machine to download the PEAS scripts.

### For `wrappeas.ps1`

- PowerShell with SSH module installed. You can install the SSH module using the following command:
  ```powershell
  Install-Module -Name SSH-Sessions -Force
  ```
- Internet connection on the remote machine to download the PEAS scripts.

## Usage

### wrappeas.sh

This script connects to a remote machine using SSH with username and password, determines the operating system, and runs the appropriate PEAS script.

#### Parameters

- `-u`: Username for SSH login.
- `-h`: Hostname or IP address of the remote machine.
- `-p`: SSH port of the remote machine.
- `-w`: Password for SSH login.

#### Example

```bash
chmod +x wrappeas.sh
./wrappeas.sh -u username -h hostname -p 22 -w password
```

### wrappeas.ps1

This script connects to a remote machine using SSH with username and password, determines the operating system, and runs the appropriate PEAS script.

#### Parameters

- `-username`: Username for SSH login.
- `-hostname`: Hostname or IP address of the remote machine.
- `-port`: SSH port of the remote machine.

#### Example

```powershell
.\wrappeas.ps1 -username your_username -hostname your_hostname -port 22
```

Upon execution, the script will prompt you to enter the password securely.

## How It Works

1. **Connection**: The script establishes an SSH connection to the specified remote machine.
2. **OS Detection**: It runs the `uname -s` command on the remote machine to detect the operating system.
3. **Download and Execute**: Based on the detected operating system, the script downloads the appropriate PEAS script (`linpeas.sh` for Linux or `winPEAS.bat` for Windows) and executes it.

## Notes

- Ensure that the remote machine has internet access to download the PEAS scripts.
- The scripts assume the availability of necessary tools (`wget`, `powershell`, etc.) on the remote machine.
- For the `wrappeas.sh` script, ensure `sshpass` is installed on your local machine.
- For the `wrappeas.ps1` script, ensure you have the SSH module installed in PowerShell.

## Disclaimer

Use these scripts responsibly and only on systems for which you have explicit permission to perform security testing.
