import smbus
import time
bus = smbus.SMBus(0)
address = 0x10

def write(value):
    bus.write_byte_data(address, 0, value)
    return -1


def range():
    range1 = bus.read_byte_data(address, 2)
    range2 = bus.read_byte_data(address, 3)
    range3 = (range1 << 8) + range2
    return range3


while True:
    write(0x51)
    time.sleep(0.7)
    rng = range()
    print(rng)
