param (
    [Parameter(Mandatory=$true)]
    [string]$username,
    
    [Parameter(Mandatory=$true)]
    [string]$hostname,
    
    [Parameter(Mandatory=$true)]
    [int]$port
)

# Prompt for the password securely
$password = Read-Host -AsSecureString "Enter password for $username@$hostname"

# Get current date and time
$currentDateTime = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

function Get-OS {
    param (
        [string]$hostname,
        [int]$port,
        [string]$username,
        [securestring]$password
    )

    $cred = New-Object System.Management.Automation.PSCredential ($username, $password)
    $session = New-SSHSession -ComputerName $hostname -Port $port -Credential $cred
    
    $os = (Invoke-SSHCommand -SSHSession $session -Command 'uname -s').Output
    Remove-SSHSession -SSHSession $session
    return $os
}

function Run-LinPEAS {
    param (
        [string]$hostname,
        [int]$port,
        [string]$username,
        [securestring]$password
    )
    
    $outputFile = "linpeas_output_$currentDateTime.txt"
    $cred = New-Object System.Management.Automation.PSCredential ($username, $password)
    $session = New-SSHSession -ComputerName $hostname -Port $port -Credential $cred
    
    $commands = @(
        "wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -O /tmp/linpeas.sh",
        "chmod +x /tmp/linpeas.sh",
        "/tmp/linpeas.sh | tee /tmp/linpeas_output.txt"
    )

    foreach ($command in $commands) {
        Invoke-SSHCommand -SSHSession $session -Command $command
    }
    
    $localPath = Join-Path -Path (Get-Location) -ChildPath $outputFile
    Copy-SSHItem -Path /tmp/linpeas_output.txt -Destination $localPath -SSHSession $session
    
    Remove-SSHSession -SSHSession $session
}

function Run-WinPEAS {
    param (
        [string]$hostname,
        [int]$port,
        [string]$username,
        [securestring]$password
    )
    
    $outputFile = "winpeas_output_$currentDateTime.txt"
    $cred = New-Object System.Management.Automation.PSCredential ($username, $password)
    $session = New-SSHSession -ComputerName $hostname -Port $port -Credential $cred
    
    $commands = @(
        "powershell.exe -Command `"Invoke-WebRequest -Uri https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEAS.bat -OutFile C:\Windows\Temp\winPEAS.bat; Start-Process C:\Windows\Temp\winPEAS.bat -NoNewWindow -Wait; Get-Content C:\Windows\Temp\winPEAS.bat -Raw | Out-File -FilePath C:\Windows\Temp\winpeas_output.txt`""
    )

    foreach ($command in $commands) {
        Invoke-SSHCommand -SSHSession $session -Command $command
    }
    
    $localPath = Join-Path -Path (Get-Location) -ChildPath $outputFile
    Copy-SSHItem -Path C:\Windows\Temp\winpeas_output.txt -Destination $localPath -SSHSession $session
    
    Remove-SSHSession -SSHSession $session
}

# Check if SSH is installed
if (-not (Get-Command ssh -ErrorAction SilentlyContinue)) {
    Write-Error "SSH is not installed. Please install SSH to use this script."
    exit 1
}

# Determine the OS of the remote machine
$os = Get-OS -hostname $hostname -port $port -username $username -password $password

# Execute the appropriate PEAS version based on the OS
if ($os -match "Linux") {
    Write-Host "Linux detected. Running linpeas..."
    Run-LinPEAS -hostname $hostname -port $port -username $username -password $password
} elseif ($os -match "MINGW|CYGWIN|Windows") {
    Write-Host "Windows detected. Running winpeas..."
    Run-WinPEAS -hostname $hostname -port $port -username $username -password $password
} else {
    Write-Error "Unsupported OS: $os"
    exit 1
}
