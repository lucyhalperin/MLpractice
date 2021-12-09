#!/bin/bash

# creating venv and installing requirements
virtualenv venv 
source venv/bin/activate 
pip3 install -r requirements.txt

# run python code inside virtualenv
python3 main.py \
--hyperparamX 4
