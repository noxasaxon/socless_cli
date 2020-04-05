#!/bin/bash


pip3 install -e . # install socless_cli as a bash command

SOCLESS_CLI_DATA_DIR="socless_cli_data"

echo "Checking for ~/$SOCLESS_CLI_DATA_DIR"

mkdir -p ~/$SOCLESS_CLI_DATA_DIR

echo "Checking for ~/$SOCLESS_CLI_DATA_DIR/socless.ini"

if test -f ~/$SOCLESS_CLI_DATA_DIR/socless.ini ; then
    echo "Config file found"
else
    echo "No file at ~/$SOCLESS_CLI_DATA_DIR/socless.ini, copying default socless.ini to ~/$SOCLESS_CLI_DATA_DIR"
    cp default_socless.ini ~/$SOCLESS_CLI_DATA_DIR
    mv ~/$SOCLESS_CLI_DATA_DIR/default_socless.ini ~/$SOCLESS_CLI_DATA_DIR/socless.ini
fi

echo "Checking for ~/$SOCLESS_CLI_DATA_DIR/socless_cli_cache"

mkdir -p ~/$SOCLESS_CLI_DATA_DIR/socless_cli_cache

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