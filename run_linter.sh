#!/bin/bash
PIPENV="$(which pipenv)"

if [ $? -eq 1 ] 
then
   python3 "$(which pip)"  install pipenv
fi

pipenv install --dev
pipenv run pylint src tests