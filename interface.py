from tkinter import *

root = Tk()

height = 32
width = 5

entry_Str = [[]]

#Defining my methods before the elements need them
def nextClock():
    entry_Str[2][0].set("OLA MUNDO") #[row starting in 1][column starting in 0]
    #IMPLEMENTAR AQUI O CÓDIGO PARA SAIR O FINAL

#Create a 5x5 excel-like table
for i in range(height): #Rows
    listVar = []
    
    for j in range(1, width + 1): #Columns
        var = StringVar()
        listVar.append(var);
        Entry(root, textvariable=var).grid(row=i, column=j)

    entry_Str.append(listVar)


#Adding button
button = Button(root, text="Clock it!", command=nextClock)
button.grid(row=33, column=5)

#Naming the labels -> I know it's an ugly code, but wich one has a different name!
lbl = Label(root, text="$r0: ")
lbl.grid(row=0, column=0)

lbl = Label(root, text="$r1: ")
lbl.grid(row=1, column=0)

lbl = Label(root, text="$r2: ")
lbl.grid(row=12, column=0)

lbl = Label(root, text="$r3: ")
lbl.grid(row=23, column=0)

lbl = Label(root, text="$r4: ")
lbl.grid(row=26, column=0)

lbl = Label(root, text="$r5: ")
lbl.grid(row=27, column=0)

lbl = Label(root, text="$r6: ")
lbl.grid(row=28, column=0)

lbl = Label(root, text="$r7: ")
lbl.grid(row=29, column=0)

lbl = Label(root, text="$r8: ")
lbl.grid(row=30, column=0)

lbl = Label(root, text="$r9: ")
lbl.grid(row=31, column=0)

lbl = Label(root, text="$r10: ")
lbl.grid(row=2, column=0)

lbl = Label(root, text="$r11: ")
lbl.grid(row=3, column=0)

lbl = Label(root, text="$r12: ")
lbl.grid(row=4, column=0)

lbl = Label(root, text="$r13: ")
lbl.grid(row=5, column=0)

lbl = Label(root, text="$r14: ")
lbl.grid(row=6, column=0)

lbl = Label(root, text="$r15: ")
lbl.grid(row=7, column=0)

lbl = Label(root, text="$r16: ")
lbl.grid(row=8, column=0)

lbl = Label(root, text="$r17: ")
lbl.grid(row=9, column=0)

lbl = Label(root, text="$r18: ")
lbl.grid(row=10, column=0)

lbl = Label(root, text="$r19: ")
lbl.grid(row=11, column=0)

lbl = Label(root, text="$r20: ")
lbl.grid(row=13, column=0)

lbl = Label(root, text="$r21: ")
lbl.grid(row=14, column=0)

lbl = Label(root, text="$r22: ")
lbl.grid(row=15, column=0)

lbl = Label(root, text="$r23: ")
lbl.grid(row=16, column=0)

lbl = Label(root, text="$r24: ")
lbl.grid(row=17, column=0)

lbl = Label(root, text="$r25: ")
lbl.grid(row=18, column=0)

lbl = Label(root, text="$r26: ")
lbl.grid(row=19, column=0)

lbl = Label(root, text="$r27: ")
lbl.grid(row=20, column=0)

lbl = Label(root, text="$r28: ")
lbl.grid(row=21, column=0)

lbl = Label(root, text="$r29: ")
lbl.grid(row=22, column=0)

lbl = Label(root, text="$r30: ")
lbl.grid(row=24, column=0)

lbl = Label(root, text="$r31: ")
lbl.grid(row=25, column=0)

mainloop()