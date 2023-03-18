from methods.converter import *


class L1CacheBlock():
    def __init__(self, number, coherence, data, address):
        self.number = number
        self.coherence = coherence
        self.data = data
        self.address = address

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getCoherence(self):
        return self.coherence

    def setCoherence(self, coherence):
        self.coherence = coherence

    def getData(self):
        return int(str(self.data), 16)

    def setData(self, data):
        self.data = decimalToHexadecimal(data, 16)

    def getAddress(self):
        return int(str(self.address), 2)

    def setAddress(self, address):
        self.address = decimalToBinary(address, 3)

    def getstring(self):
        return "bloque: " + str(self.number) + ", coherencia: " + self.coherence + ", dato: " + str(
            self.data) + ", dirección: " + str(self.address)
