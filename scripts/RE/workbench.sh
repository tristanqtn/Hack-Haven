#!/bin/bash

# Create backup and workbench directories if they don't exist
mkdir -p backup workbench workbench/analyze

# Move all files in the current folder to backup and workbench
# Exclude backup and workbench directories
find . -mindepth 1 \( -path ./backup -o -path ./workbench \) -prune -o -exec cp -t backup/ '{}' +
find . -mindepth 1 \( -path ./backup -o -path ./workbench \) -prune -o -exec mv -t workbench/ '{}' +

# If backup and workbench directories are empty, remove them
if [ ! -d backup ] || [ ! -z "$(ls -A backup)" ]; then
  rmdir backup
fi
if [ ! -d workbench ] || [ ! -z "$(ls -A workbench)" ]; then
  rmdir workbench
fi

# Copy RE_analyze.sh to workbench and make it executable
cp ~/Tools/Reverse/REAnalyze.sh workbench/
chmod +x workbench/REAnalyze.sh

rm backup/WorbenchSetUp.sh 

echo "All tasks have been completed successfully."
