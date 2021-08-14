import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
def move(x,y):
    time.sleep(1.5)
    arduino.write(x.encode())
    time.sleep(1.5)
    arduino.write(y.encode())

move('0','0')