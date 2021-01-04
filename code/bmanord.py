from tkinter import *
from tkinter import messagebox
import cx_Oracle

class BOrderM(Frame):
    
    def __init__(self,mw,usern):
        self.usenam = usern
        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Manage Orders")
        super().__init__(mw)
        self.rot = mw
        self.tf = Frame(mw)
        self.tf.place(relx=0.1,rely=0.1)
        self.lab1 = Label(self.tf,text='Manage Orders',font=('Arial',18))
        self.lab1.grid(row=0,column=0,padx=100)
        self.bacb = Button(self.tf,text='BACK',command = self.gobac,bg='#f4a690')
        self.bacb.grid(row=0,column=1)
        
        self.dumlab = Label(self,text='')
        self.dumlab.grid(row=0,column=0,pady=70)
        self.accb = Button(self,text='Accept Buy Orders',width=20,command=self.accbuyo,bg='yellow')
        self.accs = Button(self,text='Accept Sell Orders',width=20,command=self.accsello,bg='orange')
        self.orh = Button(self,text='Order History',width=20,command = self.openorh,bg='#bb8cea')
        self.accb.grid(row=1,column=0)
        self.accs.grid(row=2,column=0,pady=10)
        self.orh.grid(row=3,column=0)
        self.pack()
    
    def openorh(self):    
        self.rot.switch_frame('BOrdhis',self.usenam)
        self.destroyf()
        self.destroy()
        
    def accsello(self):
        self.rot.switch_frame('Baccsell',self.usenam)
        self.destroyf()
        self.destroy()
        
    def accbuyo(self):
        self.rot.switch_frame('Baccbuy',self.usenam)
        self.destroyf()
        self.destroy()
        
    def destroyf(self):
        self.tf.destroy()
    
    def gobac(self):
        self.rot.switch_frame('BrokerDashb',self.usenam)
        self.destroyf()
        self.destroy()

        