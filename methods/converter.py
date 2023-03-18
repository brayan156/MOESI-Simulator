import math


def decimalToBinary(decimal, nbits):
    binary = bin(decimal).replace("0b", "")
    finalBinary = "0" * (nbits - len(binary)) + binary
    return finalBinary


def decimalToHexadecimal(decimal, nbits):
    hexadecimal = hex(decimal).replace("0x", "")
    finalhexadecimal = "0" * (math.ceil(nbits / 4) - len(hexadecimal)) + hexadecimal
    return finalhexadecimal
