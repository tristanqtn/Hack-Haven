# Use an official Python 2.7 image
FROM python:2.7-slim

# Set environment variables to suppress interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /usr/src/app

# Copy your Python scripts into the container (optional)
# COPY ./scripts /usr/src/app/

# Install additional Python packages if needed
# RUN pip install some-package

# Expose the port that is used for the exploit runs on
# EXPOSE 5000

# Default command to run Python
ENTRYPOINT ["python"]