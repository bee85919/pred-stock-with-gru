#!/bin/bash


source ./source.sh


sh      $SH/load.sh
python  $PY/configure.py
python  $PY/prepare.py
sh      $SH/train.sh
python  $PY/save.py
sh      $SH/upload.sh