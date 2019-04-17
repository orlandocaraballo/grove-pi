import RPi.GPIO as GPIO
import time

# store the pin number in a const
LED_PIN = 11

# initial setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

# loop forever and blink leds
try:
  while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    print('...led on')
    time.sleep(.25)

    GPIO.output(LED_PIN, GPIO.LOW)
    print('led off...')
    time.sleep(.25)

except KeyboardInterrupt:
  GPIO.output(LED_PIN, GPIO.LOW)
  GPIO.cleanup()
