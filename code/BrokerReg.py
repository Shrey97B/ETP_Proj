

from tkinter import *
from tkinter import messagebox
import cx_Oracle
from Services.DBconn import DatabaseCon
import os


class BrokerR(Frame):

    def __init__(self,master,abc):
        
        super().__init__(master)
        dbc = DatabaseCon()
        self.con = dbc.getConnection()
        master.title("Registration form")
        master.geometry("600x600")
        master.resizable(0,0)
        self.rot=master
        self.bacb = Button(self,text='BACK',command=self.gobac,bg='#f4a690')
        self.bacb.place(relx=0.85,rely=0.85)
        self.heading = Label(self, text="Form")
        self.brokun = Label(self, text="Broker userame:")
        self.passw = Label(self, text="Password:")
        self.name = Label(self, text="Name:")
        self.email = Label(self, text="Email:")
        self.contact_no = Label(self, text="ContactNo:")
        self.brok_no = Label(self, text="Brokerage (in %):")
        self.heading.grid(row=0,column=2)
        self.brokun.grid(row=2,column=0)
        self.passw.grid(row=4,column=0)
        self.name.grid(row=6,column=0)
        self.email.grid(row=8,column=0)
        self.contact_no.grid(row=10,column=0)
        self.brok_no.grid(row=12,column=0)
        self.brokun_field = Entry(self)
        self.passw_field = Entry(self,show="*")
        self.name_field = Entry(self)
        self.email_field = Entry(self)
        self.contact_no_field = Entry(self)
        self.brok_no_field = Entry(self)
        self.brokun_field.grid(row=2,column=2,ipadx="100")
        self.passw_field.grid(row=4,column=2,ipadx="100")
        self.name_field.grid(row=6,column=2,ipadx="100")
        self.email_field.grid(row=8,column=2,ipadx="100")
        self.contact_no_field.grid(row=10,column=2,ipadx="100")
        self.brok_no_field.grid(row=12,column=2,ipadx="100")
        self.submit = Button(self,text="Submit",fg="Black",
                            bg="Yellow",command=self.insert)
        self.submit1 = Button(self,text="Reset",fg="Black",
                            bg="Yellow",command=self.clear)
        self.submit.grid(row=16,column=1)
        self.submit1.grid(row=16,column=2)
        self.pack()

    def gobac(self):
        self.rot.switch_frame('LoginFr','')
        self.destroy()
        
    def clear(self):
        self.brokun_field.delete(0,END)
        self.passw_field.delete(0,END)
        self.name_field.delete(0,END)
        self.email_field.delete(0,END)
        self.contact_no_field.delete(0,END)
        self.brok_no_field.delete(0,END)
    
    
    def insert(self):
        if (self.brokun_field.get() == "" or
            self.passw_field.get() == "" or
            self.name_field.get() == "" or
            self.email_field.get() == "" or
            self.contact_no_field.get() == "" or
            self.brok_no_field.get() == ""):
            messagebox.showinfo("","empty input")
    
        else:
            
            brun=self.brokun_field.get()
            passg=self.passw_field.get()
            name=self.name_field.get()
            email1=self.email_field.get()
            cont=self.contact_no_field.get()
            if len(cont)!=10:
                messagebox.showinfo("Error","Invalid contact number")
                return
            
            b = True
            if cont[0]=='0':
                b = False
            for ch in cont:
                if ch.isdigit()==False:
                    b = False
            
            if b==False:
                messagebox.showinfo("Error","Invalid contact number")
                return
                
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
            cur.execute("""SELECT * FROM BROKER WHERE Br_un=:param1""",{'param1':brun})
            rows = cur.fetchall()
            rowcount = len(rows)
            print(rowcount)
            if rowcount==0:
                cur2 = self.con.cursor()
                cur2.execute('INSERT INTO Broker VALUES(:1,:2,:3,:4,:5,:6,:7)',(brun,passg,name,email1,cont,brok1,''))
                messagebox.showinfo("Regform", "Registration successful")
                self.con.commit()
                self.clear()
            else:
                messagebox.showerror("Error","Brokername already exist")
