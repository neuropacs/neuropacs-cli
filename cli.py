import argparse
import os
import neuropacs

def main():
    # Arguments from Docker container
    server_url = os.getenv('SERVER_URL')
    api_key = os.getenv('API_KEY')
    # client = "api"

    parser = argparse.ArgumentParser(description="Neuropacs CLI tool.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Neuropacs sub-command help')

    # connect_parser = subparsers.add_parser('connect', help='Creates a new session with Neuropacs.')

    new_job_parser = subparsers.add_parser('new-job', help='Creates a Neuropacs order. Returns a unique order ID.')
    new_job_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID.")

    upload_dataset_parser = subparsers.add_parser('upload-dataset', help='Uploads a dataset to Neuropacs. Returns a unique datasetId.')
    upload_dataset_parser.add_argument('--dataset-path', type=str, required=True, help="Path to the dataset to be uploaded")
    upload_dataset_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    upload_dataset_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID.")
    

    run_job_parser = subparsers.add_parser('run-job', help='Executes a Neuropacs order.')
    run_job_parser.add_argument('--product-id', type=str, required=True, help="Neuropacs product to be executed. ['PD/MSA/PSP-v1.0']")
    run_job_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    run_job_parser.add_argument('--dataset-id', type=str, required=True, help="Base64 dataset ID.")
    run_job_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID.")

    check_status_parser = subparsers.add_parser('check-status', help='Retrieves current status of a running Neuropacs order.')
    check_status_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    check_status_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID.")
    check_status_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID.")
    
    get_results_parser = subparsers.add_parser('get-results', help='Retrieves results from completed Neuropacs order.')
    get_results_parser.add_argument('--format', type=str, required=True, help="Format of result file. ['TXT', 'XML', 'JSON']")
    get_results_parser.add_argument('--order-id', type=str, required=True, help="Base64 order ID.")
    get_results_parser.add_argument('--dataset-id', type=str, required=False, help="Base64 dataset ID.")
    get_results_parser.add_argument('--connection-id', type=str, required=False, help="Base64 connection ID.")



    args = parser.parse_args()


    if args.command == "connect":
        npcs = neuropacs.init(server_url, api_key)
        conn = npcs.connect()
        print(conn)
    elif args.command == "new-job":
        connection_id = args.connection_id
        npcs = neuropacs.init(server_url, api_key)
        if connection_id is not None:
            order = npcs.new_job(connection_id)
        else:
            conn = npcs.connect()
            order = npcs.new_job()
        print(order)
    elif args.command == "upload-dataset":
        dataset_path = args.dataset_path
        connection_id = args.connection_id
        order_id = args.order_id
        npcs = neuropacs.init(server_url, api_key)
        if connection_id is not None:
            datasetID = npcs.upload_dataset(dataset_path, order_id, connection_id)
        else:
            conn = npcs.connect()
            datasetID = npcs.upload_dataset(dataset_path, order_id)
        print(datasetID)
    elif args.command == "run-job":
        connection_id = args.connection_id
        product_id = args.product_id
        order_id = args.order_id
        dataset_id = args.dataset_id
        npcs = neuropacs.init(server_url, api_key)
        if connection_id is not None:
            job = npcs.run_job(product_id, order_id, dataset_id, connection_id)
        else:  
            conn = npcs.connect()
            job = npcs.run_job(product_id, order_id, dataset_id)
        print(job)
    elif args.command == "check-status":
        connection_id = args.connection_id
        order_id = args.order_id
        dataset_id = args.dataset_id
        npcs = neuropacs.init(server_url, api_key)
        if connection_id is not None:
            job_status = npcs.check_status(order_id, dataset_id, connection_id)
        else:
            conn = npcs.connect()
            job_status = npcs.check_status(order_id, dataset_id)
        print(job_status)
    elif args.command == "get-results":
        connection_id = args.connection_id
        order_id = args.order_id
        dataset_id=args.dataset_id
        format = args.format
        npcs = neuropacs.init(server_url, api_key)
        if connection_id is not None:
            results = npcs.get_results(format, order_id, dataset_id, connection_id)
        else:
            conn = npcs.connect()
            results = npcs.get_results(format, order_id, dataset_id)
        print(results)






    

if __name__ == '__main__':
    main()
