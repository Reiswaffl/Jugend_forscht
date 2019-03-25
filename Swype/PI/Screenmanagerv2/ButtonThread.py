import threading
import time
# import RPi.GPIO as GPIO


class ButtonThread(threading.Thread):
    def __init__(self, screen):
        threading.Thread.__init__(self)
        self.daemon = True
        self.touch = screen.touch

    def run(self):
        print("ButtonThread started")
        while True:
            time.sleep(0.03)
