#!/bin/bash

pip3 install -e . # install socli as a bash command
pip3 install -r ./socli/requirements.txt # install dependencies for socli

echo "Checking for ~/socless.ini"

if test -f ~/socless.ini ; then
    echo "Config file found"
else
    echo "No file at ~/socless.ini, copying default socless.ini to ~/"
    cp default_socless.ini ~
    mv ~/default_socless.ini ~/socless.ini
fi

echo "Checking for ~/socli_cache"

mkdir -p ~/socli_cache

echo "Checking for git installation to deploy SOCless via Serverless Framework"
if "git" "--version" ; then
    echo "git installed"
else
    echo "git is not installed, please install git before continuing"
fi

echo "Checking for npm installation to deploy SOCless via Serverless Framework"
if "npm" "--version" ; then
    echo "npm installed"
else
    echo "npm is not installed, please install npm before continuing"
fi

# check awscli installed