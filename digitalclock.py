from tkinter import *
from time import strftime

root=Tk()                              #creates tkinter window
root.title("Digital Clock")            #adds title to the tkinter window

#function to display time on label
def time():
    string=strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000,time)

#styling the label wodget which displays the clock
lbl =Label(root, font=("arial",160,"bold"), bg="black",fg="white")

#pack method in tkinter packs widgets into rows and columns,positions label
lbl.pack(anchor="center" , fill="both", expand=1)

time()              #calling the time function

mainloop()          #runs the application program 