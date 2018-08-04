import serial

arduino = serial.Serial('/dev/ttyACM0',9600)

while True:
	VALOR_ARDUINO = arduino.readline()
	print(VALOR_ARDUINO.decode("utf-8"))
	
	