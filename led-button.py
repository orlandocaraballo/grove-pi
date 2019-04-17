#!/usr/bin/env python3
import RPi.GPIO as GPIO

LED_PIN = 11    # define the LED_PIN
BUTTON_PIN = 12    # define the BUTTON_PIN

def setup():
	print ('Program is starting...')
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LED_PIN, GPIO.OUT)   # Set LED_PIN's mode is output
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BUTTON_PIN's mode is input, and pull up to high level(3.3V)

def loop():
	while True:
		if GPIO.input(BUTTON_PIN) == GPIO.LOW:
			GPIO.output(LED_PIN,GPIO.HIGH)
			print ('led on ...')
		else :
			GPIO.output(LED_PIN,GPIO.LOW)
			print ('led off ...')		

def destroy():
	GPIO.output(LED_PIN, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
