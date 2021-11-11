#!/bin/bash

# Auto update new packages on requirements
if ! pip3 list | grep "pipreqs"; then
    pip3 install pipreqs
fi
pipreqs ./server/ --force
echo "uvicorn==0.15.0" >> ./server/requirements.txt 