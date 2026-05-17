#!/bin/bash

temp_dir=~/lab2

echo "Cleaning files older than 7 days in $temp_dir..."

find $temp_dir -type f -mtime +7 -exec rm -f {} \;

echo "Cleanup completed successfully."
