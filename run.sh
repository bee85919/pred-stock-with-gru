#!/bin/bash

python conf_data.py

python prep_data.py

./train.sh

python save_result.py