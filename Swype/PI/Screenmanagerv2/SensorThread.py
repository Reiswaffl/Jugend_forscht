import threading
from Screenmanagerv2.ZXsensorController import *


class Sensor(threading.Thread):
    def __init__(self, sensor):
        threading.Thread.__init__(self)
        self.daemon = True
        self.sensor = sensor
        print('sensor init done')

    def run(self):
        print("SensorThread initialized")
        while True:
            if self.sensor.receiveActivity():
                self.sensor.callZpos()
            self.sensor.handleDataStraight()
            self.sensor.receiveGesture()
            self.sensor.checkGesture()
            self.sensor.handleDataStraight()
            time.sleep(0.03)


sensor = SensorController()
sensorThread = Sensor(sensor)
