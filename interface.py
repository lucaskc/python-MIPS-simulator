from tkinter import *

root = Tk()

height = 5
width = 5

#Create a 5x5 excel-like table

for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

nextClockBtn = Button(root, fg="red", text="Next Clock", command="nextClock")
nextClockBtn.pack()

#class Application(Frame):
#    def __init__(self, master=None):
#        super().__init__(master)
#        self.pack()
#        self.create_widgets()

#    def create_widgets(self):
#        self.nextClockBtn = tk.Button(self)
#        self.nextClockBtn["text"] = "Next Clock"
#        self.nextClockBtn["command"] = self.nextClock
#        self.nextClockBtn.pack(side="top")

#        self.quit = tk.Button(self, text="QUIT", fg="red",
#                              command=root.destroy)
#        self.quit.pack(side="bottom")

def nextClock():
    print("Here will be the code changing the registers")

mainloop()