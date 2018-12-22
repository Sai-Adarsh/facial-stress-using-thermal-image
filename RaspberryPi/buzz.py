from gpiozero import Buzzer
from time import sleep
import sys

flag=sys.argv[1]

buzzer = Buzzer(17)

if flag == "1":
	buzzer.on()
	sleep(0.2)
	buzzer.off()

if flag == "0":
	buzzer.on()
	sleep(0.1)
	buzzer.off()
	sleep(0.1)
	buzzer.on()
	sleep(0.1)
	buzzer.off()
