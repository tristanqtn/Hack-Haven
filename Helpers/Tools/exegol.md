# Exegol Cheat Sheet

## Description

Exegol is a hacking environment that enables users to launch a variety of hacking tools and scripts. It is a lightweight, portable, and easy-to-use hacking environment that can be run on any system with Docker installed.

## Installation

### Prerequisites

> [!IMPORTANT]  
> Ensure that you have the following prerequisites installed on your system before installing Exegol:

- Git (Linux | macOS | Windows)
- Python3 (Linux | macOS | Windows) with pipx
- Docker (Linux) or Docker Desktop (macOS | Windows)
- At least 100GB of free storage recommended (a minimum of 20GB could be enough, but only for the light image).

#### Docker Setup for Linux

> [!TIP]  
> You can install Docker on Linux by running the following commands:
>
> ```bash
> curl -fsSL "https://get.docker.com/" | sh
> ```

> [!WARNING]  
> By default, sudo will be required when running Docker, hence needed as well for Exegol. For security reasons, it should stay that way, but it’s possible to change that. In order to run Exegol from the user environment without sudo, the user must have the appropriate rights. You can use the following command to grant them to the current user:
>
> ```bash
> # add the sudo group to the user
> sudo usermod -aG docker $(id -u -n)
> # "reload" the user groups with the newly added docker group
> newgrp docker
> ```
>
> For more information, official Docker documentation shows [how to manage docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

#### Docker Desktop Setup for Windows

To support graphical applications (display sharing functionality, e.g. Bloodhound, Wireshark, Burp, etc.), additional dependencies and configuration are required:

- Windows 10 (up to date), or Windows 11, is required
- Docker Desktop installed on the Windows host
- Docker Desktop must be configured to run on WSL2 engine ([how to](https://learn.microsoft.com/en-us/windows/wsl/install))
- WSLg must be installed to support graphical applications
- At least one WSL distribution must be installed as well (e.g. Debian), with Docker integration enabled (see screenshot below)

> [!WARNING]  
> Microsoft Defender may block the installation of Exegol, you should add some exclusion path to Windows security settings (Windows Security > Protection against virus and threats > Manage settings > Add or remove exclusions > Add an exclusion > Folder).

> Path to add as exclusion: `C:\Users\<user>\.exegol\` and `C:\Users\<user>\<path>\Exegol\`

### Installation Steps

Exegol can be installed with `pip` or `pipx`, but I prefer the source installation method to manage the installation by myself.

1. Clone the Exegol repository from GitHub:

   ```bash
   git clone "https://github.com/ThePorgs/Exegol"
   ```

   > [!TIP]  
   > You can also download the repository in a lighter version if you don't want to contribute:
   >
   > ```bash
   > git clone --shallow-since="2023/05/08" "https://github.com/ThePorgs/Exegol"
   > ```

#### Windows Specificity

Windows may format the shell script needed by Exegol container's. In order to correct this, format them back into proper Unix format with the following command:

```bash
dos2unix Exegol/exegol/utils/imgsync/*.sh
```

2. Change the directory to the Exegol folder:

   ```bash
   cd Exegol
   ```

3. Install the dependencies:

   ```bash
   python3 -m pip install --user --requirement "requirements.txt"
   ```

4. Add the Exegol directory to the PATH:

#### Linux

Once this is taken care of, the Exegol wrapper can then be added to the PATH with a symlink for direct access. This allows calling Exegol from wherever, instead of using the absolute path. Exegol can then be used with `exegol <action>` instead of `python3 /path/to/Exegol/exegol.py <action>`.

```bash
sudo ln -s "$(pwd)/exegol.py" "/usr/local/bin/exegol"
```

#### Windows

To create the alias file correctly, open a PowerShell and place yourself in the folder where Exegol is located (applicable only for from-source installations) and run the following commands:

**Create $PROFILE file if it doesn’t exist:**

```powershell
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
```

**Create alias for Exegol in $PROFILE:**

```powershell
# add the alias to the $PROFILE
Set-Alias -Name exegol -Value 'C:\Users\<path>\exegol.py'
```

5. Installation of the first image:

   ```bash
   exegol install
   ```

**Exegol is now installed and ready to use!**

## Usage

- Install an Exegol image: `exegol install`
- List available images: `exegol info`
- Start Exegol image: `exegol start`
- Stop Exegol image: `exegol stop`
- Remove Exegol image: `exegol remove`
- Update Exegol image: `exegol update`

**Often used commands:**

```bash
exegol info <container_name> # retrieve information about the container

exegol install <image_name> # install a specific image

exegol start <container_name> <image_name> --desktop # start a container with a graphical interface
```

**File sharing:**

Exegol automatically binds the folders `/opt/resources` and `/opt/my-resources` with the host machine. This allows sharing files between the host and the container. The `/opt/resources` folder is read-only, while the `/opt/my-resources` folder is read-write.

If you want to share some files between the host and the container, you can place them in the `/workspace` folder.

**Graphical interface:**

The `--desktop` option allows running Exegol with a graphical interface. This option is required to run graphical applications (e.g. Bloodhound, Wireshark, Burp, etc.).
