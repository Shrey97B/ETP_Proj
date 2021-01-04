from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class BrokerDashb(Frame):
    
    def __init__(self,mw,unam):
        
        dbc = DatabaseCon()
        self.con = dbc.getConnection()
        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Broker Dashboard")
        super().__init__(mw)
        
        self.rot = mw
        self.usname = unam

        self.bf = Frame(mw)
        self.bf.place(relx=0.2,rely = 0.6)
        self.v = StringVar()
        self.lab1 = Label(self,textvariable=self.v,font=(28))
        self.lab1.grid(row=0,column=0,pady=20,padx=35)
        self.logo = Button(self,text='Logout',command = self.logout,bg='red')
        self.logo.grid(row=0,column=1,padx=25)
        
        self.but1 = Button(self.bf,text='Account Info',width=18,command=self.openaci,bg='yellow')
        self.but2 = Button(self.bf,text='Update Brokerage',width=18,command=self.openupb,bg='green')
        self.but3 = Button(self.bf,text='Stock Info',width=18,command = self.opensti,bg='cyan')
        self.but4 = Button(self.bf,text='Manage Orders',width=18,command = self.openmord,bg='#bb8cea')
        
        self.but1.grid(row=0,column=0,padx=5,pady = 5)
        self.but2.grid(row=0,column=1,padx=5,pady=5)
        self.but3.grid(row=1,column=0,padx=5,pady=5)
        self.but4.grid(row=1,column=1,padx=5,pady=5)
        self.pack()
        
        self.dispName()
        
    def openupb(self):
        self.rot.switch_frame('Brokerage',self.usname)
        self.destroyf()
        self.destroy()
        
    def opensti(self):
        lis = [self.usname,'BrokerDashb']
        self.rot.switch_frame('StInf',lis)
        self.destroyf()
        self.destroy()
    
    def openaci(self):
        self.rot.switch_frame('Brokerdetail',self.usname)
        self.destroyf()
        self.destroy()
        
    def logout(self):
        self.rot.switch_frame('LoginFr','')
        self.destroyf()
        self.destroy()
        
    def openmord(self):
        self.rot.switch_frame('BOrderM',self.usname)
        self.destroyf()
        self.destroy()
        
    def destroyf(self):
        self.bf.destroy()
        
    def dispName(self):
        cur = self.con.cursor()
        s = self.usname
        strq = "select name from Broker where br_un='" + s + "'"
        cur.execute(strq)
        res = cur.fetchall()
        self.v.set('Welcome ' + res[0][0])