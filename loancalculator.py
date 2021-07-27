from tkinter import *

class loancalculator:
    def __init__(self):
        window=Tk()
        window.title("Loan Calculator")
        window.configure(background="black")
        Label(window,font="Helvetica 12 bold",background="black",fg="white",text="Annual Interest Rate").grid(row=1,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",background="black",fg="white",text="Number of Years").grid(row=2,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",background="black",fg="white",text="Loan Amount ").grid(row=3,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",background="black",fg="white",text="Monthly Payment").grid(row=4,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",background="black",fg="white",text="Total Payment").grid(row=5,column=1,sticky=W)
        
        self.annualinterestrateVar=StringVar()
        Entry(window,textvariable=self.annualinterestrateVar,justify=RIGHT).grid(row=1,column=2)
        self.numberofyearsVar=StringVar()
        Entry(window,textvariable=self.numberofyearsVar,justify=RIGHT).grid(row=2,column=2)
        self.loanamountVar=StringVar()
        Entry(window,textvariable=self.loanamountVar,justify=RIGHT).grid(row=3,column=2)
        self.monthlypaymentVar=StringVar()
        lblmonthlypayment=Label(window,font="Helvetica 12 bold",background="black",textvariable=self.monthlypaymentVar).grid(row=4,column=2,sticky=E)
        self.totalpaymentVar=StringVar()
        lblmonthlypayment=Label(window,font="Helvetica 12 bold",background="black",textvariable=self.totalpaymentVar).grid(row=5,column=2,sticky=E)

        btComputePayment=Button(window,text="Compute Payment",background="blue",fg="white",font="Helvetica 12 bold",command=self.computepayment).grid(row=6,column=2,sticky=E)
        btClear=Button(window,text="Clear",background="red",fg="white",font="Helvetica 12 bold",command=self.delete_all).grid(row=6,column=5,padx=20,pady=20,sticky=E)

        window.mainloop()

    def computepayment(self):
        monthlypayment=self.getmonthlypaymentVar(
            float(self.loanamountVar.get()) ,
            float(self.annualinterestrateVar.get()) /1200,
            int(self.numberofyearsVar.get())
        )

        self.monthlypaymentVar.set(format(monthlypayment,"10.2f"))

        totalpayment=float(self.monthlypaymentVar.get()) * 12 \
        * int(self.numberofyearsVar.get())

        self.totalpaymentVar.set(format(totalpayment,"10.2f"))

    def getmonthlypaymentVar(self,loanamount,monthlyinterestrate,numberofyears):
        monthlypayment=loanamount*monthlyinterestrate/(1-1/(1+monthlyinterestrate)**(numberofyears*12))
        return monthlypayment

    def delete_all(self):
        self.monthlypaymentVar.set("")
        self.loanamountVar.set("")
        self.annualinterestrateVar.set("")
        self.numberofyearsVar.set("")
        self.totalpaymentVar.set("")
loancalculator()   
