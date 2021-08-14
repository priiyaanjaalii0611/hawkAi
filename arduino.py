import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
def move(x,y):
    x=str(x)
    y=str(y)
    arduino.write(x.encode())
    time.sleep(0.1)
    # arduino.write(y.encode())
    # print(arduino.readline())

move(50,0)
print('huh')