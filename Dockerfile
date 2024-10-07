# Python3.9 slim parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/neuropacs-cli

# Copy the current directory contents into the container
COPY . /usr/src/neuropacs-cli

# Update pip and install required packages
RUN pip install --upgrade pip
RUN pip install \
    backports.tarfile \
    certifi \
    cffi \
    charset-normalizer \
    cryptography \
    idna \
    importlib_metadata \
    jaraco.classes \
    jaraco.context \
    jaraco.functools \
    keyring \
    markdown-it-py \
    mdurl \
    more-itertools \
    Naked \
    pillow \
    pkginfo \
    pycparser \
    pycryptodome \
    Pygments \
    PyYAML \
    readme-renderer \
    requests \
    requests-toolbelt \
    rfc3986 \
    rich \
    rsa \
    shellescape \
    tqdm \
    twine \
    update \
    urllib3 \
    zipp \
    neuropacs

# Define build-time variables for server_url and api_key
ARG server_url
ARG api_key

# Set environment variables
ENV SERVER_URL=$server_url
ENV API_KEY=$api_key

# Run CLI when the container launches
ENTRYPOINT ["python", "/usr/src/neuropacs-cli/cli.py"]
