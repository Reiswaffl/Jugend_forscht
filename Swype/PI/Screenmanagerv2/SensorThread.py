import threading
from Screenmanagerv2.ZXsensorController import *


class SensorThread(threading.Thread):
    def __init__(self, sensor):
        threading.Thread.__init__(self)
        self.daemon = True
        self.sensor = sensor

    def run(self):
        print("SensorThread started")
        while True:
            if self.sensor.receiveActivity():
                self.sensor.callZpos()
            self.sensor.handleDataStraight()
            self.sensor.receiveGesture()
            self.sensor.checkGesture()
            time.sleep(0.03)


sensor = SensorController()
sensorThread = SensorThread(sensor)
