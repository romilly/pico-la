from machine import Pin
from time import sleep

pin2 = machine.Pin(2, Pin.OUT)

while True:
    pin2.value(0)
    sleep(0.01)
    pin2.value(1)
    sleep(0.01)
    
    