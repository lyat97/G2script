import RPi.GPIO as GPIO
import os
import time
from multiprocessing import Process

#initialize pins

powerPin = 26 
powerenPin = 27 

#initialize GPIO settings
def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(powerenPin, GPIO.OUT)
	GPIO.output(powerenPin, GPIO.HIGH)
	GPIO.setwarnings(False)

#waits for user to hold button up to 1 second before issuing poweroff command
def poweroff():
	while True:
		GPIO.wait_for_edge(powerPin, GPIO.FALLING)
		os.system("shutdown -h now")
def lcdrun():
	while True:
		os.system("/opt/RetroFlag/lcdnext.sh")
		time.sleep(1)

if __name__ == "__main__":
	#initialize GPIO settings
	init()
	#create a multiprocessing.Process instance for each function to enable parallelism 
	powerProcess = Process(target = poweroff)
	powerProcess.start()
	lcdrunProcess = Process(target = lcdrun)
	lcdrunProcess.start()

	powerProcess.join()
	lcdrunProcess.join()

	GPIO.cleanup()
