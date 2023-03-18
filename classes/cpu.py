import time

from classes.controller import Controller
from methods.instructionGenerator import generateInstruction


class Cpu:
    def __init__(self, number, bus, mutex, interfaceData):
        self.number = number
        self.controller = Controller()
        self.bus = bus
        self.currentInstruction = ""
        self.mutex = mutex
        self.interfaceData = interfaceData
        self.manualInstruction = []
        self.nextCycle = False
        self.lastInstruction = ""
        self.continueProcess = True

    def setmanualInstruction(self, instruction):
        self.manualInstruction = instruction

    def getInstruction(self):
        name = "file" + str(self.number) + ".txt"
        file1 = open(name, "w")
        file1.close()

        while 1:
            print(self.manualInstruction)
            if not self.manualInstruction:
                instruction = generateInstruction()
            else:
                instruction = self.manualInstruction
                self.manualInstruction = []
            print(self.number, instruction)

            actions = []
            if instruction[0] == "calc":
                self.currentInstruction = "P" + str(self.number) + ": CALC"
                actions = [["noAction"]]
            elif instruction[0] == "write":
                self.currentInstruction = "P" + str(self.number) + ": WRITE " + instruction[1] + ";" + instruction[2]
                actions = self.controller.write(int(instruction[1], 2), int(instruction[2], 16))
            elif instruction[0] == "read":
                self.currentInstruction = "P" + str(self.number) + ": READ " + instruction[1]
                actions = self.controller.readPetition(int(instruction[1], 2))
            self.log(self.currentInstruction + " cache: |" + self.controller.l1cache.getstring())
            self.interfaceData.lastInstruction = self.currentInstruction
            self.manageBus(actions)
            self.lastInstruction = self.currentInstruction
            self.applyMode()

    def manageBus(self, actions):
        action = actions[0]
        if action[0] != "noAction" and action[0] != "hit":
            self.mutex.acquire()
            if len(actions) == 2:
                self.bus.writeToMemory(action[1], action[2])
                self.applyMode()
                action = actions[1]
            if action[0] == "readMiss":
                print(self.number, "readmiss")
                self.waitResponse(action[1])
            elif action[0] == "writeMiss":
                print(self.number, "writemiss")
                self.Invalidate(action[1])
            self.mutex.release()

    def waitResponse(self, address):
        data = None
        for i in range(4):
            if i != self.number:
                readed = self.bus.conections[i].controller.readMiss(address)
                if readed is not None:
                    data = readed
        if data is None:
            data = self.bus.readFromMemory(address)
            self.applyMode()
            action = self.controller.read(address, data, "memory")
        else:
            action = self.controller.read(address, data, "cache")
        if action[0] == "WB":
            self.bus.writeToMemory(action[1], action[2])
            self.applyMode()

    def Invalidate(self, address):
        for i in range(4):
            if i != self.number:
                self.bus.conections[i].controller.writeMiss(address)

    def applyMode(self):
        if self.interfaceData.mode == "manual":
            while 1:
                if self.nextCycle:
                    self.nextCycle = False
                    break
        else:
            while 1:
                if self.continueProcess:
                    break
            time.sleep(self.interfaceData.period)

    def log(self, string):
        name = "file" + str(self.number) + ".txt"
        file1 = open(name, "a")
        file1.write("\n")
        file1.write(string)
        file1.close()
