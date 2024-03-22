#To use this wrapper:
#1.Make this script executable: chmod +x wrapper.sh
#2.Move this script into /usr/local/bin/: sudo mv wrapper.sh /usr/local/bin/
#3.Now you can use the 'neuropacs' command directly to invoke the cli


#!/bin/bash

DOCKER_IMAGE="neuropacs"

docker run --rm "$DOCKER_IMAGE" "$@"
