#This is a basic script to be run onboard the Pi for taking a test picture
import picamera2
import picamera
from picamera2 import Picamera2, Preview
from libcamera import controls
import time
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")
