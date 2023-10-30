#!/bin/bash

cnt=0
while true; do
  ((cnt++))
  
  symbols_len=$(cat ./input/symbols_length.txt)
  symbols_txt=$(cat ./input/symbols.txt)

  if [[ "$symbols_txt" == "[]" ]]; then
    echo "작업이 완료되었습니다."
    break
  fi

  echo "Batch: ${cnt}/${symbols_len}"

  python train_models.py    
done