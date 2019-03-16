# coding=utf-8
import smbus
import time


class SensorController:
    def __init__(self):
        self.gesture = 0
        self.z_pos = 0
        self.pointZero = 0
        self.z_pos_old = 0
        self.bus = smbus.SMBus(1)
        self.state = 0
        self.activity = False
        self.start_time = time.clock()
        self.tolerance = 4
        print("init done")

    def receiveActivity(self):
        status = self.bus.read_byte_data(0x10, 0x00)
        if status == 129:
            self.activity = True
        elif status == 1:
            self.activity = True
        else:
            self.activity = False
        print(self.activity)
        return self.activity

    def receiveZpos(self):
        self.z_pos_old = self.z_pos
        self.z_pos = self.bus.read_byte_data(0x10, 0x0A)

    def receiveGesture(self):
        self.gesture = self.bus.read_byte_data(0x10, 0x04)

    def checkGesture(self):
        if self.gesture == 1:
            print("swipe")
        elif self.gesture == 2:
            print("swipe 2")

    def handleData(self):
        print(self.state)
        if self.state == 0:
            if self.receiveActivity():
                self.start_time = time.clock()
                self.state = 1
            self.checkGesture()
        elif self.state == 1:
            dt = time.clock() - self.start_time
            if self.receiveActivity():
                if dt > 0.003:
                    self.state = 2
                    self.pointZero = self.z_pos
            else:
                self.state = 0
            self.checkGesture()
        elif self.state == 2:
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos > (self.pointZero + self.tolerance):
                self.state = 3
            elif self.z_pos < (self.pointZero + self.tolerance):
                self.state = 5
        elif self.state == 3:
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos > self.z_pos_old:
                print("Lautstärke HOCH!")
            elif self.z_pos < (self.z_pos_old - (self.tolerance / 2)):
                self.state = 4
        elif self.state == 4:
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos <= self.pointZero:
                self.pointZero = self.z_pos
                self.state = 2
        elif self.state == 5:
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos < self.z_pos_old:
                print("Lautstärke RUNTER!")
            elif self.z_pos == (self.pointZero + (self.tolerance / 2)):
                self.state = 2
        elif self.state == 6:
            if self.receiveActivity() == 0:
                self.state = 0
            elif self.z_pos >= self.pointZero:
                self.pointZero = self.z_pos
        elif self.state == 7:
            pass
        else:
            self.state = 0
