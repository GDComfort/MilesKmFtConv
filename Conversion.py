
from tkinter import *
from tkinter import ttk

root = Tk()

root.minsize(400,200)
root.title("Lab 10")

canvas = Canvas(
    root,
    height = 200,
    width = 400,
    )
canvas.pack

def km2me():
    num = int(entry.get())
    km2me = num*1000
    label3.config(text="Meters: "+str(km2me))
    
def km2mi():
    num = int(entry.get())
    km2mi = num*0.62137
    label3.config(text="Miles: "+str(km2mi))
    
def km2fe():
    num = int(entry.get())
    km2fe = num*3280.84
    label3.config(text="Feet: "+str(km2fe))

metres = Button(
    text="Metres",
    command=km2me
    )

miles = Button(
    text="Miles",
    command=km2mi
    )

feet = Button(
    text="Feet",
    command=km2fe
    )

exit = Button(
    text="Exit",
    command=exit
    )


label1 = Label(text="Enter kilometres:").place(x=25, y=25)
entry = Entry()
entry.place(x=125, y=25)


label2 = Label(text="Choose a measurement").place(x=25, y=75)
label3 = Label(text="Result:")
label3.place(x=200, y=75)



metres.place(x=25,y=100)
miles.place(x=80,y=100)
feet.place(x=125,y=100)
exit.place(x=25, y=150)


root.mainloop()