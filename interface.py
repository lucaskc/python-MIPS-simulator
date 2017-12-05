from tkinter import *
import PipelineSimulator
import Instruction
import os
import sys
from sys import argv

root = Tk()

height = 46
width = 5

entry_Str = [[]]
clockNumber = 0

#Create a 5x5 excel-like table
for i in range(0,height): #Rows
    listVar = []

    for j in range(1, width + 1): #Columns
        var = StringVar()
        listVar.append(var)
        
        if(i > 31):
            Entry(root, textvariable=var).grid(row=(i-32), column=(j+7))
        else:
            Entry(root, textvariable=var).grid(row=i, column=j)

    entry_Str.append(listVar)

#Defining my methods before the elements need them
def forwardResults():
    for i in range(1, (height+1)):
        for j in range(width-1, 0, -1):
            entry_Str[i][j].set(entry_Str[i][j - 1].get())

def nextClock():
    forwardResults()

    entry_Str[1][0].set("r1") #[column starting in 1][row starting in 0]
    entry_Str[2][0].set("r10")
    entry_Str[3][0].set("r11")
    entry_Str[4][0].set("r12")
    entry_Str[5][0].set("r13")
    entry_Str[6][0].set("r14")
    entry_Str[7][0].set("r15")
    entry_Str[8][0].set("r16")
    entry_Str[9][0].set("r17")
    entry_Str[10][0].set("r18")
    entry_Str[11][0].set("r19")
    entry_Str[12][0].set("r2")
    entry_Str[13][0].set("r20")
    entry_Str[14][0].set("r21")
    entry_Str[15][0].set("r22")
    entry_Str[16][0].set("r23")
    entry_Str[17][0].set("r24")
    entry_Str[18][0].set("r25")
    entry_Str[19][0].set("r26")
    entry_Str[20][0].set("r27")
    entry_Str[21][0].set("r28")
    entry_Str[22][0].set("r29")
    entry_Str[23][0].set("r3")
    entry_Str[24][0].set("r30")
    entry_Str[25][0].set("r31")
    entry_Str[26][0].set("r4")
    entry_Str[27][0].set("r5")
    entry_Str[28][0].set("r6")
    entry_Str[29][0].set("r7")
    entry_Str[30][0].set("r8")
    entry_Str[31][0].set("r9")
    entry_Str[32][0].set("r9")
    entry_Str[33][0].set("r9")
    entry_Str[34][0].set("r9")
    entry_Str[35][0].set("r9")
    entry_Str[36][0].set("r9")
    entry_Str[37][0].set("r9")
    entry_Str[38][0].set("r9")
    entry_Str[39][0].set("r8")
    entry_Str[40][0].set("r9")
    entry_Str[41][0].set("r9")
    entry_Str[42][0].set("r9")
    entry_Str[43][0].set("r9")
    entry_Str[44][0].set("r9")
    entry_Str[45][0].set("r9")
    entry_Str[46][0].set("r9")

#------------------------------------ colocar os registradores ai nesses sets cada vez que apertar.

#Adding button
button = Button(root, text="Clock it!", command=nextClock)
button.grid(row=14, column=7)

#Naming the labels -> I know it's an ugly code, but wich one has a different name!
lbl = Label(root, text="$r0: ")
lbl.grid(row=0, column=0)

lbl = Label(root, text="$r1: ")
lbl.grid(row=1, column=0)

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

lbl = Label(root, text="$r2: ")
lbl.grid(row=12, column=0)

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

lbl = Label(root, text="$r3: ")
lbl.grid(row=23, column=0)

lbl = Label(root, text="$r30: ")
lbl.grid(row=24, column=0)

lbl = Label(root, text="$r31: ")
lbl.grid(row=25, column=0)

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

lbl = Label(root, text="IF/ID[1]: ")
lbl.grid(row=0, column=7)

lbl = Label(root, text="IF/ID[2]: ")
lbl.grid(row=1, column=7)

lbl = Label(root, text="ID/EX[1]: ")
lbl.grid(row=2, column=7)

lbl = Label(root, text="ID/EX[2]: ")
lbl.grid(row=3, column=7)

lbl = Label(root, text="ID/EX[3]: ")
lbl.grid(row=4, column=7)

lbl = Label(root, text="ID/EX[4]: ")
lbl.grid(row=5, column=7)

lbl = Label(root, text="ID/EX[5]: ")
lbl.grid(row=6, column=7)

lbl = Label(root, text="EX/MEM[1]: ")
lbl.grid(row=7, column=7)

lbl = Label(root, text="EX/MEM[2]: ")
lbl.grid(row=8, column=7)

lbl = Label(root, text="EX/MEM[3]: ")
lbl.grid(row=9, column=7)

lbl = Label(root, text="EX/MEM[4]: ")
lbl.grid(row=10, column=7)

lbl = Label(root, text="MEM/WB[1]: ")
lbl.grid(row=11, column=7)

lbl = Label(root, text="MEM/WB[2]: ")
lbl.grid(row=12, column=7)

lbl = Label(root, text="MEM/WB[3]: ")
lbl.grid(row=13, column=7)

mainloop()