import RPi.GPIO as GPIO

# define led and button pins
LED_PIN = 11
BUTTON_PIN = 12

print ('Program is starting...')

# set Numbers GPIOs by physical location
GPIO.setmode(GPIO.BOARD)     

 # set led pin's mode is output
GPIO.setup(LED_PIN, GPIO.OUT)

# Set button pin's mode is input, and pull up to high level(3.3V)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		if GPIO.input(BUTTON_PIN) == GPIO.LOW:
			# turn led on
			GPIO.output(LED_PIN, GPIO.HIGH)
			print ('led on ...')
		else:
			# turn led on
			GPIO.output(LED_PIN, GPIO.LOW)
			print ('led off ...')		

except KeyboardInterrupt:
	# turn led off
	GPIO.output(LED_PIN, GPIO.LOW)

	# Release resource
	GPIO.cleanup()
