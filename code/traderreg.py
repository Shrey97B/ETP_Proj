

from tkinter import *
from tkinter import messagebox
import cx_Oracle
from Services.DBconn import DatabaseCon
import os

class TraderR(Frame):

    def __init__(self,master,abc):
        
        super().__init__(master)
        master.title("Registration form")
        master.geometry("600x600")
        master.resizable(0,0)
        self.rot=master
        self.bacb = Button(self,text='BACK',command=self.gobac,bg='#f4a690')
        self.bacb.place(relx=0.85,rely=0.85)
        self.heading = Label(self, text="Form")
        self.tradeun = Label(self, text="Trader userame:")
        self.passw = Label(self, text="Password:")
        self.name = Label(self, text="Name:")
        self.email = Label(self, text="Email:")
        self.contact_no = Label(self, text="ContactNo:")
        self.wallid = Label(self, text="Wallet id:")
        self.heading.grid(row=0,column=2)
        self.tradeun.grid(row=2,column=0)
        self.passw.grid(row=4,column=0)
        self.name.grid(row=6,column=0)
        self.email.grid(row=8,column=0)
        self.contact_no.grid(row=10,column=0)
        self.wallid.grid(row=12,column=0)
        self.tradeun_field = Entry(self)
        self.passw_field = Entry(self,show="*")
        self.name_field = Entry(self)
        self.email_field = Entry(self)
        self.contact_no_field = Entry(self)
        self.wallid_field = Entry(self)
        self.tradeun_field.grid(row=2,column=2,ipadx="100")
        self.passw_field.grid(row=4,column=2,ipadx="100")
        self.name_field.grid(row=6,column=2,ipadx="100")
        self.email_field.grid(row=8,column=2,ipadx="100")
        self.contact_no_field.grid(row=10,column=2,ipadx="100")
        self.wallid_field.grid(row=12,column=2,ipadx="100")
        self.submit = Button(self,text="Submit",fg="Black",
                            bg="Yellow",command=self.insert)
        self.submit1 = Button(self,text="Reset",fg="Black",
                            bg="Yellow",command=self.clear)
        self.submit.grid(row=14,column=1)
        self.submit1.grid(row=14,column=2)
        self.pack()


    def clear(self):
        self.tradeun_field.delete(0,END)
        self.passw_field.delete(0,END)
        self.name_field.delete(0,END)
        self.email_field.delete(0,END)
        self.contact_no_field.delete(0,END)
        self.wallid_field.delete(0,END)
    
    def gobac(self):
        self.rot.switch_frame('LoginFr','')
        self.destroy()
        
    def insert(self):
        if (self.tradeun_field.get() == "" or
            self.passw_field.get() == "" or
            self.name_field.get() == "" or
            self.email_field.get() == "" or
            self.contact_no_field.get() == "" or
            self.wallid_field.get() == ""):
            messagebox.showinfo("","empty input")
    
        else:
            dbc = DatabaseCon()
            self.con = dbc.getConnection()
            trun=self.tradeun_field.get()
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
                
            wall1=self.wallid_field.get()
            cur=self.con.cursor()
            cur.execute("""SELECT * FROM TRADER WHERE Tr_un=:param1""",{'param1':trun})
            rows = cur.fetchall()
            rowcount = len(rows)
            print(rowcount)
            if rowcount==0:
                cur2 = self.con.cursor()
                cur2.execute("""SELECT * FROM DUM_WALL WHERE Wallet_Id=:param1""",{'param1':wall1})
                rows = cur2.fetchall()
                rowcount1 = len(rows)
                print(rowcount1)
                if rowcount1==0:
                    messagebox.showerror("Error","Wallet ID INVALID")
                else:
                    cur3 = self.con.cursor()
                    cur3.execute('INSERT INTO Trader VALUES(:1,:2,:3,:4,:5,:6)',(trun,passg,name,email1,cont,wall1))
                    messagebox.showinfo("Regform", "Registration successful")
                    self.con.commit()
                    self.clear()
            else:
                messagebox.showerror("Error","Tradername already exist")
                
    



