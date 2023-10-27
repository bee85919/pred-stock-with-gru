#!/bin/bash
count=0
while true; do
  ((count++))
  python train_models.py
  echo "train_models.py가 ${count}번 실행되었습니다."

  if [[ ! $(cat ./input/test.txt) ]]; then
    echo "작업이 완료되었습니다."
    break
  fi
done