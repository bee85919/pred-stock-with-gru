#!/bin/bash

INSTANCE_IP=$1

POSTGRES_CONTAINER_ID=$2

./scripts/load.sh $INSTANCE_IP $POSTGRES_CONTAINER_ID

python ./src/conf_data.py

python ./src/prep_data.py

./scripts/train.sh

python ./src/save_result.py 