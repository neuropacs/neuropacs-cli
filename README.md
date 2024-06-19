# Neuropacs CLI

This project provides a CLI for the Neuropacs project via a Docker container. This project provides a Dockerfile to build the Neuropacs CLI Docker image.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Docker
  - Install Docker on Windows: https://docs.docker.com/desktop/install/windows-install/
  - Install Docker on Linux: https://docs.docker.com/engine/install/
  - Install Docker on Mac: https://docs.docker.com/desktop/install/mac-install/

### Build the image:

#### Option 1: Pull the neuropacs-cli repository and build from the Dockerfile

1. Pull the neuropacs-cli repository
   Note: Git is required for this option

```bash
git clone https://github.com/neuropacs/neuropacs-cli.git
```

2. Navigate to neuropacs-cli project

```bash
cd neuropacs-cli/
```

3. Build the image
   Note: Use the server_url and api_key provided by Neuropacs

```bash
sudo docker build . --no-cache --build-arg server_url=SERVER_URL --build-arg api_key=API_KEY -t neuropacs
```

## Usage

Hint: To view the help screen of any command, use the '-h' or '--help' option.

### Create a neuropacs session. Returns connection JSON.

Example: Create a neuropacs connection [recommended]:

```bash
sudo docker run --rm neuropacs connect
```

### Creates a Neuropacs order. Returns a unique order ID.

Example: Create a new order [recommended]:

```bash
sudo docker run --rm neuropacs new-job
```

Example: Create a new order using an existing connection:

```bash
sudo docker run --rm neuropacs new-job --connection-id CONNECTION_ID --aes-key AES_KEY
```

### Uploads a dataset. Returns upload status code.

Example: Upload a dataset [recommended]:

```bash
sudo docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset --order-id ORDER_ID
```

Example: Upload a dataset in verbose mode:

```bash
sudo docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset -v --order-id ORDER_ID
```

Example: Upload a dataset with a custom dataset ID:

```bash
sudo docker run --rm -v /path/to/dataset/:/data upload-dataset --order-id ORDER_ID --dataset-id DATASET_ID
```

Example: Upload a dataset with an existing connection:

```bash
sudo docker run --rm -v /path/to/dataset/:/data upload-dataset --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

### Validates an existing dataset. Returns array of missing files.

Example: Validate a dataset [recommended]:

```bash
sudo docker run --rm -v /path/to/dataset/:/data neuropacs validate-dataset --order-id ORDER_ID
```

Example: Validate a dataset in verbose mode:

```bash
sudo docker run --rm -v /path/to/dataset/:/data neuropacs validate-dataset -v --order-id ORDER_ID
```

Example: Validate a dataset with a custom dataset ID:

```bash
sudo docker run --rm -v /path/to/dataset/:/data validate-dataset --order-id ORDER_ID --dataset-id DATASET_ID
```

Example: Validate a dataset with an existing connection:

```bash
sudo docker run --rm -v /path/to/dataset/:/data validate-dataset --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

### Executes a Neuropacs order. Returns a status code.

Note: To use the current PD vs MSP diagnostic pipeline, use "PD/MSA/PSP-v1.0" for --product-id

Example: Executes an order [recommended]:

```bash
sudo docker run --rm neuropacs run-job --product-id PRODUCT_ID --order-id ORDER_ID
```

Example: Execute an order with a custom dataset ID:

```bash
sudo docker run --rm neuropacs run-job --product-id PRODUCT_ID --order-id ORDER_ID --dataset-id DATASET_ID
```

Example: Execute an order using an existing connection:

```bash
sudo docker run --rm neuropacs run-job --product-id PRODUCT_ID --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

### Retrieves current status of a running Neuropacs order. Return status JSON.

Example: Check order status [recommended]:

```bash
sudo docker run --rm neuropacs check-status --order-id ORDER_ID
```

Example: Check order status with a custom dataset ID:

```bash
sudo docker run --rm neuropacs check-status --order-id ORDER_ID --dataset-id DATASET_ID
```

Example: Check order status using an existing connection:

```bash
sudo docker run --rm neuropacs check-status --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

### Retrieves results from completed Neuropacs order. Return result in specified format.

Note: Available formats: TXT, JSON, XML, PNG

Example: Retrieves results [recommended]:

```bash
sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID
```

Example: Retrieves results with a custom dataset ID:

```bash
sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID --dataset-id DATASET_ID
```

Example: Retrieves results using an existing connection:

```bash
sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

## Author

Kerrick Cavanaugh (kerrick@neuropacs.com)

```

```
