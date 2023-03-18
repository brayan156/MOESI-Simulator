import math

import numpy as np

from methods.converter import *


def generateInstruction():
    instructionSelector = np.random.binomial(2, 0.5)
    if instructionSelector == 0:
        return generateRead()
    elif instructionSelector == 1:
        return ["calc"]
    elif instructionSelector == 2:
        return generateWrite()


def generateWrite():
    memoryBlock = round(np.random.uniform(0, 799)) // 100
    memoryBlockBin = decimalToBinary(memoryBlock, 3)
    data = round(np.random.uniform(0, 65535))
    dataHexa = decimalToHexadecimal(data, 16)
    return ["write", memoryBlockBin, dataHexa]


def generateRead():
    memoryBlock = round(np.random.uniform(0, 799)) // 100
    memoryBlockBin = decimalToBinary(memoryBlock, 3)
    return ["read", memoryBlockBin]
