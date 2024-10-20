# TimeLapse
TimeLapse for RPi


There's only 3 files required and a change to 1 file.

Setup:
Full version of Raspbian on a RPi with enough storage space (I used a 512Gb SD).

**sudo apt install -y python3-kms++**

**sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev**

**sudo pip3 install numpy --upgrade**

**sudo apt install python3-crontab**

**sudo apt install python3-picamera2 --upgrade**

**Edit the config file:**

**sudo nano /boot/firmware/config.txt**

**Update**

camera_auto_detect=0

**Add at end of file**

dtoverlay=imx219,cam0

dtoverlay=imx219,cam1

**comment:** You technically only need one of the 2. Depending on which port you plugged the camera into. I added both (I'm using a RPi 5)





Exit nano and reboot



To test: 
**rpicam-vid**

Then, ensure you're NOT root, open a terminal and type the following:

cd ~

**mkdir -p TimeLapse\photos**

Copy "timelapse.py" into the folder "\home\USERNAME\TimeLapse"

Copy "create_vid_ffmpeg.sh" into "\home\USERNAME\TimeLapse\photos"

Copy "combine.sh" into "\home\USERNAME\TimeLapse\photos"

Open the file "timelapse.py" in text editor (or a code editor like Geany)
Replace every instance of USERNAME with the username of your RPi. Ensure that you only change USERNAME. If there are " or ', leave them.
Do the same with "create_vid_ffmpeg.sh"
Do the same with "combine.sh"

then, run:

**cd ~\TimeLapse\photos**

**chmod +x .\create_vid_ffmpeg.sh**

**chmod +x .\combine.sh**

Everything is now configured.

Usage:

python3 ~\TimeLapse\timelapse.py _day_number_ _number_of_photos_to_take_

The script will take a photo every 30 seconds (can be configured in the script). For 18hrs, use 2160 (hrs * 60 * 2)

eg. Day 3, 18hrs:

**python3 ~\TimeLapse\timelapse.py 3 2160**

This will start taking photos. It will also do the following:

Create a CronJob to automatically start the next day at 04:00 the next day, incrementing the day number. The time to start can be configured in the script (timelapse.py).
It also creates a CronJob to convert the current day into a video. This script runs at 22:05 on the same day. The time can also be configured in the script (timelapse.py).
In the script (timelapse.py), I've commented the 2 areas that need to be changed for the photos and video creation.

"Change the photo schedule here!" and "Change the video creation schedule here!"

If you manually run the script (the first day), there might will be some issues with the amount of photos it takes and for how long. This can be circumvented in the following way:

1. Work out how many hours you still want photos to be taken of today (eg. 5hrs)
2. Take this value and perform the following arithmetic:

   hrs * 60 * 2

   (5 * 60 * 2 = 600)

   **python3 ~\TimeLapse\timelapse.py 3 600**

   This will take photos for another 5hrs only. But the scheduled task will then also be configured for 5hrs.
3. We then need to fix the scheduled task:
   **crontab -e** (if asked with editor, use nano. vi is broken on Debian)
4. In the line where the task is created, change the 600 to the number you previously calculated.
5. That's it. It should then process automatically the next day.


To kill the camera task triggered by CronTab, run the following:

**top -p $(pgrep -d',' python3)**

This will show a "python3" process that your username is running. Take a note of the process id

**kill "process_id"**


The photos will be created in **/home/USERNAME/TimeLapse/photos/** There will be a new folder for each day (eg. **/home/USERNAME/TimeLapse/photos/day1/photo0001.jpg**)

The videos will be created in **/home/USERNAME/TimeLapse/photos/** There will be individual files (eg. **/home/USERNAME/TimeLapse/photos/day1.mp4**)

The script **/home/USERNAME/TimeLapse/photos/combine.sh** will combine all videos (in chronological order) found in **/home/USERNAME/TimeLapse/photos/**

So if you want certain videos to be excluded, move them into a temporary folder. Alternatively:
1. Comment out the last line of the script (# ffmpeg...)
2. Run the script. This will create a file "vidlist.txt"
3. Open this file and delete the lines of the videos that you do not want to include
4. Open **combine.sh** again, copy the last line into your clipboard (the one you commented out in step 1)
5. Exit to terminal
6. Paste clipboard and run (make sure that the # is not in the line)
7. This will then use your modified "vidlist.txt" to create the video. You can also play around with the order of the individual videos if you like. But that doesn't really make sense.
