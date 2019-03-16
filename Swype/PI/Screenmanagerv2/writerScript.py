import time

shortcutTime = time.time()


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
        # ser.write(bin('W' + x + '\n'))


def write_release():
    print("release all")
    # ser.write(bin('R' + '\n'))


def write_soundchange(operator):
    print(operator)
    # ser.write(bin('S' + operator + '\n'))
