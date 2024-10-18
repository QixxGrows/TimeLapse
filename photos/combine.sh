#!/bin/bash
rm -rf /home/USERNAME/TimeLapse/photos/vidlist.txt 
search_dir=/home/USERNAME/TimeLapse/photos
for filename in "$search_dir"/day*.mp4
do
  echo "file '$filename'" >> /home/USERNAME/TimeLapse/photos/vidlist.txt
done
ffmpeg -safe 0 -f concat -i "/home/USERNAME/TimeLapse/photos/vidlist.txt" -c copy /home/USERNAME/TimeLapse/photos/combined.mp4
