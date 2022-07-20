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




