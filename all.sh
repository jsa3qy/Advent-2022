#!/bin/bash

start=$SECONDS
NUM=$(ls -l ./ | grep -c ^d)
for i in $(seq 1 $NUM); do 
    echo Day $i
    cd day$i
    python3 main.py
    echo
    cd ../
done
echo $(( SECONDS - start )) seconds to finish