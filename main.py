import time
from tkinter import ttk

from classes.bus import Bus
from classes.cpu import Cpu
from threading import Lock, Thread

from tkinter import *

from classes.interfaceData import InterfaceData

mutex = Lock()
bus = Bus()
interfaceData = InterfaceData()
procesor0 = Cpu(0, bus, mutex, interfaceData)
procesor1 = Cpu(1, bus, mutex, interfaceData)
procesor2 = Cpu(2, bus, mutex, interfaceData)
procesor3 = Cpu(3, bus, mutex, interfaceData)
processorlist = [procesor0, procesor1, procesor2, procesor3]
bus.conections.append(procesor0)
bus.conections.append(procesor1)
bus.conections.append(procesor2)
bus.conections.append(procesor3)


def createProcessorsAux(processor):
    processor.getInstruction()


def createProcessorsThreads():
    Thread(target=createProcessorsAux, args=(procesor0,), daemon=True).start()
    Thread(target=createProcessorsAux, args=(procesor1,), daemon=True).start()
    Thread(target=createProcessorsAux, args=(procesor2,), daemon=True).start()
    Thread(target=createProcessorsAux, args=(procesor3,), daemon=True).start()


if __name__ == '__main__':
    createProcessorsThreads()


def updatedata():
    while 1:
        labelp0.config(
            text="Procesador 0:\nultima instrucción ejecutada: " + procesor0.lastInstruction+ "\nultima instrucción genereda: "+procesor0.currentInstruction + "\n" + procesor0.controller.l1cache.getstring())
        labelp1.config(
            text="Procesador 1:\nultima instrucción ejecutada: " + procesor0.lastInstruction+ "\nultima instrucción genereda: "+procesor1.currentInstruction + "\n" + procesor1.controller.l1cache.getstring())
        labelp2.config(
            text="Procesador 2:\nultima instrucción ejecutada: " + procesor0.lastInstruction+ "\nultima instrucción genereda: "+procesor2.currentInstruction + "\n" + procesor2.controller.l1cache.getstring())
        labelp3.config(
            text="Procesador 3:\nultima instrucción ejecutada: " +procesor0.lastInstruction+ "\nultima instrucción genereda: "+procesor3.currentInstruction + "\n" + procesor3.controller.l1cache.getstring())
        labelmem.config(
            text="memoria:\n" + bus.memory.getstring())
        if procesor0.continueProcess:
            pausa="activo"
        else:
            pausa="pausa"
        labelinformation.config(
            text="ultima instruccion: " + interfaceData.lastInstruction +
                 "\n" + "tiempo por ciclo: " + str(interfaceData.period) + " segundos\n" +
                 "modo: " + interfaceData.mode + "\n"+"estado: "+pausa)
        time.sleep(1)

    # creating the tkinter window


Main_window = Tk()
Main_window.geometry("1100x400")
Main_window.resizable(False, False)
# create a Label widget
labelp0 = Label(Main_window,
                text="")
labelp1 = Label(Main_window,
                text="")
labelp2 = Label(Main_window,
                text="")
labelp3 = Label(Main_window,
                text="")
labelmem = Label(Main_window,
                 text="")
labelinformation = Label(Main_window,
                         text="")


def setManualMode():
    interfaceData.mode = "manual"


butttonmanualmode = Button(Main_window,
                           text="modo manual",
                           command=setManualMode)


def setTimeMode():
    interfaceData.mode = "time"


buttontimemode = Button(Main_window,
                        text="modo continuo",
                        command=setTimeMode)

combooperation = ttk.Combobox(Main_window,
                              values=[
                                  "calc",
                                  "write",
                                  "read"], state="readonly")
combomemory = ttk.Combobox(Main_window,
                           values=[
                               "000", "001", "010",
                               "011", "100", "101",
                               "110", "111"], state="readonly")
comboprocessor = ttk.Combobox(Main_window,
                              values=[
                                  "p0",
                                  "p1",
                                  "p2", "p3"], state="readonly")
comboprocessor.current(0)
combooperation.current(0)
combomemory.current(0)

textdata = Entry(Main_window)


def setInstruction():
    if interfaceData.mode=="manual" or not procesor0.continueProcess:
        data = textdata.get()
        processor = int(comboprocessor.get()[1])
        memoryaddress = combomemory.get()
        operation = combooperation.get()
        if operation == "write" and isHex(data) and len(data) == 4:
            processorlist[processor].manualInstruction = [operation, memoryaddress, data]
        elif operation == "read":
            processorlist[processor].manualInstruction = [operation, memoryaddress]
        elif operation == "calc":
            processorlist[processor].manualInstruction = [operation]


def isHex(string):
    for letter in string:
        if (letter < '0' or letter > '9') and (letter < 'a' or letter > 'f'):
            return False
    return True


buttoninstruction = Button(Main_window,
                           text="ingresar instrucción",
                           command=setInstruction)

timetext = Entry(Main_window)


def setTime():
    if timetext.get().isnumeric():
        interfaceData.period = int(timetext.get())


buttonperiod = Button(Main_window,
                      text="cambiar tiempo por ciclo",
                      command=setTime)


def nextCycle():
    for p in processorlist:
        p.nextCycle = True


buttonNext = Button(Main_window,
                    text="siguiente ciclo",
                    command=nextCycle)


def pausarReanudar():
    for p in processorlist:
        p.continueProcess = not p.continueProcess


buttonPause = Button(Main_window,
                     text="Pausar/Reaundar",
                     command=pausarReanudar)


Label(Main_window, text="Elegir un nuevo tiempo por ciclo:").grid(row=4, column=0)
labelp0.grid(row=0, column=0)
labelp1.grid(row=0, column=2)
labelp2.grid(row=1, column=0)
labelp3.grid(row=1, column=2)
labelmem.grid(row=0, column=4)
labelinformation.grid(row=1, column=4)
butttonmanualmode.grid(row=3, column=0)
buttontimemode.grid(row=3, column=1)
buttonNext.grid(row=3, column=2)
buttonPause.grid(row=3, column=3)
timetext.grid(row=4, column=1)
buttonperiod.grid(row=4, column=2)
Label(Main_window, text="Introducir nueva instrucción:").grid(row=5, column=0)
comboprocessor.grid(row=6, column=0)
combooperation.grid(row=6, column=1)
combomemory.grid(row=6, column=2)
textdata.grid(row=6, column=3)
buttoninstruction.grid(row=6, column=4)

Thread(target=updatedata, daemon=True).start()

Main_window.mainloop()

