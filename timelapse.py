from picamera2 import Picamera2, Preview
from crontab import CronTab
import time
import os
import sys
import subprocess

def capture_photo(iterations, sleep_duration, save_directory):
	for i in range(iterations):		
		# Replace USERNAME with your username	
		photo_path = '/home/USERNAME/TimeLapse/photos/' + save_directory
		os.makedirs(photo_path, exist_ok=True)
		photo_path += '/photo{0:04d}.jpg'.format(i)
		picam2.capture_file(photo_path)
		time.sleep(sleep_duration)	
	
def create_cronjob(day_num, photo_count):
	subprocess.run(["crontab", "-r"])
	# Replace USERNAME with your username
	cronJob = CronTab(user='USERNAME')
	cmd = 'python3 /home/USERNAME/TimeLapse/timelapse.py ' + str(day_num) + ' ' + str(photo_count)
	job = cronJob.new(command=cmd)
	job.minute.on(0)
	job.hour.on(4)
	cronJob.write()

def create_cronjob_video(day_num):	
	# Replace USERNAME with your username
	cronJob = CronTab(user='USERNAME')
	cmd = 'sh /home/USERNAME/TimeLapse/photos/create_gif_ffmpeg.sh ' + str(day_num)
	job = cronJob.new(command=cmd)
	job.minute.on(5)
	job.hour.on(22)
	cronJob.write()
    
if __name__ == "__main__":
	create_cronjob(int(sys.argv[1]) + 1, int(sys.argv[2]))
	create_cronjob_video(int(sys.argv[1]))
	picam2 = Picamera2()

	camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
	picam2.configure(camera_config)

	picam2.start()

	#for j in range(int(sys.argv[1]), 100):
		# 2160 photos taken at 30 second intervals is 18hrs
		# 1440 photos taken at 30 second intervals is 12hrs
		#capture_photo(int(sys.argv[2]), 30, 'day' + str(j))
		
		# 21600secs is 6hrs
		# 43200secs is 12hrs
		#time.sleep(int(sys.argv[3]))	
	
	capture_photo(int(sys.argv[2]), 30, 'day' + sys.argv[1])
	
	picam2.close()
	
# convert -delay 10 -loop 0 photo*.jpg animation.gif


