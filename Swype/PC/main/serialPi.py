import serial
import time


class Ser:
    def __init__(self):
        pass

    def start(self, com):  # returns "Error" if the programm can't open the serial-interface
        try:
            self.Pi_Serial = serial.Serial(com, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
            # setup for serial-interface
            time.sleep(1)

            if self.Pi_Serial.isOpen():  # opens it again, if its open already (to minimize error rate)
                self.Pi_Serial.close()
                self.Pi_Serial.open()
            return None
        except:
            print('[Error]: Not able to start Serial-port')
            return "[Error]: Not able to start Serial-port"

    def getIncomingData(self):
        try:
            return str(self.Pi_Serial.readline())
        except:
            return '-'

    def write(self, data):
        self.Pi_Serial.write(data)
