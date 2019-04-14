from flask import Flask
import grovepi
import time

SENSOR_ID = 2
LEADING_ZERO = False

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route('/set-display/<number>')
def change_time(number):
	print("Sending message")
	grovepi.fourDigit_segment(SENSOR_ID, 0, 0x9) # 15 = F
	grovepi.fourDigit_segment(SENSOR_ID, 1, 63) # 15 = F
	grovepi.fourDigit_segment(SENSOR_ID, 2, 63) # 15 = F
	grovepi.fourDigit_segment(SENSOR_ID, 3, 56) # 15 = F
	
	print("Sleeping for 2 seconds")
	time.sleep(2)
	
	print("Sending message")
	grovepi.fourDigit_number(SENSOR_ID, int(number), LEADING_ZERO)

    	
	return "I changed the display! {}".format(number)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
