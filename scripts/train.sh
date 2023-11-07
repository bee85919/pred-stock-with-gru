#!/bin/bash





cnt=0
while true; do
  ((cnt++))
  
  batch_size=$(cat ./input/batch_size.txt)
  syms=$(cat ./input/syms.txt)

  if [[ "$syms" == "[]" ]]; then
    echo "작업이 완료되었습니다."
    break
  fi

  echo "Batch: ${cnt}/${batch_size}"

  python src/train.py
done