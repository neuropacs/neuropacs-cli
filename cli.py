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

    subparsers.add_parser('connect', 
    help='Creates a new session with Neuropacs. Returns connection JSON.',
    description='Creates a new session with Neuropacs. Returns connection JSON.\n\n'
                'Examples:\n'
                '  Create a new session [recommended]:\n'/
                '    sudo docker run --rm neuropacs connect\n\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)

    new_job_parser = subparsers.add_parser('new-job', 
    help='Creates a Neuropacs order. Returns a unique order ID.',
    description='Creates a Neuropacs order. Returns a unique order ID.\n\n'
                'Examples:\n'
                '  Create a new order [recommended]:\n'
                '    sudo docker run --rm neuropacs new-job\n\n'
                '  Create a new order using an existing connection:\n'
                '    sudo docker run --rm neuropacs new-job --connection-id CONNECTION_ID --aes-key AES_KEY\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    new_job_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    new_job_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    upload_dataset_parser = subparsers.add_parser('upload-dataset', 
    help='Uploads a dataset. Returns upload status code.',
    description='Uploads a dataset. Returns upload status code.\n\n'
                'Examples:\n'
                '  Upload a dataset [recommended]:\n'
                '    sudo docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset --order-id ORDER_ID\n\n'
                '  Upload a dataset in verbose mode:\n'
                '    sudo docker run --rm -v /path/to/dataset/:/data neuropacs upload-dataset -v --order-id ORDER_ID\n\n'
                '  Upload a dataset with an existing connection:\n'
                '    sudo docker run --rm -v /path/to/dataset/:/data upload-dataset --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
                formatter_class=argparse.RawTextHelpFormatter,
                usage=argparse.SUPPRESS)
    upload_dataset_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    upload_dataset_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    upload_dataset_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")
    upload_dataset_parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode.')
    
    run_job_parser = subparsers.add_parser('run-job', 
    help='Executes a Neuropacs order. Returns a status code.',
    description='Executes a Neuropacs order. Returns a status code.\n'
            'Available product-id(s): PD/MSA/PSP-v1.0\n\n'
            'Examples:\n'
            '  Execute an order [recommended]:\n'
            '    sudo docker run --rm neuropacs run-job --product-id PRODUCT_ID --order-id ORDER_ID\n\n'
            '  Execute an order using an existing connection:\n'
            '    sudo docker run --rm neuropacs run-job --product-id PRODUCT_ID --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
            formatter_class=argparse.RawTextHelpFormatter,
            usage=argparse.SUPPRESS)
    run_job_parser.add_argument('--product-id', type=str, required=True, help="Neuropacs product to be executed. ")
    run_job_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    run_job_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    run_job_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    check_status_parser = subparsers.add_parser('check-status', 
    help='Retrieves current status of a running Neuropacs order. Return status JSON.',
    description='Retrieves current status of a running Neuropacs order. Return status JSON.\n\n'
        'Examples:\n'
        '  Check order status [recommended]:\n'
        '    sudo docker run --rm neuropacs check-status --order-id ORDER_ID\n\n'
        '  Check order status using an existing connection:\n'
        '    sudo docker run --rm neuropacs check-status --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    check_status_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    check_status_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    check_status_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")
    
    get_results_parser = subparsers.add_parser('get-results', 
    help='Retrieves results from completed Neuropacs order. Return result in specified format.',
    description='Retrieves current status of a running Neuropacs order.\n'
        'Available formats: TXT, JSON, XML, PNG\n\n'
        'Examples:\n'
        '  Retrieves results [recommended]:\n'
        '    sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID\n\n'
        '  Retrieves results using an existing connection:\n'
        '    sudo docker run --rm neuropacs get-results --format FORMAT --order-id ORDER_ID --connection-id CONNECTION_ID --aes-key AES_KEY\n',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    get_results_parser.add_argument('--format', type=str, required=True, help="Format of result file. ['TXT', 'XML', 'JSON']")
    get_results_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    get_results_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID. Required if providing --aes-key.")
    get_results_parser.add_argument('--aes-key', type=str, required=False, help="Base64 connection ID. Required if providing --connection-id.")

    args = parser.parse_args()

    if args.command == "connect":
        npcs = neuropacs.init(server_url=server_url, api_key=api_key)
        conn = npcs.connect()
        print(conn) # Print connection object
    elif args.command == "new-job":
        connection_id = args.connection_id
        aes_key = args.aes_key
        npcs = neuropacs.init(server_url=server_url, api_key=api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        order = npcs.new_job()
        print(order) # Print UUIDv4 order ID
    elif args.command == "upload-dataset":
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        verbose = args.verbose
        npcs = neuropacs.init(server_url=server_url, api_key=api_key)
        if connection_id and aes_key :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        if verbose: # Verbose
            upload_status = npcs.upload_dataset(directory="/data", order_id=order_id, callback=lambda data: print(data))
        else:
            upload_status = npcs.upload_dataset(directory="/data", order_id=order_id)

        print(upload_status)
    elif args.command == "run-job":
        connection_id = args.connection_id
        aes_key = args.aes_key
        product_id = args.product_id
        order_id = args.order_id
        npcs = neuropacs.init(server_url=server_url, api_key=api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        job = npcs.run_job(product_id=product_id, order_id=order_id)
        print(job)
    elif args.command == "check-status":
        connection_id = args.connection_id
        aes_key = args.aes_key
        order_id = args.order_id
        npcs = neuropacs.init(server_url=server_url, api_key=api_key)
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
        npcs = neuropacs.init(server_url=server_url, api_key=api_key)
        if (connection_id is not None) and (aes_key is not None) :
            npcs.connection_id = connection_id
            npcs.aes_key = aes_key
        else:  
            npcs.connect()

        results = npcs.get_results(format=format, order_id=order_id)
        print(results)


if __name__ == '__main__':
    main()
