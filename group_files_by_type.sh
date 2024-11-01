#!/bin/bash

# This script groups files in the current directory by their extension

# Use associative array to store file names by extension
declare -A extension_groups

# Iterate over files in the current directory
for file in *; do
    if [[ -f "$file" ]]; then
        ext="${file##*.}"
        extension_groups["$ext"]+="$file "
    fi
done

# Print files grouped by extension
for ext in "${!extension_groups[@]}"; do
    echo "Files with .$ext extension:"
    for file in ${extension_groups[$ext]}; do
        echo "  $file"
    done
    echo
done
