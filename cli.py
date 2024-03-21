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

    # parser for the "init" command
    init_parser = subparsers.add_parser('init', help='Initializes the Neuropacs tool.')
    init_parser.add_argument('server_url', type=str, help='The URL of your Neuropacs instance.')
    init_parser.add_argument('api_key', type=str, help='Provided API key.')

    connect_parser = subparsers.add_parser('connect', help='Creates a session with Neuropacs.')
    connect_parser.add_argument('server_url', type=str, help='The URL of your Neuropacs instance.')
    connect_parser.add_argument('api_key', type=str, help='Provided API key.')

    # parser.add_argument('--connect', help='Creates a session with Neuropacs.')
    # parser.add_argument('--new-job', help='Creates a Neuropacs order. Returns a unique orderId.')
    # parser.add_argument('--upload-dataset', help='Uploads a dataset to Neuropacs. Returns a unique datasetId.')
    # parser.add_argument('--run-job', help='Executes a Neuropacs order. Returns a status code.')
    # parser.add_argument('--check-status', help='Retrieves current status of a running Neuropacs order.')
    # parser.add_argument('--get-results', help='Retrieves results from completed Neuropacs order.')

    args = parser.parse_args()
    

    if args.command == "connect":
        npcs = neuropacs.init(server_url, api_key, "cli")
        conn = npcs.connect()
        print(conn)
    elif args.command == "new-job":
        npcs = neuropacs.init(server_url, api_key)
        conn = npcs.connect()
        order = npcs.new_job()
        print(order)
    elif args.command == "upload-dataset":
        npcs = neuropacs.init(server_url, api_key)
        conn = npcs.connect()
        datasetID = npcs.upload_dataset("../dicom_examples/DICOM_small")
    

if __name__ == '__main__':
    main()
