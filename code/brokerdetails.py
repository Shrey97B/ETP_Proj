


from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle
import os

class Brokerdetail(Frame):

    def __init__(self,master,username):
        
        master.title("Broker Details")
        master.geometry("600x600")
        master.resizable(0,0)
        super().__init__(master)
       
        self.rot=master
        self.usenam = username
        self.tf = Frame()
        self.tf.place(relx=0,rely=0)
        self.lab1 = Label(self.tf,text='Account Information',font=('Arial',18))
        self.lab1.grid(row=0,column=0,padx=40,pady=30)
        self.bacb = Button(self.tf,text='BACK',command = self.gobac)
        self.bacb.grid(row=0,column=1)
        
        dumlab = Label(self,text='')
        dumlab.grid(row=1,column=0,pady=50)
        self.brokun3 = Label(self, text="Broker userame:")
        self.name3 = Label(self, text="Name:")
        self.email3 = Label(self, text="Email:")
        self.contact_no3 = Label(self, text="ContactNo:")
        self.brokno3 = Label(self, text="Brokerage No:")
       
        self.brokun3.grid(row=2,column=0)
        dumlab2 = Label(self,text='')
        dumlab2.grid(row=3,column=0)
        self.name3.grid(row=4,column=0)
        dumlab3 = Label(self,text='')
        dumlab3.grid(row=5,column=0)
        self.email3.grid(row=6,column=0)
        dumlab4 = Label(self,text='')
        dumlab4.grid(row=7,column=0)
        self.contact_no3.grid(row=8,column=0)
        dumlab5 = Label(self,text='')
        dumlab5.grid(row=9,column=0)
        self.brokno3.grid(row=10,column=0)

        
        row = self.fetchBrokerDetails()
        self.brokun4 = Label(self, text=row[0])
        self.name4 = Label(self, text=row[2])
        self.email4 = Label(self, text=row[3])
        self.contact_no4 = Label(self, text=row[4])
        self.brokno4 = Label(self, text=row[5])
        self.brokun4.grid(row=2,column=1)
        self.name4.grid(row=4,column=1)
        self.email4.grid(row=6,column=1)
        self.contact_no4.grid(row=8,column=1)
        self.brokno4.grid(row=10,column=1)
        self.pack()
        
    def fetchBrokerDetails(self):
        connection = DatabaseCon().getConnection()
        cur = connection.cursor()
        cur.execute("""SELECT * FROM BROKER WHERE Br_un=:param1""",{'param1':self.usenam})
        rows = cur.fetchall()
        row = rows[0]
        return row
        
    def gobac(self):
        self.rot.switch_frame('BrokerDashb',self.usenam)
        self.tf.destroy()
        self.destroy()
