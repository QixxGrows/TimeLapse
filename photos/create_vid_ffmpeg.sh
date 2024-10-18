#!/bin/bash

if [ -z "$1" ]; then
  echo "Include the day number as argument 1"
  exit 1
fi

ffmpeg \
  -framerate 120 \
  -pattern_type glob \
  # Replace USERNAME with your username
  -i "/home/USERNAME/TimeLapse/photos/day$1/photo*.jpg" \
  /home/USERNAME/TimeLapse/photos/day$1.mp4
