#!/bin/bash

input_dir="./original"
output_dir="./results"

for file in "$input_dir"/*.avi; do
    if [ -f "$file" ]; then
        base=$(basename "$file")
        filename="${base%.*}"
        output_file="${output_dir}/${filename}_deinterlaced.avi"

        ffmpeg -i "$file" -vf yadif -c:v libx264 -crf 23 -c:a copy "$output_file"
    fi
done

