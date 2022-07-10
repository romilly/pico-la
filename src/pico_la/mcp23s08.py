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





