#!/bin/bash
count=0
while true; do
  ((count++))
  python train_models.py
  total_symbols=$(cat ./input/symbols_length.txt)
  echo "processing: ${count}/${total_symbols}"

  if [[ ! $(cat ./input/symbols.txt) ]]; then
    echo "작업이 완료되었습니다."
    break
  fi
done