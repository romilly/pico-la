# Project journal for Pico-LA

## Sunday 10 July 2022

I wrote a quick spike to access an MCP23S08 SPI prt expander from 
MicroPython and realized that it does all I need for the first version of 
Pico-LA!

## Wednesday 20 July 2022

I'm about to start the first experiment.

I am going to use another Pico sending GPIO data as the signal source.

So

1. Signal capture
   1. Set up a second Pico driving GPIOs.
   2. Write code on the W to save the data
   3. Print the result and use `mu` to plot it
2. Generate svg
   1. I can write and test this code on any Python system.
   2. Once it's working, move it to the Pico and adapt Alasdair Allan's web 
      page example from [Connecting to the Internet with Raspberry Pi Pico W](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf)


