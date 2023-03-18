from classes.l1Cache import L1Cache


class Controller:
    def __init__(self):
        self.l1cache = L1Cache()

    def readMiss(self, address):
        block = self.l1cache.searchData(address)
        if block is None:
            return None
        if block.getCoherence() == "M":
            block.setCoherence("O")
            return block.getData()
        elif block.getCoherence() == "O":
            return block.getData()
        elif block.getCoherence() == "E":
            block.setCoherence("S")
            return block.getData()
        elif block.getCoherence() == "S":
            return block.getData()
        elif block.getCoherence() == "I":
            return None

    def write(self,address,data):
        block = self.l1cache.getBlocktoWrite(address)
        if block.getCoherence() == "M":
            if block.getAddress()==address:
                block.setData(data)
                return [["noAction"]]
            else:
                action=[["WB",block.getAddress(),block.getData()],["writeMiss",address]]
                block.setAddress(address)
                block.setData(data)
                return action
        elif block.getCoherence() == "O":
            if block.getAddress()==address:
                block.setData(data)
                return [["writeMiss",address]]
            else:
                action=[["WB",block.getAddress(),block.getData()],["writeMiss",address]]
                block.setAddress(address)
                block.setData(data)
                block.setCoherence("M")
                return action
        elif block.getCoherence() == "E":
            block.setAddress(address)
            block.setData(data)
            block.setCoherence("M")
            return [["noAction"]]
        elif block.getCoherence() == "S":
            block.setAddress(address)
            block.setData(data)
            block.setCoherence("M")
            return [["writeMiss",address]]
        elif block.getCoherence() == "I":
            block.setAddress(address)
            block.setData(data)
            block.setCoherence("M")
            return [["writeMiss", address]]

    def writeMiss(self,address):
        block = self.l1cache.searchData(address)
        if block is None:
            return
        elif block.getCoherence() == "M":
            block.setCoherence("I")
        elif block.getCoherence() == "O":
            block.setCoherence("I")
        elif block.getCoherence() == "E":
            block.setCoherence("I")
        elif block.getCoherence() == "S":
            block.setCoherence("I")

    def readPetition(self,address):
        block = self.l1cache.searchData(address)
        if block is None:
            return [["readMiss",address]]
        elif block.getCoherence() == "I":
            return [["readMiss",address]]
        return [["hit",block.getAddress(),block.getData()]]

    def read(self,address,data,dataFrom):
        block = self.l1cache.getBlocktoWrite(address)
        action = ["noAction"]
        if block.getAddress() != address:
            if block.getCoherence() == "O" or block.getCoherence() == "M":
                action = ["WB", block.getAddress(), block.getData()]
        block.setAddress(address)
        block.setData(data)
        if dataFrom == "memory":
            block.setCoherence("E")
        else:
            block.setCoherence("S")
        return action




