#!/bin/bash

if [ ! -f "$1" ]; then
	echo "File '$1' not found!"
	exit 1
fi

filename=$(basename -- "$1")
name="${filename%.*}"

xxd -r "$1" > "./$name"