import smbus
import time


class SensorController:
    def __init__(self):
        self.gesture = 0
        self.z_pos = 0
        self.bus = SMBus(1)
        self.state = 0
        self.start_time = time.clock()

    def receiveXpos(self):
        # self.gesture = self.bus.read_byte_data(0x10, 0x04)
        self.z_pos = self.bus.read_byte_data(0x10, 0x0A)

    def receiveGesture(self):
        self.gesture = self.bus.read_byte_data(0x10, 0x04)

    def checkGesture(self):
        if self.gesture == 0x10:
            print("swipe")
        elif self.gesture == 0x20:
            print("swipe 2")

    def handleData(self):
        if self.state == 0:
            if self.z_pos > 0:
                self.start_time = time.clock()
                self.state = 1
            self.checkGesture()
        elif self.state == 1:
            dt = self.start_time - time.clock()
            if self.z_pos > 0:
                if dt < 1:
                    self.state = 2
            elif self.z_pos == 0:
                self.state = 0
            self.checkGesture()
        elif self.state == 2:
            pass
        elif self.state == 3:
            pass
        elif self.state == 4:
            pass
        elif self.state == 5:
            pass
        elif self.state == 6:
            pass
        elif self.state == 7:
            pass
        else:
            self.state = 0


# sensorController = SensorController()

# while True:
    # sensorController.receiveData()
    # sensorController.handleData()
    # time.sleep(0.2)
