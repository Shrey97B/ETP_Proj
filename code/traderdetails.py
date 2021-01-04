
from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle
import os

class Traderdetail(Frame):

    def __init__(self,master,username):
        master.title("Trader Details")
        master.geometry('600x600')
        master.resizable(0,0)
        super().__init__(master)
        self.rot=master
        self.usenam = username
        self.tf = Frame()
        self.tf.place(relx=0,rely=0)
        self.lab1 = Label(self.tf,text='Account Information',font=('Arial',18))
        self.lab1.grid(row=0,column=0,padx=40,pady=30)
        self.bacb = Button(self.tf,text='BACK',command = self.gobac,bg='#f27979')
        self.bacb.grid(row=0,column=1)
       
        self.tradeun1 = Label(self, text="Trader userame:")
        self.name1 = Label(self, text="Name:")
        self.email1 = Label(self, text="Email:")
        self.contact_no1 = Label(self, text="ContactNo:")
        self.walletid1 = Label(self, text="Walletid:")
      
        dumlab = Label(self,text='')
        dumlab.grid(row=1,column=0,pady=50)
        self.tradeun1.grid(row=2,column=0)
        dumlab2 = Label(self,text='')
        dumlab2.grid(row=3,column=0)
        self.name1.grid(row=4,column=0)
        dumlab3 = Label(self,text='')
        dumlab3.grid(row=5,column=0)
        self.email1.grid(row=6,column=0)
        dumlab4 = Label(self,text='')
        dumlab4.grid(row=7,column=0)
        self.contact_no1.grid(row=8,column=0)
        dumlab5 = Label(self,text='')
        dumlab5.grid(row=9,column=0)
        self.walletid1.grid(row=10,column=0)
        db = DatabaseCon()
        self.con = db.getConnection()
        
        row = self.getTraderDetails()
       
        self.tradeun2 = Label(self, text=row[0])
        self.name2 = Label(self, text=row[2])
        self.email2 = Label(self, text=row[3])
        self.contact_no2 = Label(self, text=row[4])
        self.walletid2 =  Label(self, text=row[5])
        self.tradeun2.grid(row=2,column=1)
        self.name2.grid(row=4,column=1)
        self.email2.grid(row=6,column=1)
        self.contact_no2.grid(row=8,column=1)
        self.walletid2.grid(row=10,column=1)
        self.pack()
        
    def getTraderDetails(self):
        cur = self.con.cursor() 
        cur.execute("""SELECT * FROM TRADER WHERE Tr_un=:param1""",{'param1':self.usenam})
        rows = cur.fetchall()
        row = rows[0]
        return row
        
    def gobac(self):
        self.rot.switch_frame('TraderDashb',self.usenam)
        self.tf.destroy()
        self.destroy()
