import time

from pico_la.mcp23s08 import read_pins

NUM_SAMPLES = 10000
SAMPLE_INTERVAL = 100

samples = bytearray(NUM_SAMPLES)

for i in range(NUM_SAMPLES):
    samples[i] = read_pins()
    time.sleep(SAMPLE_INTERVAL)

log = open("samples.b", "wb")
for i in range(NUM_SAMPLES):
    log.write(samples[i])
log.flush()
log.close()



