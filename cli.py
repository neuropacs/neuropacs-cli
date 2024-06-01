import argparse
import os
import neuropacs

# ! If ask for connectionId, dont you need aes_key with it?

def main():
    # Arguments from Docker container
    server_url = os.getenv('SERVER_URL')
    api_key = os.getenv('API_KEY')
    # client = "api"

    parser = argparse.ArgumentParser(description="Neuropacs CLI tool.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Neuropacs sub-command help')

    # connect_parser = subparsers.add_parser('connect', help='Creates a new session with Neuropacs.')

    new_job_parser = subparsers.add_parser('new-job', 
    help='Creates a Neuropacs order. Returns a unique order ID.',
    description='Creates a Neuropacs order. Returns a unique order ID.\n\n'
                'Examples:\n'
                '  Create a new order [recommended]:\n'
                '    sudo docker run --rm neuropacs new-job\n\n'
                '  Create a new order using an existing connection:\n'
                '    sudo docker run --rm neuropacs new-job --connection-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --aes-key yyyyyyyyyyyyyyyyyyy==\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    new_job_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    new_job_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    upload_dataset_parser = subparsers.add_parser('upload-dataset', 
    help='Uploads a dataset. Returns upload status code.',
    description='Uploads a dataset. Returns upload status code.\n\n'
                'Examples:\n'
                '  Upload a dataset [recommended]:\n'
                '    sudo docker run --rm upload-dataset --dataset-path "C:\\path\\to\\dataset" --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\n\n'
                '  Upload a dataset with a custom dataset ID:\n'
                '    sudo docker run --rm upload-dataset --dataset-path "C:\\path\\to\\dataset" --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --dataset-id example123\n\n'
                '  Upload a dataset with an existing connection:\n'
                '    sudo docker run --rm upload-dataset --dataset-path "C:\\path\\to\\dataset" --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --connection-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --aes-key yyyyyyyyyyyyyyyyyyy==\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    upload_dataset_parser.add_argument('--dataset-path', type=str, required=True, help="Path of dataset.")
    upload_dataset_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    upload_dataset_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID. If not provided, one will be generated for you.")
    upload_dataset_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    upload_dataset_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    validate_dataset_parser = subparsers.add_parser('validate-dataset', 
    help='Validates an existing dataset. Returns array of missing files.',  
    description='Validates an existing dataset. Returns array of missing files.\n\n'
                'Examples:\n'
                '  Validate a dataset [recommended]:\n'
                '    sudo docker run --rm validate-dataset --dataset-path "C:\\path\\to\\dataset" --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\n\n'
                '  Validate a dataset with a custom dataset ID:\n'
                '    sudo docker run --rm validate-dataset --dataset-path "C:\\path\\to\\dataset" --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --dataset-id example123\n\n'
                '  Validate a dataset with an existing connection:\n'
                '    sudo docker run --rm validate-dataset --dataset-path "C:\\path\\to\\dataset" --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --connection-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --aes-key yyyyyyyyyyyyyyyyyyy==\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    validate_dataset_parser.add_argument('--dataset-path', type=str, required=True, help="Path of dataset.")
    validate_dataset_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    validate_dataset_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID. Default is same as order ID.")
    validate_dataset_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    validate_dataset_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    run_job_parser = subparsers.add_parser('run-job', 
    help='Executes a Neuropacs order. Returns a status code.',
    description='Executes a Neuropacs order. Returns a status code.\n'
            'Available product-id(s): PD/MSA/PSP-v1.0\n\n'
            'Examples:\n'
            '  Execute an order [recommended]:\n'
            '    sudo docker run --rm neuropacs run-job --product-id PD/MSA/PSP-v1.0 --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\n\n'
            '  Execute an order with a custom dataset ID:\n'
            '    sudo docker run --rm neuropacs run-job --product-id PD/MSA/PSP-v1.0 --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --dataset-id example123\n\n'
            '  Execute an order using an existing connection:\n'
            '    sudo docker run --rm neuropacs run-job --product-id PD/MSA/PSP-v1.0--order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --connection-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --aes-key yyyyyyyyyyyyyyyyyyy==\n',
            formatter_class=argparse.RawTextHelpFormatter,
            usage=argparse.SUPPRESS)
    run_job_parser.add_argument('--product-id', type=str, required=True, help="Neuropacs product to be executed. ")
    run_job_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    run_job_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID. Default is same as order ID.")
    run_job_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    run_job_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    check_status_parser = subparsers.add_parser('check-status', 
    help='Retrieves current status of a running Neuropacs order.',
    description='Retrieves current status of a running Neuropacs order.\n\n'
        'Examples:\n'
        '  Check order status [recommended]:\n'
        '    sudo docker run --rm neuropacs check-status --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\n\n'
        '  Check order status with a custom dataset ID:\n'
        '    sudo docker run --rm neuropacs check-status --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --dataset-id example123\n\n'
        '  Check order status using an existing connection:\n'
        '    sudo docker run --rm neuropacs check-status --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --connection-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --aes-key yyyyyyyyyyyyyyyyyyy==\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    check_status_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    check_status_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID. Default is same as order-id.")
    check_status_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    check_status_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")
    
    get_results_parser = subparsers.add_parser('get-results', 
    help='Retrieves results from completed Neuropacs order.',
    description='Retrieves current status of a running Neuropacs order.\n'
        'Available formats: TXT, JSON, XML\n\n'
        'Examples:\n'
        '  Retrieves results [recommended]:\n'
        '    sudo docker run --rm neuropacs get-results --format TXT --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\n\n'
        '  Retrieves results with a custom dataset ID:\n'
        '    sudo docker run --rm neuropacs get-results --format TXT --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --dataset-id example123\n\n'
        '  CRetrieves results using an existing connection:\n'
        '    sudo docker run --rm neuropacs get-results --format TXT --order-id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee --connection-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --aes-key yyyyyyyyyyyyyyyyyyy==\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    get_results_parser.add_argument('--format', type=str, required=True, help="Format of result file. ['TXT', 'XML', 'JSON']")
    get_results_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    get_results_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID. Default is same as order-id.")
    get_results_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    get_results_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    args = parser.parse_args()

    if args.command == "connect":
        npcs = neuropacs.init(server_url, api_key)
        conn = npcs.connect()
        print(conn)
    elif args.command == "new-job":
        connection_id = args.connection_id
        aes_key = args.connection_id
        npcs = neuropacs.init(server_url, api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()
        order = npcs.new_job()
        print(order)
    elif args.command == "upload-dataset":
        connection_id = args.connection_id
        aes_key = args.connection_id
        dataset_path = args.dataset_path
        dataset_id = args.dataset_id
        order_id = args.order_id
        npcs = neuropacs.init(server_url, api_key)
        if connection_id and aes_key :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()
        
        if dataset_id is not None: # With custom dataset ID
            upload_status = npcs.upload_dataset(dataset_path, order_id, dataset_id, callback=lambda data: print(data))
        else:   # Default
            upload_status = npcs.upload_dataset(dataset_path, order_id, order_id, callback=lambda data: print(data))
        print(upload_status)
    elif args.command == "validate-dataset":
        connection_id = args.connection_id
        aes_key = args.connection_id
        dataset_path = args.dataset_path
        order_id = args.order_id
        npcs = neuropacs.init(server_url, api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if dataset_id is not None: # With custom dataset ID
            validation_results = npcs.validate_upload(dataset_path, order_id, dataset_id, callback=lambda data: print(data))
        else: # Default
            validation_results = npcs.validate_upload(dataset_path, order_id, order_id, callback=lambda data: print(data))
        print(validation_results)
    elif args.command == "run-job":
        connection_id = args.connection_id
        aes_key = args.connection_id
        product_id = args.product_id
        order_id = args.order_id
        dataset_id = args.dataset_id
        npcs = neuropacs.init(server_url, api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if dataset_id is not None: # With custom dataset ID
            job = npcs.run_job(product_id, order_id, dataset_id)
        else: # Default
            job = npcs.run_job(product_id, order_id, order_id)
        print(job)
    elif args.command == "check-status":
        connection_id = args.connection_id
        aes_key = args.connection_id
        order_id = args.order_id
        dataset_id = args.dataset_id
        npcs = neuropacs.init(server_url, api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if dataset_id is not None: # With custom dataset ID
            job_status = npcs.check_status(order_id, dataset_id)
        else: # Default
            job_status = npcs.check_status(order_id, order_id)
        
        print(job_status)
    elif args.command == "get-results":
        connection_id = args.connection_id
        aes_key = args.connection_id
        order_id = args.order_id
        dataset_id=args.dataset_id
        format = args.format
        npcs = neuropacs.init(server_url, api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if dataset_id is not None: # With custom dataset ID
            results = npcs.get_results(format, order_id, dataset_id)
        else: # Default
            results = npcs.get_results(format, order_id, order_id)
        print(results)


if __name__ == '__main__':
    main()
