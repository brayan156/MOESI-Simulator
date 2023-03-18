from classes.memory import Memory


class Bus:
    def __init__(self):
        self.conections = []
        self.memory = Memory()

    def writeToMemory(self, address, data):
        block = self.memory.getBlockByNumber(address)
        block.setData(data)

    def readFromMemory(self, address):
        return self.memory.getBlockByNumber(address).getData()
