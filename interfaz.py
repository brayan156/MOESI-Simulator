
    # creating the tkinter window
Main_window = Tk()

# variable

# function define for
# updating the my_label
# widget content

# create a button widget and attached
# with counter function
my_button = Button(Main_window,
                   text="Please update")

# create a Label widget
labelp0 = Label(Main_window,
                 text="")
labelp1 = Label(Main_window,
                 text="")
labelp2 = Label(Main_window,
                text="")
labelp3 = Label(Main_window,
                text="")

# place the widgets
# in the gui window
labelp0.grid(row=0,column=0)
labelp1.grid(row=0, column=1)
labelp2.grid(row=1, column=0)
labelp3.grid(row=1, column=1)


Thread(target=updatedata, daemon=True).start()
# Start the GUI
Main_window.mainloop()
def updatedata():
    while 1:
        labelp0.config(text="ultima instrucción: "+procesor0.currentInstruction+"\n"+procesor0.controller.l1cache.getstring())
        labelp1.config(text="ultima instrucción: "+procesor1.currentInstruction + "\n" + procesor1.controller.l1cache.getstring())
        labelp2.config(
            text="ultima instrucción: " + procesor2.currentInstruction + "\n" + procesor2.controller.l1cache.getstring())
        labelp3.config(
            text="ultima instrucción: " + procesor3.currentInstruction + "\n" + procesor3.controller.l1cache.getstring())

        time.sleep(5)