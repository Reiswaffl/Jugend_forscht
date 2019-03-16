# coding=utf-8
# import smbus
from Screenmanagerv2.writerScript import *


class SensorController:
    def __init__(self):

        self.gesture = 0
        self.z_pos = 0
        self.pointZero = 0
        self.z_pos_old = 0
        # self.bus = smbus.SMBus(1)
        self.state = 0
        self.activity = False
        self.start_time = time.clock()
        self.tolerance = 10
        self.t2 = 3
        self.t3 = 10
        self.lastActivity = False

    def receiveActivity(self):
        # status = self.bus.read_byte_data(0x10, 0x00)
        #if status == 129:
        #    self.activity = True
        #    self.lastActivity = True
        #elif status == 1:
        #    self.activity = True
        #    self.lastActivity = True
        #else:
        #    if self.lastActivity:
        #        self.lastActivity = False
        #        self.activity = True
        #    else:
        #        self.activity = False
        ## print(self.activity)
        #return self.activity
        return False

    def receiveZpos(self):
        self.z_pos_old = self.z_pos
        # self.z_pos = self.bus.read_byte_data(0x10, 0x0A)
        return self.z_pos

    def callZpos(self):
        global z_pos
        data = 0
        notzero = 0
        for x in range(0, 8):
            # datacall = self.bus.read_byte_data(0x10, 0x0A)
            #if not datacall == 0:
            #    data += datacall
            #    notzero += 1
            pass
        if notzero >= 5:
            pos = data / notzero
        else:
            pos = 0
        self.z_pos_old = self.z_pos
        self.z_pos = pos
        return pos

    def receiveGesture(self):
        # self.gesture = self.bus.read_byte_data(0x10, 0x04)
        self.gesture = 0

    def checkGesture(self):
        if self.gesture == 1:
            print("swipe")
            write_Shortcut('swipe')
        elif self.gesture == 2:
            print("swipe 2")
            write_Shortcut('swipe2')

    def handleData(self):
        print("_______wrong_____")
        if self.state == 0:
            if self.receiveActivity():
                self.start_time = time.clock()
                self.state = 1
            self.checkGesture()
        elif self.state == 1:
            # print("state 1")
            dt = time.clock() - self.start_time
            if self.receiveActivity():
                if dt > 0.002:
                    self.state = 2
                    self.pointZero = self.z_pos
                    print("||||" + str(self.z_pos) + "||||")
            else:
                self.state = 0
            self.checkGesture()
        elif self.state == 2:
            print("state 2")
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos == 0:
                self.state = 0
            elif self.z_pos > (self.pointZero + self.tolerance):
                print("switch to state 3")
                self.state = 3
            elif self.z_pos < (self.pointZero - self.tolerance):
                print("switch to state 5")
                self.state = 5
            else:
                write_soundchange('+')
                write_soundchange('-')
                pass
        elif self.state == 3:
            print("state 3")
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos > self.z_pos_old:
                print("Lautstärke HOCH!")
                write_soundchange('+')
            elif self.z_pos < (self.z_pos_old - (self.tolerance / 2)):
                self.state = 4
        elif self.state == 4:
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos <= self.pointZero:
                self.pointZero = self.z_pos
                self.state = 2
        elif self.state == 5:
            print("state 5")
            if not self.receiveActivity():
                self.state = 0
            elif self.z_pos == 0:
                self.state = 0
            elif self.z_pos < self.z_pos_old:
                print("Lautstärke RUNTER!")
                write_soundchange('-')
            elif self.z_pos >= (self.pointZero + (self.tolerance / 2)):
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

    def handleDataStraight(self):
        if self.state == 0:
            if self.receiveActivity():
                self.state = 1
                self.start_time = time.clock()
                self.z_pos_old = self.receiveZpos()
        elif self.state == 1:
            if self.receiveActivity():
                dt = time.clock() - self.start_time
                if dt > 0.01:
                    self.state = 2
                    # print("success")
            else:
                self.state = 0
        elif self.state == 2:  # Einstellmodus, unterscheidet zwischen leichten Bewegungen und schnellen
            if self.receiveActivity():
                # print(str(self.z_pos) + "   o: " + str(self.z_old))
                if self.z_pos > self.z_pos_old + self.t2 + self.t3:
                    self.state = 3
                    print("fast up")
                elif self.z_pos < self.z_pos_old - self.t2 - self.t3:
                    self.state = 4
                    print("fast down")
                elif self.z_pos > self.z_pos_old + self.t2:
                    write_soundchange('+')
                    print("up")
                    # print(self.z_pos)
                elif self.z_pos < self.z_pos_old - self.t2:
                    print("down")
                    # print(self.z_pos)
                    write_soundchange('-')
                else:
                    pass
        elif self.state == 3:  # schnelle Hochbewegung, endet mit kleiner Bewegung nach unten
            # print(str(self.activity) + "   " + str(self.z_pos))
            if self.receiveActivity():
                if self.z_pos < self.z_pos_old - self.t2:
                    self.state = 2
                    print("back to normal")
            else:
                self.state = 0
        elif self.state == 4:  # schnelle Runterbewegung, endet mit kleiner Bewegung nach oben
            if self.receiveActivity():
                if self.z_pos > self.z_pos_old + self.t2:
                    self.state = 2
                    print("back to normal")
            else:
                self.state = 0
        else:
            self.state = 0
