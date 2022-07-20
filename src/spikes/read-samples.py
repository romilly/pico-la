with open('/home/romilly/git/active/pico-la/data/samples.b','rb') as sample_file:
    samples = sample_file.read()

for b in samples:
    print("%x" % b)
