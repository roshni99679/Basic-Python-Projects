from tkinter import *          #import whole module

class CurrencyConverter:       #create class
    def __init__(self):        #special method in python class 
        window = Tk()          #create application window
        window.title("CurrencyConverter")      #add title to application window
        window.configure(bg="yellow")          #add background color to application window 


        #adding label widgets to application window 
        Label(window,font="Helvetica 12 bold",bg="yellow",text="Amount to Convert").grid(row=1,column=8,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="yellow",text="Conversion Rate").grid(row=2,column=8,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="yellow",text="Converted amount ").grid(row=3,column=8,sticky=W)


        #create objects and add entry functions
        self.amounttoconvertvar=StringVar()
        Entry(window,textvariable=self.amounttoconvertvar,justify=RIGHT).grid(row=1,column=9)
        self.conversionratevar=StringVar()
        Entry(window,textvariable=self.conversionratevar,justify=RIGHT).grid(row=2,column=9)
        self.convertedamountvar=StringVar()
        lblConvertedamount=Label(window,font ="Helvetica 12 bold",bg="yellow",textvariable=self.convertedamountvar).grid(row=3,column=9,sticky=E)


        #create convert and clear buttons 
        btConvertedamount = Button(window,text="Convert",font ="Helvetica 12 bold",bg="black",fg="white",command=self.Convertedamount).grid(row=4,column=8,sticky=E)
        btdelete_all=Button(window,text="Clear",font ="Helvetica 12 bold",bg="red",fg="white",command=self.delete_all).grid(row=4,column=13,sticky=E,padx=25,pady=25)


        window.mainloop()      #runs the application program 

    #function for conversion 
    def Convertedamount(self):
        amt= float(self.conversionratevar.get())
        convertedamountvar = float(self.amounttoconvertvar.get()) *amt
        self.convertedamountvar.set(format(convertedamountvar,"10.2f"))

    #functions to delete /clear all
    def delete_all(self):
        self.amounttoconvertvar.set("")
        self.conversionratevar.set("")
        self.convertedamountvar.set("")

CurrencyConverter()




