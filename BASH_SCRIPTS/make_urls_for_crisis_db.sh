#!/bin/bash

echo "Before appending the files..."
source_abs_dir="outputs/output_urls/"
destination_abs_dir="/home/majid/dev/seshat/seshat/seshat/apps/crisisdb/"
#destination_abs_dir="/home/majid/Downloads/"

destination_file="urls.py"

full_file_path=$source_abs_dir$destination_file

if test -f "$full_file_path";
then
    echo "The file ($full_file_path) exists on your filesystem."
else
    echo "WARNING: The file ($full_file_path) DOES NOT exist on your filesystem."
fi

cp $full_file_path $destination_abs_dir$destination_file
echo "Contents of the file ($full_file_path) successfully transferred to: $destination_abs_dir$destination_file!"
echo "================="
echo "SUCCESS!"