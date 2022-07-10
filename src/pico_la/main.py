import time

from mcp23s08 import read_pins

NUM_SAMPLES = 10000
SAMPLE_INTERVAL = 100

samples = bytearray(NUM_SAMPLES)

for i in range(NUM_SAMPLES):
    samples[i] = read_pins()
    time.sleep_us(SAMPLE_INTERVAL)

log = open("samples.b", "wb")
log.write(samples)
log.flush()
log.close()



