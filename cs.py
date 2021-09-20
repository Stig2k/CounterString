from tkinter import *
import pyperclip as pc


mywindow = Tk()
mywindow.wm_attributes("-topmost", 1)
# mywindow.geometry("180x50")
mywindow.title("CounterString Generator")

def createCounterString():

    inputInt=int(e.get())
    firstString = "x" + str(inputInt)[::-1]
    newInt = inputInt - len(firstString)
    while newInt > 1:
        nextString = "x" + str(newInt)[::-1]
        firstString = firstString + nextString
        newInt = inputInt - len(firstString)
    if len(firstString) < inputInt:
        pc.copy("x" + firstString[::-1])
    else:
        pc.copy(firstString[::-1])
    e.delete(0, END)


def button_click(digit):
    current = str(e.get())
    e.delete(0, END)
    e.insert(0, current + digit)

e = Entry(mywindow, width="15", borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_0 = Button(mywindow, text="0", padx=10, pady=2, command=lambda: button_click("0"))
button_1 = Button(mywindow, text="1", padx=10, pady=2, command=lambda: button_click("1"))
button_2 = Button(mywindow, text="2", padx=10, pady=2, command=lambda: button_click("2"))
button_3 = Button(mywindow, text="3", padx=10, pady=2, command=lambda: button_click("3"))
button_4 = Button(mywindow, text="4", padx=10, pady=2, command=lambda: button_click("4"))
button_5 = Button(mywindow, text="5", padx=10, pady=2, command=lambda: button_click("5"))
button_6 = Button(mywindow, text="6", padx=10, pady=2, command=lambda: button_click("6"))
button_7 = Button(mywindow, text="7", padx=10, pady=2, command=lambda: button_click("7"))
button_8 = Button(mywindow, text="8", padx=10, pady=2, command=lambda: button_click("8"))
button_9 = Button(mywindow, text="9", padx=10, pady=2, command=lambda: button_click("9"))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

myButton = Button(mywindow, padx=6, pady=2, text=" Generate ", command=createCounterString)
myButton.grid(row=4, column=1, columnspan=2)

mywindow.mainloop()
