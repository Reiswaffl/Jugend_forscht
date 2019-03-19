import time
import serial

shortcutTime = time.time()
# ser = serial.Serial(
#    port='/dev/ttyAMA0',
#    baudrate=115200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
# )


def write_Shortcut(shortcut):
    global shortcutTime
    if time.time() > shortcutTime + 0.5:
        print(shortcut)
        if not shortcut == "c3":
            shortcutTime = time.time()
    # ser.write(bin('SC' + shortcut + '\n'))


def write_Movement(x, y):
    global shortcutTime
    if time.time() - 0.1 > shortcutTime:
        print(x, y)
    # ser.write(bin('M' + x + ',' + y + '\n'))


def write_write(x):
    global shortcutTime
    if time.time() - 0.1 > shortcutTime:
        print(x)
        shortcutTime = time.time()
        # ser.write(bin('W' + x + '\n'))


def write_release():
    global shortcutTime
    if time.time() - 0.1 > shortcutTime:
        print('R')
    # ser.write(bin('R' + '\n'))


def write_soundchange(operator):
    global shortcutTime
    if time.time() - 0.1 > shortcutTime:
        print(operator)
        shortcutTime = time.time()
    # ser.write(bin('S' + operator + '\n'))


def write_spotifycom(command):
    global shortcutTime
    if time.time() - 0.1 > shortcutTime:
        print(command)
        shortcutTime = time.time()
    # ser.write(bin('SP' + command + '\n'))


def receive_spotifycom(command):
    write_spotifycom(command)
    commandinput = 'SP\n'  # ser.readline()
    commandinput = commandinput.replace('\n', '').replace('SP', '')
    return commandinput
