#!/bin/bash

while read -r linha; do
    echo "$linha"
done <.env
