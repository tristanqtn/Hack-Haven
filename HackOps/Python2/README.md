# Python 2 Docker Container for Running Exploits

This repository provides a Dockerfile to create a lightweight Python 2.7 environment for running exploits and scripts that require Python 2.7. This is particularly useful for CTF challenges where Python 2 is still commonly used.

## Features

- Based on the official `python:2.7-slim` Docker image.
- Includes essential system dependencies for Python development:
  - `build-essential`
  - `libssl-dev`
  - `libffi-dev`
  - `python-dev`
- Minimalistic setup to keep the container lightweight.

## Prerequisites

Ensure that Docker is installed on your system. You can download and install Docker from [Docker's official website](https://www.docker.com/).

## Setup Instructions

### 1. Build the Docker Image

Clone this repository or copy the `Dockerfile` to your desired directory. Navigate to the directory containing the `Dockerfile` and build the Docker image:

```bash
docker build -t python2-exploit-env .
```

### 2. Running the Container

To run a Python 2 interactive shell, execute:

```bash
docker run -it python2-exploit-env
```

You will be dropped into a Python 2.7 interactive session where you can execute your exploits or scripts.

### 3. Mount Local Scripts

To use local scripts in the container, mount a directory from your host machine. For example, if your scripts are in `/path/to/scripts`:

```bash
docker run -it -v /path/to/scripts:/usr/src/app python2-exploit-env
```

Within the container, you can access your scripts in the `/usr/src/app` directory.

### 4. Install Additional Python Packages

If your exploit requires additional Python packages, you can install them using `pip` within the container. For example:

```bash
pip install some-package
```

Alternatively, you can add these packages to the `Dockerfile`:

```dockerfile
# Example: Add additional packages
RUN pip install some-package another-package
```

Then rebuild the image.

### 5. Customizing the Image

If your scripts are static, you can copy them directly into the container during the build process. Uncomment the `COPY` line in the `Dockerfile` and modify it to point to your scripts:

```dockerfile
# Copy your Python scripts into the container (optional)
COPY ./scripts /usr/src/app/
```

Rebuild the image to include your scripts.

### 6. Running a Specific Script

To execute a specific Python script, use the following command:

```bash
docker run -it python2-exploit-env python /usr/src/app/your-script.py
```

Replace `your-script.py` with the name of your script.

## Cleanup

To remove the image and container after use:

1. Stop and remove running containers:

   ```bash
   docker ps -a  # List all containers
   docker rm <container_id>
   ```

2. Remove the Docker image:
   ```bash
   docker rmi python2-exploit-env
   ```

## Troubleshooting

- **Permission Issues**: Ensure you have the necessary permissions to run Docker and access the directories.
- **Package Installation Errors**: Verify that the required system dependencies are installed in the image.
