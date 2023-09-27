#!/bin/bash

set -e

source ./env.sh

rsync -a ./Dockerfile root@$sub_domain.$domain:~/
rsync -a ./docker-compose.yaml root@$sub_domain.$domain:~/