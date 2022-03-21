import time
import serial

ser = serial.Serial(            
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

while (1):
    command = input("Type your command to be sent to the remote terminal:   ")
    ser.write(command.encode())
    command = ""
    time.sleep(1)




