import subprocess
import serial 
from time import sleep

def listToString(s): 

	# initialize an empty string
	str1 = "" 

	# return string  
	return (str1.join(s))


ser = serial.Serial ("/dev/ttyUSB0", 9600)
data = []

while (1):
	try:
		received_data = ser.read()              
		sleep(0.03)
		data_left = ser.inWaiting()             
		received_data += ser.read(data_left)
		#print (received_data)                   
		ser.write(received_data)
		for i in received_data:
			data.append(chr(i))
		command = listToString(data)
		subprocess.call([command])
		data.clear()
		command = ""
	except:
		print("Error")
		data.clear()
		command = ""




