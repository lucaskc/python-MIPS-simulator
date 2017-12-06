from tkinter import *
import PipelineSimulator
import Instruction
import os
import sys

root = Tk()

height = 46
width = 5

entry_Str = [[]]
clockNumber = 0

iparser = Instruction.InstructionParser()
pipelinesim = PipelineSimulator.PipelineSimulator(iparser.parseFile(sys.argv[1]))
    
filename = sys.argv[2] if len(sys.argv) > 2 else "debug.txt"
f = open(filename, 'w')
sys.stdout = f
simulationInfo = pipelinesim.run()

mainRegs = [None] * 32

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

def setValues():
    global clockNumber

    if clockNumber >= len(simulationInfo):
        return

    for index in range(0, 32):
        mainRegs[index] = simulationInfo[clockNumber].mainRegs["$r" + str(index)]

def nextClock():
    forwardResults()
    setValues()

    global clockNumber, mainRegs

    for i in range(1, 33):
        entry_Str[i][0].set(mainRegs[i - 1])
    
    #entry_Str[1][8].set("Test")

    clockNumber += 1

#------------------------------------ colocar os registradores ai nesses sets cada vez que apertar.

#Adding button
button = Button(root, text="Clock it!", command=nextClock)
button.grid(row=14, column=7)

#Naming the labels -> I know it's an ugly code, but wich one has a different name!
lbl = Label(root, text="$r0: ")
lbl.grid(row=0, column=0)

lbl = Label(root, text="$r1: ")
lbl.grid(row=1, column=0)

lbl = Label(root, text="$r2: ")
lbl.grid(row=2, column=0)

lbl = Label(root, text="$r3: ")
lbl.grid(row=3, column=0)

lbl = Label(root, text="$r4: ")
lbl.grid(row=4, column=0)

lbl = Label(root, text="$r5: ")
lbl.grid(row=5, column=0)

lbl = Label(root, text="$r6: ")
lbl.grid(row=6, column=0)

lbl = Label(root, text="$r7: ")
lbl.grid(row=7, column=0)

lbl = Label(root, text="$r8: ")
lbl.grid(row=8, column=0)

lbl = Label(root, text="$r9: ")
lbl.grid(row=9, column=0)

lbl = Label(root, text="$r10: ")
lbl.grid(row=10, column=0)

lbl = Label(root, text="$r11: ")
lbl.grid(row=11, column=0)

lbl = Label(root, text="$r12: ")
lbl.grid(row=12, column=0)

lbl = Label(root, text="$r13: ")
lbl.grid(row=13, column=0)

lbl = Label(root, text="$r14: ")
lbl.grid(row=14, column=0)

lbl = Label(root, text="$r15: ")
lbl.grid(row=15, column=0)

lbl = Label(root, text="$r16: ")
lbl.grid(row=16, column=0)

lbl = Label(root, text="$r17: ")
lbl.grid(row=17, column=0)

lbl = Label(root, text="$r18: ")
lbl.grid(row=18, column=0)

lbl = Label(root, text="$r19: ")
lbl.grid(row=19, column=0)

lbl = Label(root, text="$r20: ")
lbl.grid(row=20, column=0)

lbl = Label(root, text="$r21: ")
lbl.grid(row=21, column=0)

lbl = Label(root, text="$r22: ")
lbl.grid(row=22, column=0)

lbl = Label(root, text="$r23: ")
lbl.grid(row=23, column=0)

lbl = Label(root, text="$r24: ")
lbl.grid(row=24, column=0)

lbl = Label(root, text="$r25: ")
lbl.grid(row=25, column=0)

lbl = Label(root, text="$r26: ")
lbl.grid(row=26, column=0)

lbl = Label(root, text="$r27: ")
lbl.grid(row=27, column=0)

lbl = Label(root, text="$r28: ")
lbl.grid(row=28, column=0)

lbl = Label(root, text="$r29: ")
lbl.grid(row=29, column=0)

lbl = Label(root, text="$r30: ")
lbl.grid(row=30, column=0)

lbl = Label(root, text="$r31: ")
lbl.grid(row=31, column=0)

lbl = Label(root, text="IF/ID.IR: ")
lbl.grid(row=0, column=7)

lbl = Label(root, text="IF/ID.PC: ")
lbl.grid(row=1, column=7)

lbl = Label(root, text="ID/EX.IR: ")
lbl.grid(row=2, column=7)

lbl = Label(root, text="ID/EX.PC: ")
lbl.grid(row=3, column=7)

lbl = Label(root, text="ID/EX.A: ")
lbl.grid(row=4, column=7)

lbl = Label(root, text="ID/EX.B: ")
lbl.grid(row=5, column=7)

lbl = Label(root, text="ID/EX.IMM: ")
lbl.grid(row=6, column=7)

lbl = Label(root, text="EX/MEM.IR: ")
lbl.grid(row=7, column=7)

lbl = Label(root, text="EX/MEM.B: ")
lbl.grid(row=8, column=7)

lbl = Label(root, text="EX/MEM.COND: ")
lbl.grid(row=9, column=7)

lbl = Label(root, text="EX/MEM.ALUOUT: ")
lbl.grid(row=10, column=7)

lbl = Label(root, text="MEM/WB.IR: ")
lbl.grid(row=11, column=7)

lbl = Label(root, text="MEM/WB.ALOUT: ")
lbl.grid(row=12, column=7)

lbl = Label(root, text="MEM/WB.LMD: ")
lbl.grid(row=13, column=7)

mainloop()