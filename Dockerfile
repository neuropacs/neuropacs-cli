# Python3.9 slim parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/neuropacs-cli

# Copy the current directory contents into the container
COPY . /usr/src/neuropacs-cli

# Update pip and install required packages
RUN pip install --upgrade pip
RUN pip install \
    argparse \
    tqdm \
    neuropacs


# Run CLI when the container launches
ENTRYPOINT ["python", "/usr/src/neuropacs-cli/cli.py"]
