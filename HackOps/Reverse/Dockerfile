# Base image with Python and utilities
FROM ubuntu:20.04

# Set environment variables to suppress interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    python3-pip \
    default-jre \
    wget \
    curl \
    binutils \
    gdb \
    strace \
    ltrace \
    binwalk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python libraries for reverse engineering
RUN pip3 install capstone keystone-engine

# Install Ghidra
RUN mkdir -p /opt/ghidra && \
    wget -q https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.3.1_build/ghidra_10.3.1_PUBLIC_20231010.zip -O /tmp/ghidra.zip && \
    unzip /tmp/ghidra.zip -d /opt/ghidra && \
    rm /tmp/ghidra.zip

# Install IDA Free
RUN wget -q https://out7.hex-rays.com/files/idafree82_linux.run -O /tmp/idafree.run && \
    chmod +x /tmp/idafree.run && \
    /tmp/idafree.run --mode unattended --prefix /opt/ida && \
    rm /tmp/idafree.run

# Copy automation scripts
WORKDIR /opt/re-tools
COPY scripts/* /opt/re-tools/

# Set the default entrypoint to bash for flexibility
ENTRYPOINT ["/bin/bash"]
