#!/bin/bash

# Check if a filename was provided as an argument
if [ $# -eq 0 ]; then
    echo "No filename provided. Please run the script with a filename as an argument."
    exit 1
fi

FILENAME=$1
OUTPUT_FILE="analyze_${FILENAME}.txt"
OBJDUMP_FILE="obj_dump_${FILENAME}.txt"
STRINGS_FILE="strings_${FILENAME}.txt"

# Check if the file exists
if [ ! -f "$FILENAME" ]; then
    echo "File not found. Please provide a valid filename."
    exit 1
fi

# Create or truncate the output files
> "$OUTPUT_FILE"
> "$OBJDUMP_FILE"
> "$STRINGS_FILE"

# Use tee to write to both the console and the output file
echo -e "\033[1;32mFile: $FILENAME\033[0m" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Determine file type and architecture
echo -e "\033[1;32mFile type and architecture:\033[0m" | tee -a "$OUTPUT_FILE"
file "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Run strings and save the output to a file
echo -e "\033[1;32mStrings:\033[0m" | tee -a "$OUTPUT_FILE"
strings "$FILENAME" > "$STRINGS_FILE"
echo "Output saved to $STRINGS_FILE" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Run strings with grep for CTF-related keywords
echo -e "\033[1;32mStrings with CTF-related keywords:\033[0m" | tee -a "$OUTPUT_FILE"
grep -iE 'root|flag|password|secret|key|token|admin|user|hide|hidden|encode|encrypt|decode|decrypt|shadow' "$STRINGS_FILE" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Disassemble the executable and display information about sections and symbols
echo -e "\033[1;32mObjdump:\033[0m" | tee -a "$OUTPUT_FILE"
objdump -d -h -t "$FILENAME" > "$OBJDUMP_FILE"
echo "Output saved to $OBJDUMP_FILE" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Display information about ELF headers, sections, and symbols
echo -e "\033[1;32mReadelf:\033[0m" | tee -a "$OUTPUT_FILE"
readelf -h -S -s "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# List the symbols from object files
echo -e "\033[1;32mNm:\033[0m" | tee -a "$OUTPUT_FILE"
nm -D "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Print shared library dependencies
echo -e "\033[1;32mLdd:\033[0m" | tee -a "$OUTPUT_FILE"
ldd "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Create a hex dump of the file
echo -e "\033[1;32mHex dump (first 16 lines):\033[0m" | tee -a "$OUTPUT_FILE"
xxd -l 256 "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Run binwalk
echo -e "\033[1;32mBinwalk:\033[0m" | tee -a "$OUTPUT_FILE"
binwalk "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Run binwalk -e
echo -e "\033[1;32mBinwalk -e:\033[0m" | tee -a "$OUTPUT_FILE"
binwalk -e "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

# Calculate the SHA-256 checksum of the file
echo -e "\033[1;32mSHA-256 checksum:\033[0m" | tee -a "$OUTPUT_FILE"
shasum -a 256 "$FILENAME" | tee -a "$OUTPUT_FILE"
echo "----------------------------" | tee -a "$OUTPUT_FILE"
echo | tee -a "$OUTPUT_FILE"

echo "All output saved to $OUTPUT_FILE"
