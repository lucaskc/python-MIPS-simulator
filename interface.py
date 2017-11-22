from tkinter import *

root = Tk()

height = 5
width = 5


#Defining my methods before the elements need them
def nextClock():
    print("Here will be the code changing the registers")

#Create a 5x5 excel-like table
for i in range(height): #Rows
    lbl = Label(root, text="OLÁ MUNDO")
    lbl.grid(row=i, column=0)

    for j in range(1, width + 1): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

button = Button(root, text="É isso?", command=nextClock)
button.grid(row=4, column=4)

mainloop()