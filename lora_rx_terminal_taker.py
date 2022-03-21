import subprocess
import serial 
from time import sleep

ser = serial.Serial ("/dev/ttyUSB0", 9600)

while (1):
    received_data = ser.read()              
    sleep(0.03)
    data_left = ser.inWaiting()             
    received_data += ser.read(data_left)
    print (received_data)                   
    ser.write(received_data)
    subprocess.call([received_data])





