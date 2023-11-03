#!/bin/bash

SH=./scripts
PY=./src

export PEM_PATH=$1
export INSTANCE_IP=$2
export POSTGRES_CONTAINER_ID=$3
export RESULT_PATH=/home/ubuntu/work/pred-stock-with-gru/data/result/result.csv
export RESULT_INSTANCE_PATH=/home/ubuntu/result.csv
export RESULT_POSTGRESQL_PATH=/home/result.csv
export DB_NAME="test01"
export TABLE_NAME="pred"