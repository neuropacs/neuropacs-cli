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
sudo docker build . --no-cache --build-arg server_url=<server_url> --build-arg api_key=<api_key> -t neuropacs
```

## Usage

### Create a new order (returns an order ID)

```bash
sudo docker run --rm neuropacs new-job
```

### Upload a dataset (returns a dataset ID)

```bash
sudo docker run --rm -v </path/to/dataset>:/data neuropacs upload-dataset --dataset-path /data --order-id <order_id>
```

### Run an order

Note: To use the current PD vs MSP diagnostic pipeline, use "PD/MSA/PSP-v1.0" for <product_id>

```bash
sudo docker run --rm neuropacs run-job --product-id <product_id> --order-id <order_id> --dataset-id <dataset_id>
```

### Check order status

```bash
sudo docker run --rm neuropacs check-status --order-id <order_id> --dataset-id <dataset_id>
```

### Get results

```bash
sudo docker run --rm neuropacs get-results --format <format> --order-id <order_id> --dataset-id <dataset_id>
```

## Authors

Kerrick Cavanaugh (kerrick@neuropacs.com)
