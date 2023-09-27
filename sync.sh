#!/bin/bash

set -e

source ./env.sh

rsync -a ./Dockerfile $sub_domain.$domain:~/
rsync -a ./docker-compose.yaml $sub_domain.$domain:~/