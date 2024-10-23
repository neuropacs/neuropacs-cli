![CodeQL](https://github.com/neuropacs/neuropacs-cli/actions/workflows/codeql-analysis.yml/badge.svg)

# neuropacs™ CLI

This repository provides a CLI for the neuropacs™ project via a Docker container.

## Getting Started

### Prerequisites

- Docker
  - Install Docker on Windows: https://docs.docker.com/desktop/install/windows-install/
  - Install Docker on Linux: https://docs.docker.com/engine/install/
  - Install Docker on Mac: https://docs.docker.com/desktop/install/mac-install/

### Build the image:

#### Pull the neuropacs-cli repository and build from the Dockerfile

1. Pull the neuropacs-cli repository

   Note: Git is required

```bash
git clone https://github.com/neuropacs/neuropacs-cli.git
```

2. Navigate to neuropacs-cli project

```bash
cd neuropacs-cli/
```

3. Build the image

   Note: Use the URL and API key provided by neuropacs™

```bash
sudo docker build . --no-cache --build-arg server_url=SERVER_URL --build-arg api_key=API_KEY -t neuropacs
```

## Usage

Hint: To view the help screen of any command, use the '-h' or '--help' option.

### Create a neuropacs™ session. Returns connection JSON.

NOTE: This is optional. Each command will start a new session unless custom session parameters are specified.

- Example: Create a neuropacs™ session [recommended]:

```bash
sudo docker run --rm neuropacs connect
```

- View help menu:

```bash
sudo docker run --rm neuropacs connect -h
```

### Creates a neuropacs™ order. Returns a unique order ID.

- Example: Create a new order [recommended]:

```bash
sudo docker run --rm neuropacs new-job
```

- Example: Create a new order using an existing connection:

```bash
sudo docker run --rm neuropacs new-job --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu:

```bash
sudo docker run --rm neuropacs new-job -h
```

### Uploads a dataset. Returns upload status code.

- Example: Upload a dataset [recommended]:

```bash
sudo docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset --order-id ORDER_ID
```

- Example: Upload a dataset in verbose mode:

```bash
sudo docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset -v --order-id ORDER_ID
```

- Example: Upload a dataset with an existing connection:

```bash
sudo docker run --rm -v /path/to/dataset/:/data upload-dataset --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu:

```bash
sudo docker run --rm neuropacs upload-dataset  -h
```

### Executes a neuropacs™ order. Returns a status code.

NOTE: To use the current PD vs MSP diagnostic pipeline, use "Atypical/MSAp/PSP-v1.0" for --product

- Example: Executes an order [recommended]:

```bash
sudo docker run --rm neuropacs run-job --product PRODUCT_ID --order-id ORDER_ID
```

- Example: Execute an order using an existing connection:

```bash
sudo docker run --rm neuropacs run-job --product PRODUCT_ID --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu:

```bash
sudo docker run --rm neuropacs run-job  -h
```

### Retrieves current status of a running neuropacs™ order. Return status JSON.

- Example: Check order status [recommended]:

```bash
sudo docker run --rm neuropacs check-status --order-id ORDER_ID
```

- Example: Check order status using an existing connection:

```bash
sudo docker run --rm neuropacs check-status --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu:

```bash
sudo docker run --rm neuropacs check-status  -h
```

### Retrieves results from completed neuropacs™ order. Return result in specified format.

NOTE: Available formats: TXT, JSON, XML, PNG

- Example: Retrieves results [recommended]:

```bash
sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID
```

- Example: Retrieves results using an existing connection:

```bash
sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu:

```bash
sudo docker run --rm neuropacs get-results  -h
```

## Author

Kerrick Cavanaugh (kerrick@neuropacs.com)
