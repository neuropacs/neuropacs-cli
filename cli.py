# neuropacs CLI v1.0.3
# (c) 2025 neuropacs
# Released under the MIT License.

import argparse
import os
import neuropacs

# ! If ask for connectionId, dont you need aes_key with it?

def main():
    # Arguments from Docker container
    server_url = os.getenv('SERVER_URL')
    api_key = os.getenv('API_KEY')
    # client = "api"

    parser = argparse.ArgumentParser(description="neuropacs™ CLI tool.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='neuropacs™ sub-command help')

    subparsers.add_parser('connect', 
    help='Creates a new session with neuropacs™. Returns connection JSON.',
    description='Creates a new session with neuropacs™. Returns connection JSON.\n\n'
                'Examples:\n'
                '  Create a new session:\n'
                '     docker run --rm neuropacs connect\n\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)

    new_job_parser = subparsers.add_parser('new-job', 
    help='Creates a neuropacs™ order. Returns a unique order ID.',
    description='Creates a neuropacs™ order. Returns a unique order ID.\n\n'
                'Examples:\n'
                '  Create a new order:\n'
                '     docker run --rm neuropacs new-job\n\n'
                '  Create a new order using an existing connection:\n'
                '     docker run --rm neuropacs new-job --connection-id CONNECTION_ID --aes-key AES_KEY\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    new_job_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    new_job_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID Required if providing --connection-id.")

    upload_dataset_from_path_parser = subparsers.add_parser('upload-dataset-from-path', 
    help='Uploads a dataset from local path. Returns upload status.',
    description='Uploads a dataset from a local path (ex. "/path/to/dataset"). Returns upload status.\n\n'
                'Examples:\n'
                '  Upload a dataset:\n'
                '     docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset-from-path --order-id ORDER_ID\n\n'
                '  Upload a dataset in verbose mode:\n'
                '     docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset-from-path -v --order-id ORDER_ID\n\n'
                '  Upload a dataset with an existing connection:\n'
                '     docker run --rm -v /path/to/dataset/:/data upload-dataset-from-path --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    upload_dataset_from_path_parser.add_argument('--order-id', type=str, required=True, help="Unique base64 identifier for the order.")
    upload_dataset_from_path_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    upload_dataset_from_path_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")
    upload_dataset_from_path_parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode.')

    upload_dataset_from_dicom_web = subparsers.add_parser('upload-dataset-from-dicom-web', 
    help='Upload a dataset via DICOMweb WADO-RS protocol. Returns upload status.',
    description='Uploads a dataset from DICOMweb-compliant server via a base URL and studyUid w/ optional credentials (basic auth). Returns upload status.\n\n'
                'Examples:\n'
                '  Upload a dataset:\n'
                '    docker run --rm --network host neuropacs upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url WADO_URL --study-uid STUDY_UID\n\n'
                '  Upload a dataset w/ credentials:\n'
                '    docker run --rm --network host neuropacs upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url WADO_URL --study-uid STUDY_UID --username USERNAME --password PASSWORD\n\n'
                '  Upload a dataset in verbose mode:\n'
                '    docker run --rm --network host neuropacs upload-dataset-from-dicom-web -v --order-id ORDER_ID --wado_url WADO_URL --study-uid STUDY_UID\n\n'
                '  Upload a dataset with an existing connection:\n'
                '    docker run --rm --network host upload-dataset-from-dicom-web --order-id ORDER_ID --wado_url WADO_URL --study-uid STUDY_UID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    upload_dataset_from_dicom_web.add_argument('--order-id', type=str, required=True, help="Unique base64 identifier for the order.")
    upload_dataset_from_dicom_web.add_argument('--wado_url', type=str, required=True, help="Base URL of the DICOMweb server (e.g., 'http://localhost:8080/dicomweb').")
    upload_dataset_from_dicom_web.add_argument('--study-uid', type=str, required=True, help="Unique Study Instance UID of the study to be retrieved.")
    upload_dataset_from_dicom_web.add_argument('--username', type=str, required=False, help="Username for basic authentication.")
    upload_dataset_from_dicom_web.add_argument('--password', type=str, required=False, help="Password for basic authentication.")
    upload_dataset_from_dicom_web.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    upload_dataset_from_dicom_web.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")
    upload_dataset_from_dicom_web.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode.')

    qc_check_parser = subparsers.add_parser('qc-check', 
    help='QC/Compliance validation for an uploaded dataset. Returns QC report in specified format.',
    description='QC/Compliance validation for an uploaded dataset.\n'
        'Available formats: TXT, CSV, JSON\n\n'
        'Examples:\n'
        '  Retrieves QC results [recommended]:\n'
        '     docker run --rm neuropacs qc-check --order-id ORDER_ID --format FORMAT \n\n'
        '  Retrieves QC results using an existing connection:\n'
        '     docker run --rm neuropacs qc-check --order-id ORDER_ID --format FORMAT  --connection-id CONNECTION_ID --aes-key AES_KEY\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    qc_check_parser.add_argument('--format', type=str, required=True, help="Format of QC report. ['TXT', 'CSV', 'JSON']")
    qc_check_parser.add_argument('--order-id', type=str, required=True, help="Unique base64 identifier for the order.")
    qc_check_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    qc_check_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")
    
    run_job_parser = subparsers.add_parser('run-job', 
    help='Executes a Neuropacs order. Returns a status code.',
    description='Executes a Neuropacs order. Returns a status code.\n'
            'Available product(s): Atypical/MSAp/PSP-v1.0\n\n'
            'Examples:\n'
            '  Execute an order:\n'
            '     docker run --rm neuropacs run-job --order-id ORDER_ID --product PRODUCT_ID \n\n'
            '  Execute an order using an existing connection:\n'
            '     docker run --rm neuropacs run-job --order-id ORDER_ID --product PRODUCT_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
            formatter_class=argparse.RawTextHelpFormatter,
            usage=argparse.SUPPRESS)
    run_job_parser.add_argument('--product', type=str, required=True, help="Neuropacs product to be executed.")
    run_job_parser.add_argument('--order-id', type=str, required=True, help="Unique base64 identifier for the order.")
    run_job_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    run_job_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")

    check_status_parser = subparsers.add_parser('check-status', 
    help='Retrieves current status of a running neuropacs™ order. Return status JSON.',
    description='Retrieves current status of a running neuropacs™ order. Return status JSON.\n\n'
        'Examples:\n'
        '  Check order status:\n'
        '     docker run --rm neuropacs check-status --order-id ORDER_ID\n\n'
        '  Check order status using an existing connection:\n'
        '     docker run --rm neuropacs check-status --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    check_status_parser.add_argument('--order-id', type=str, required=True, help="Unique base64 identifier for the order.")
    check_status_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    check_status_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")
    
    get_results_parser = subparsers.add_parser('get-results', 
    help='Retrieves results from completed neuropacs™ order. Return result in specified format.',
    description='Retrieves current status of a running neuropacs™ order.\n'
        'Available formats: TXT, JSON, XML, PNG, FEATURES\n\n'
        'Examples:\n'
        '  Retrieves results [recommended]:\n'
        '     docker run --rm neuropacs get-results --order-id ORDER_ID --format FORMAT \n\n'
        '  Retrieves results using an existing connection:\n'
        '     docker run --rm neuropacs get-results --order-id ORDER_ID --format FORMAT --connection-id CONNECTION_ID --aes-key AES_KEY\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    get_results_parser.add_argument('--format', type=str, required=True, help="Format of result file. ['TXT', 'XML', 'JSON', 'PNG', 'FEATURES']")
    get_results_parser.add_argument('--order-id', type=str, required=True, help="Unique base64 identifier for the order.")
    get_results_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    get_results_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")

    get_report_parser = subparsers.add_parser('get-report', 
    help='Generate a structured API key usage report. Returns report in specified format.',
    description='Generate a structured API key usage report for any neuropacs™ API key. If an admin API key is used. An aggregated report will be created with all keys associated with the same institution. If "email" format is used, an email will be sent to the admin associated with the specified API key.\n'
        'Available formats: TXT, JSON, EMAIL\n\n'
        'Examples:\n'
        '  Generates report [recommended]:\n'
        '     docker run --rm neuropacs get-report --format FORMAT --start-date START_DATE --end-date END_DATE\n\n'
        '  Generates report using an existing connection:\n'
        '     docker run --rm neuropacs get-results --format FORMAT --start-date START_DATE --end-date END_DATE --connection-id CONNECTION_ID --aes-key AES_KEY\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    get_report_parser.add_argument('--format', type=str, required=True, help="Format of result file. ['TXT', 'JSON', 'EMAIL']")
    get_report_parser.add_argument('--start-date', type=str, required=True, help="Start date of report in the form MM/DD/YYYY.")
    get_report_parser.add_argument('--end-date', type=str, required=True, help="End date of report in the form MM/DD/YYYY.")
    get_report_parser.add_argument('--connection-id', type=str, required=False, help="Unique base64 connection ID associated with session. Required if providing --aes-key.")
    get_report_parser.add_argument('--aes-key', type=str, required=False, help="Unique base64 AES key associated with the provided connection ID. Required if providing --connection-id.")


    args = parser.parse_args()

    if args.command == "connect":
        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        conn = npcs.connect()
        print(conn) # Print connection object

    elif args.command == "new-job":
        connection_id = args.connection_id
        aes_key = args.aes_key
        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        order = npcs.new_job()
        print(order) # Print UUIDv4 order ID

    elif args.command == "upload-dataset-from-path":
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        verbose = args.verbose

        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if connection_id and aes_key :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if verbose: # Verbose
            upload_status = npcs.upload_dataset_from_path(order_id=order_id, path="/data", callback=lambda data: print(data))
        else:
            upload_status = npcs.upload_dataset_from_path(order_id=order_id, path="/data")
        print(upload_status)

    elif args.command == "upload-dataset-from-dicom-web":
        wado_url = args.wado_url
        study_uid = args.study_uid
        username = args.username
        password = args.password
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        verbose = args.verbose
        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if connection_id and aes_key :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if(username is not None and password is not None):
            if verbose:
                upload_status = npcs.upload_dataset_from_dicom_web(order_id=order_id, wado_url=wado_url, study_uid=study_uid, username=username, password=password, callback=lambda data: print(data))
            else:
                upload_status = npcs.upload_dataset_from_dicom_web(order_id=order_id, wado_url=wado_url, study_uid=study_uid, username=username, password=password)
        else:
            if verbose:
                upload_status = npcs.upload_dataset_from_dicom_web(order_id=order_id, wado_url=wado_url, study_uid=study_uid, callback=lambda data: print(data))
            else:
                upload_status = npcs.upload_dataset_from_dicom_web(order_id=order_id, wado_url=wado_url, study_uid=study_uid)
        print(upload_status)

    elif args.command == "qc-check":
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        format = args.format

        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        results = npcs.qc_check(order_id=order_id, format=format)
        print(results)


    elif args.command == "run-job":
        connection_id = args.connection_id
        aes_key = args.aes_key
        product = args.product
        order_id = args.order_id
        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        job = npcs.run_job(product_name=product, order_id=order_id)
        print(job)

    elif args.command == "check-status":
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        job_status = npcs.check_status(order_id=order_id)
        print(job_status)

    elif args.command == "get-results":
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        format = args.format
        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")

        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        results = npcs.get_results(order_id=order_id, format=format)
        print(results)

    elif args.command == "get-report":
        connection_id = args.connection_id
        aes_key = args.aes_key
        format = args.format
        start_date = args.start_date
        end_date = args.end_date

        npcs = neuropacs.init(server_url=server_url, api_key=api_key, origin_type="CLI")
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        report = npcs.get_report(format=format, start_date=start_date, end_date=end_date)
        print(report)


if __name__ == '__main__':
    main()
