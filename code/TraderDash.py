from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class TraderDashb(Frame):
    
    def __init__(self,mw,unam):
        
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Trader Dashboard")
        super().__init__(mw)
        
        self.rot = mw
        self.usname = unam

        self.bf = Frame(mw)
        self.bf.place(relx=0.2,rely = 0.6)
        self.v = StringVar()
        self.lab1 = Label(self,textvariable=self.v,font=(28))
        self.lab1.grid(row=0,column=0,pady=20,padx=35)
        self.logo = Button(self,text='Logout',command = self.logout,bg='#f27979')
        self.logo.grid(row=0,column=1,padx=25)
        
        self.but1 = Button(self.bf,text='Account Info',command=self.openaci,width=18,bg='#6ff7f7')
        self.but2 = Button(self.bf,text='Portfolio',width=18,command=self.openpo,bg='#f4c16e')
        self.but3 = Button(self.bf,text='Stock Info',command = self.opensti,width=18,bg='yellow')
        self.but4 = Button(self.bf,text='Order',command=self.openord,width=18,bg='green')
        
        self.but1.grid(row=0,column=0,padx=5,pady = 5)
        self.but2.grid(row=0,column=1,padx=5,pady=5)
        self.but3.grid(row=1,column=0,padx=5,pady=5)
        self.but4.grid(row=1,column=1,padx=5,pady=5)
        self.pack()
        
        self.dispName()
    
    def openpo(self):
        self.rot.switch_frame('Stockdetail',self.usname)
        self.destroyf()
        self.destroy()
        
    def logout(self):
        self.rot.switch_frame('LoginFr','')
        self.destroyf()
        self.destroy()
        
    def openaci(self):
        self.rot.switch_frame('Traderdetail',self.usname)
        self.destroyf()
        self.destroy()
    
    def openord(self):
        self.rot.switch_frame('OrderM',self.usname)
        self.destroyf()
        self.destroy()
        
    def opensti(self):
        lis = [self.usname,'TraderDashb']
        self.rot.switch_frame('StInf',lis)
        self.destroyf()
        self.destroy()
        
    def destroyf(self):
        self.bf.destroy()
        
    def dispName(self):
        cur = self.con.cursor()
        s = self.usname
        strq = "select name from Trader where tr_un='" + s + "'"
        cur.execute(strq)
        res = cur.fetchall()
        self.v.set('Welcome ' + res[0][0])

    