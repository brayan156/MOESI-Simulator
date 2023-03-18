from methods.converter import *


class MemoryBlock:
    def __init__(self, number, data):
        self.number = number
        self.data = data

    def getNumber(self):
        return int(str(self.number),2)

    def setNumber(self, number):
        self.number = decimalToBinary(number, 3)

    def getData(self):
        return int(str(self.data),16)

    def setData(self, data):
        self.data = decimalToHexadecimal(data,16)

    def getstring(self):
        return "bloque: "+str(decimalToBinary(self.number, 3))+", dato: "+str(self.data)