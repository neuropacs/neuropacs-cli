[![Integration Tests](https://github.com/neuropacs/neuropacs-py-api/actions/workflows/ci.yml/badge.svg)](https://github.com/neuropacs/neuropacs-py-api/actions/workflows/ci.yml)
![CodeQL](https://github.com/neuropacs/neuropacs-cli/actions/workflows/codeql-analysis.yml/badge.svg)

# neuropacs™ CLI

Our CLI enables seamless integration with our product's capabilities in any command line-based environment.

## Installation

### Prerequisites

- Docker
  - Install Docker on Windows: https://docs.docker.com/desktop/install/windows-install/
  - Install Docker on Linux: https://docs.docker.com/engine/install/
  - Install Docker on Mac: https://docs.docker.com/desktop/install/mac-install/

### Option 1: Pull image from Docker Hub

1. Pull the image

```bash
docker pull neuropacman/neuropacs-cli
```

### Option 2. Build with docker-compose

1. Add your API key to the .env file

```env
API_KEY=your_api_key
```

2. Build with docker-compose

```bash
docker-compose up
```

### Option 3: Build from source

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

```bash
docker build . --no-cache -t neuropacs
```

## Using your API key

If using options 1 or 3 when building neuropacs-cli, you will need to pass your API key with each run command. Use one of the two following options:

1. Pass your API key manually using '-e' flag in each run command [most common]

```bash
docker run --rm -e API_KEY=your_api_key neuropacs new-job
```

2. Pass a .env file using '--env-file' flag in each command

```bash
docker run --rm --env-file .env neuropacs new-job
```

## Usage

Hint: To view the help screen of any command, use the '-h' or '--help' option.

### Create a neuropacs™ session. Returns connection JSON string.

NOTE: This is optional. Each command will start a new session unless custom session parameters are specified.

- Example: Create a neuropacs™ session [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs connect
```

- View help menu for more details:

```bash
docker run --rm neuropacs connect -h
```

### Create a neuropacs™ order. Returns a unique order ID.

- Example: Create a new order [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs new-job
```

- Example: Create a new order using an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs new-job --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu for more details:

```bash
docker run --rm neuropacs new-job -h
```

### Upload a dataset from path. Returns upload status.

- Example: Upload a dataset from path [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key -v /path/to/dataset/:/data neuropacs upload-dataset-from-path --order-id ORDER_ID
```

- Example: Upload a dataset from path with progress bar (verbose):

```bash
docker run --rm -e API_KEY=your_api_key -v /path/to/dataset/:/data neuropacs upload-dataset-from-path --progress --order-id ORDER_ID
```

- View help menu for more details:

```bash
docker run --rm neuropacs upload-dataset-from-path -h
```

### Upload a dataset from DICOMweb WADO-RS. Returns upload status.

- Example: Upload a dataset from DICOMweb WADO-RS w/out credentials [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key --network host neuropacs upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url BASE_URL --study-uid STUDY_UID
```

- Example: Upload a dataset from DICOMweb WADO-RS w/out credentials with a progress bar (verbose):

```bash
docker run --rm -e API_KEY=your_api_key --network host neuropacs upload-dataset-from-dicom-web --progress --order-id ORDER_ID --wado_url BASE_URL --study-uid STUDY_UID
```

- Example: Upload a dataset from DICOMweb WADO-RS w/out credentials with an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key --network host upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url BASE_URL --study-uid STUDY_UID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- Example: Upload a dataset from DICOMweb WADO-RS w/ credentials [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key --network host neuropacs upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url BASE_URL --study-uid STUDY_UID --username USERNAME --password PASSWORD
```

- Example: Upload a dataset from DICOMweb WADO-RS w/ credentials with a progress bar (verbose):

```bash
docker run --rm -e API_KEY=your_api_key --network host neuropacs upload-dataset-from-dicom-web --progress --order-id ORDER_ID --wado_url BASE_URL --study-uid STUDY_UID --username USERNAME --password PASSWORD
```

- Example: Upload a dataset from DICOMweb WADO-RS w/ credentials with an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key --network host upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url BASE_URL --study-uid STUDY_UID --connection-id CONNECTION_ID --aes-key AES_KEY --username USERNAME --password PASSWORD
```

- View help menu for more details:

```bash
docker run --rm neuropacs upload-dataset-from-dicom-web -h
```

### QC/Compliance validation for an uploaded dataset. Returns QC report in specified format.

NOTE: Available formats: TXT, JSON, CSV

- Example: Retrieves QC results [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs qc-check --order-id ORDER_ID --format FORMAT
```

- Example: Retrieves QC results using an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs qc-check --order-id ORDER_ID --format FORMAT  --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu for more details:

```bash
docker run --rm neuropacs qc-check -h
```

### Execute a neuropacs™ order. Returns a status code.

NOTE: To use the current PD vs MSP diagnostic pipeline, use "Atypical/MSAp/PSP-v1.0" for --product

- Example: Executes an order [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs run-job --order-id ORDER_ID --product PRODUCT_ID
```

- Example: Execute an order using an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs run-job --order-id ORDER_ID --product PRODUCT_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu for more details:

```bash
docker run --rm neuropacs run-job -h
```

### Retrieve current status of a running neuropacs™ order. Return status JSON.

- Example: Check order status [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs check-status --order-id ORDER_ID
```

- Example: Check order status using an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs check-status --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu for more details:

```bash
docker run --rm neuropacs check-status -h
```

### Retrieve results from completed neuropacs™ order. Return result in specified format.

NOTE: Available formats: TXT, JSON, XML, PNG, FEATURES

- Example: Retrieves results [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs get-results --order-id ORDER_ID --format FORMAT
```

- Example: Retrieves results using an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs get-results --order-id ORDER_ID --format FORMAT --connection-id CONNECTION_ID --aes-key AES_KEY
```

### Generate a structured API key usage report. Returns report in specified format.

NOTE: Available formats: TXT, JSON, EMAIL

- Example: Generates report [recommended]:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs get-report --format FORMAT --start-date START_DATE --end-date END_DATE
```

- Example: Generates report using an existing connection:

```bash
docker run --rm -e API_KEY=your_api_key neuropacs get-report --format FORMAT --start-date START_DATE --end-date END_DATE --connection-id CONNECTION_ID --aes-key AES_KEY
```

- View help menu for more details:

```bash
docker run --rm neuropacs get-report -h
```

## Author

Kerrick Cavanaugh (kerrick@neuropacs.com)
