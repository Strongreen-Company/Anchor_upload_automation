#!/bin/bash
#shellcheck disable=SC2163

while IFS= read -r linha || [[ -n "$linha" ]]; do
    echo "$linha"
    export "$linha"
done <".env"
