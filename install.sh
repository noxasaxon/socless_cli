#!/bin/bash

pip3 install -e .

echo "Checking for ~/socless.ini"

if test -f ~/socless.ini ; then
    echo "Config file found"
else
    echo "No file at ~/socless.ini, copying default socless.ini to ~/"
    cp default_socless.ini ~
    mv ~/default_socless.ini ~/socless.ini
fi
