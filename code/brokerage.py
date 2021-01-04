

from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle
import os
class Brokerage(Frame):

    def __init__(self,mw,username):
        
        super().__init__(mw)
        dbc = DatabaseCon()
        self.con = dbc.getConnection()

        mw.geometry("600x600")
        mw.title("Brokerage")
        super().__init__(mw)
        self.usename = username
        self.rot = mw
        
        self.lab1 = Label(self,text='Update Brokerage',font=('Helvetica',16))
        self.lab1.grid(row=0,column=0,padx=45,pady=10)
        
        self.bacb = Button(self,text='BACK',command=self.gobac)
        self.bacb.grid(row=0,column=1,padx=5,pady=10)
        
        self.tf = Frame()
        self.tf.place(relx=0.1,rely=0.4)

        old_br = self.fetchBrokerage()
        self.brok_no = Label(self.tf, text="Old Brokerage Rate:")
        self.brok_no.grid(row=0,column=0)
        self.brok_no1 = Label(self.tf, text=old_br)
        self.brok_no1.grid(row=0,column=1)
        self.brok_no2 = Label(self.tf, text="Enter New Brokerage Rate:")
        self.brok_no2.grid(row=1,column=0)
        self.brok_no_field = Entry(self.tf)
        self.user= username
        print(self.user)
        self.brok_no_field.grid(row=1,column=1,ipadx="10")
        self.submit = Button(self.tf,text="Submit",fg="Black",
                            bg="Yellow",command=self.update)
        self.submit1 = Button(self.tf,text="Reset",fg="Black",
                            bg="Yellow",command=self.clear)
        self.submit.grid(row=2,column=0)
        self.submit1.grid(row=2,column=1)
        self.pack()


    def clear(self):
        self.brok_no_field.delete(0,END)
        
    def fetchBrokerage(self):
        cur=self.con.cursor()
        cur.execute("""SELECT BROKERAGE FROM BROKER WHERE Br_un=:param1""",{'param1':self.usename})
        rows = cur.fetchall()
        return rows[0]
    
    def update(self):
        brok1=self.brok_no_field.get()
        try:
            brok1 = int(brok1)
        except ValueError as e:
            messagebox.showerror('Error','Invalid percentage')
            return
                
        if brok1<0 or brok1>=100:
            messagebox.showerror('Error','Invalid percentage')
            return  
        
        cur=self.con.cursor()
        cur.execute("""UPDATE BROKER SET BROKERAGE=:param1 WHERE Br_un=:param2""",{'param1':brok1,'param2':self.user})
        messagebox.showinfo("Update", "Update successful")
        
        self.con.commit()
        self.rot.switch_frame('Brokerage',self.usename)
        self.tf.destroy()
        self.destroy()
        
    def gobac(self):
        self.rot.switch_frame('BrokerDashb',self.usename)
        self.tf.destroy()
        self.destroy()
            

