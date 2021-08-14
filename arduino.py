import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
def move(x):
    time.sleep(1.5)
    arduino.write(x.encode())

move('0')