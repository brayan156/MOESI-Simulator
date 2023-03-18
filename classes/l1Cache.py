from classes.l1CacheBlock import L1CacheBlock
import numpy as np


class L1Cache:
    def __init__(self):
        self.sets = [
            [L1CacheBlock(0, "I", 0, 0), L1CacheBlock(1, "I", 0, 0)],
            [L1CacheBlock(2, "I", 0, 0), L1CacheBlock(3, "I", 0, 0)]
        ]

    def getSets(self):
        return self.sets

    def getBlock(self, number):
        return self.sets[number // 2][number % 2]

    def getSet(self, setNumber):
        return self.sets[setNumber]

    def getAllBlocks(self):
        return self.sets[0] + self.sets[1]

    def searchData(self, address):
        set = self.getSet(address % 2)
        for block in set:
            if block.getAddress() == address:
                if block.getAddress() == 0 and block.getData() == 0 and block.getCoherence() == "I":
                    return None
                else:
                    return block
        return None

    def getBlockByReplacePolicy(self, address):
        selector = round(np.random.uniform(0, 199)) // 100
        set = self.getSet(address % 2)
        block = set[selector]
        return block

    def getFreeBlock(self, address):
        set = self.getSet(address % 2)
        for block in set:
            if block.getCoherence() == "I":
                return block
        return None

    def getBlocktoWrite(self, address):
        block = self.searchData(address)
        if block is None:
            block = self.getFreeBlock(address)
            if block is None:
                block = self.getBlockByReplacePolicy(address)
            return block
        else:
            return block

    def getstring(self):
        data=""
        for block in self.getAllBlocks():
            data+=block.getstring()
            data+="\n"
        return data
