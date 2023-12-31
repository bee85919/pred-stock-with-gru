#!/bin/bash


SH=./scripts
PY=./src


export PEM_PATH=PEM_PATH
export INSTANCE_IP=INSTANCE_IP
export POSTGRES_CONTAINER_ID=POSTGRES_CONTAINER_ID
export RESULT_PATH=RESULT_PATH
export RESULT_INSTANCE_PATH=RESULT_INSTANCE_PATH
export RESULT_POSTGRESQL_PATH=RESULT_POSTGRESQL_PATH
export DB_NAME=DB_NAME
export TABLE_NAME=TABLE_NAME
export DATE=$(date '+%Y, %m, %d')
export PERIOD=300