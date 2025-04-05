# Reverse Engineering Toolkit

This Docker image provides a comprehensive environment for reverse engineering tasks, including tools and automation scripts for analyzing ELF and PE files.

## Features

- **Tools Included**:

  - **Ghidra**: A powerful reverse engineering tool.
  - **IDA Free**: Interactive disassembler for static analysis.
  - **Binwalk**: Firmware analysis tool.
  - **strace/ltrace**: Trace system and library calls.
  - **Capstone & Keystone**: Disassembly and assembly frameworks.

- **Automation Scripts**:
  - `parse_elf.py`: Parse and dump sections from ELF binaries.
  - `parse_pe.py`: Parse and dump sections from PE binaries.

## Setup Instructions

### 1. Build the Docker Image

Clone this repository or copy the `Dockerfile` to your directory, then build the image:

```bash
docker build -t reverse-engineering-toolkit .
```

### 2. Run the Container

Start the container with:

```bash
docker run -it reverse-engineering-toolkit
```

### 3. Analyze Files

#### ELF File Parsing

To analyze an ELF file:

```bash
python3 /opt/re-tools/parse_elf.py /path/to/elf_file
```

#### PE File Parsing

To analyze a PE file:

```bash
python3 /opt/re-tools/parse_pe.py /path/to/pe_file
```

### 4. Using Ghidra and IDA Free

Start Ghidra:

```bash
/opt/ghidra/ghidraRun
```

Start IDA Free:

```bash
/opt/ida/ida64
```

### 5. Mount Local Files

To analyze local binaries, mount a directory:

```bash
docker run -it -v /path/to/binaries:/opt/binaries reverse-engineering-toolkit
```

Access your files under `/opt/binaries` within the container.

## Troubleshooting

- **Permission Issues**: Ensure your user has the necessary permissions to run Docker and access the files.
- **Missing Tools**: Verify the build process completes successfully and all tools are installed.
