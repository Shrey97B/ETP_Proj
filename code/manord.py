from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class OrderM(Frame):
    
    def __init__(self,mw,usern):
        self.usenam = usern
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Manage Orders")
        super().__init__(mw)
        self.rot = mw
        self.tf = Frame(mw)
        self.tf.place(relx=0.1,rely=0.1)
        self.lab1 = Label(self.tf,text='Manage Orders',font=('Arial',18))
        self.lab1.grid(row=0,column=0,padx=100,pady=30)
        self.bacb = Button(self.tf,text='BACK',command=self.gobac,bg='#f27979')
        self.bacb.grid(row=0,column=1)
        
        self.bf = Frame(mw)
        self.bf.place(relx = 0.1,rely=0.4)
        self.buyor = Button(self.bf,text ='BUY STOCK',width=27,command = self.gotobuys,bg='green')
        self.buyor.grid(row=0, column=0,padx=10)
        self.sellor = Button(self.bf,text ='SELL STOCK',width=27,command = self.gotosells,bg='orange')
        self.sellor.grid(row=0, column=1,padx=10)
        
        self.bacc = Button(self.bf,text='Accepted Bought Orders',width=27,command=self.accbuy,bg='cyan')
        self.bacc.grid(row=1,column=0,pady=10,padx=10)
        self.sacc = Button(self.bf,text='Recently Completed Sell Orders',width=27,command = self.recsell,bg='blue')
        self.sacc.grid(row=1,column=1,pady=1,padx=10)
        self.expen = Button(self.bf,text ='Pending and Recent Expired Orders',width=27,command=self.pne,bg='yellow')
        self.expen.grid(row=2, column=0,padx=10)
        self.prevorders = Button(self.bf,text='Order History',width=27,command=self.orhi,bg='pink')
        self.prevorders.grid(row=2,column=1,padx=10)
        
        self.pack()
    
    def recsell(self):
        self.rot.switch_frame('RecComp',self.usenam)
        self.destroyf()
        self.destroy()
        
    def orhi(self):
        self.rot.switch_frame('Ordhis',self.usenam)
        self.destroyf()
        self.destroy()
        
    def accbuy(self):
        self.rot.switch_frame('Accbuyor',self.usenam)
        self.destroyf()
        self.destroy()
        
    def gotosells(self):
        self.rot.switch_frame('Sellst',self.usenam)
        self.destroyf()
        self.destroy()
        
    def gotobuys(self):
        self.rot.switch_frame('Buyst',self.usenam)
        self.destroyf()
        self.destroy()
        
    def gobac(self):
        self.rot.switch_frame('TraderDashb',self.usenam)
        self.destroyf()
        self.destroy()
        
    def destroyf(self):
        self.tf.destroy()
        self.bf.destroy()
        
    def pne(self):
        self.rot.switch_frame('PandEord',self.usenam)
        self.destroyf()
        self.destroy()
        