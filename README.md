# Pico Logic Analyzer

MicroPython code for a simple Logic Analyser for the Raspberry Pi Pico/Pico W.

Here's the board:

![image](http://images.rareschool.com/img/ec705cc2-0814-11ed-9d6e-8fbd78adec0c-picola.jpg)

In this close-up you can see that there are eight header sockets and eight header pins connected to the eight sampling inputs.

![image](http://images.rareschool.com/img/ce0f5528-0817-11ed-9d6e-8fbd78adec0c-pico-la-headers.jpg)


## Plan

The first iteration will just capture a stream of 8-bit digital data and save 
it to a file. I'll use mpremote to copy the file locally so I can work with it. 

The minimalist MCP23S08 is working. I'll write a full driver when I have time. 

The driver that I'm using assumes that

1. The MCP23S08 has address lines A0, A1 at ground.
2. All that's needed is to set the port to Input mode and then read its values repeatedly.


So the driver doesn't cope with addresses other than the default, and does not use any additional features of the chip.

## The minimalist driver

Here's the test code:

```python
import time

from mcp23s08 import read_pins

NUM_SAMPLES = 1000000
SAMPLE_INTERVAL = 1000

samples = bytearray(NUM_SAMPLES)

for i in range(NUM_SAMPLES):
    samples[i] = read_pins()
    time.sleep_us(SAMPLE_INTERVAL)
    

with open("samples.b", "wb") as log
    log.write(samples)
    log.flush()
```

Here's the driver code:

```python
# Inspired by Tony DiCola's Adafruit CircuitPython library
# https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx
# and then hacked beyond recognition by Romilly Cocking
# MIT License
"""

"""

from machine import Pin, SPI

SCK = Pin(2)
SPI_TX = Pin(3)
SPI_RX = Pin(4)

# create SPI device
spi = SPI(0, baudrate=100000, sck=SCK, mosi=SPI_TX, miso=SPI_RX)

# NCS - Not Chip Select - goes LOW to enable the chip
cs = Pin(15, mode=Pin.OUT, value=1)


OUT_BUFFER = bytearray(3)
IN_BUFFER = bytearray(3)
CODE_READ = 0x41
CODE_WRITE = 0x40

IODIR = 0x00
GPIO = 0x09

# Write a byte to the specifice register
def spi_write(register: int, value: int) -> None:
    cs.value(0)  # select chip
    OUT_BUFFER[0] = CODE_WRITE
    OUT_BUFFER[1] = register & 0xFF
    OUT_BUFFER[2] = value & 0xFF
    spi.write(OUT_BUFFER)
    cs.value(1)  # de-select


# read a byte from the specified register
def spi_read(register):
    cs.value(0)  # select chip
    OUT_BUFFER[0] = CODE_READ
    OUT_BUFFER[1] = register & 0xFF
    spi.write_readinto(OUT_BUFFER, IN_BUFFER)
    cs.value(1)  # de-select
    return IN_BUFFER[2]


# read a byte of data from the input pins
def read_pins():
    return spi_read(GPIO)


# set all pins to be inputs
spi_write(IODIR, 0xFF)
```
