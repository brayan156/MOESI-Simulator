from classes.memoryBlock import MemoryBlock


class Memory:
    def __init__(self):
        self.blocks = [
            MemoryBlock(0, 0),
            MemoryBlock(1, 0),
            MemoryBlock(2, 0),
            MemoryBlock(3, 0),
            MemoryBlock(4, 0),
            MemoryBlock(5, 0),
            MemoryBlock(6, 0),
            MemoryBlock(7, 0)
        ]

    def getBlockByNumber(self, number):
        return self.blocks[number]

    def getstring(self):
        data=""
        for block in self.blocks:
            data+=block.getstring()
            data+="|"
            if block.number%2==1:
                data+="\n"
        return data