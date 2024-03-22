USAGE:

# Neuropacs CLI

This project provides a CLI for the Neuropacs project via a Docker container. This project provides a Dockerfile to build the Neuropacs CLI Docker image.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Docker
  - Install Docker on Windows: https://docs.docker.com/desktop/install/windows-install/
  - Install Docker on Linux: https://docs.docker.com/desktop/install/linux-install/
  - Install Docker on Mac: https://docs.docker.com/desktop/install/mac-install/

### Build the image:

#### Option 1: Pull from Docker container registry

#### Option 2: Pull the neuropacs-cli repository and build from the Dockerfile

1. Pull the neuropacs-cli repository

```bash
git clone https://github.com/neuropacs/neuropacs-cli.git
```

2. Build the image
   Note: Use the server_url and api_key provided by Neuropacs

```bash
sudo docker build --build-arg server_url=<server_url> --build-arg api_key=<api_key> -t neuropacs /path/to/neuropacs-cli/project
```

## Usage

# Create a new order (returns an order_id)

```bash
sudo docker run --rm neuropacs new-job
```

# Upload a dataset

```bash
sudo docker run --rm -v </path/in/host>:/data neuropacs upload-dataset --dataset-path /data --order-id <order_id>
```

# Run an order

```bash
sudo docker run --rm neuropacs run-job --product-id <product_id> --order-id <order_id> --dataset-id <dataset_id>
```

# Check order status

```bash
sudo docker run --rm neuropacs check-status --order-id <order_id>
```

# Get results

```bas
sudo docker run --rm neuropacs get-results --order-id <order_id> --format <format>
```

### Authors

Kerrick Cavanaugh (kerrick@neuropacs.com)
