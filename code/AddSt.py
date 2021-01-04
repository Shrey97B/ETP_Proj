from tkinter import *
import cx_Oracle
from Services.DBconn import DatabaseCon
from Services.StockService import StockServ
import os

class AddStock(Frame):

    def __init__(self,master,abc):
        
        super().__init__(master)
        self.usename = abc
        master.title("Add Stock Form")
        master.geometry("600x600")
        master.resizable(0,0)
        self.rot=master
        dbc = DatabaseCon()
        self.con = dbc.getConnection()

        self.heading = Label(self, text="Add Stock Form")
        self.stsymlab = Label(self, text="Stock Symbol:")
        self.stcomplab = Label(self, text="Company Name:")
        self.avsharelab = Label(self, text="Available Shares:")
        self.heading.grid(row=0,column=2)
        self.bacb = Button(self,text='BACK',command=self.gobac,bg='#f4a690')
        self.bacb.grid(row=0,column=4)
        self.stsymlab.grid(row=2,column=0)
        self.stcomplab.grid(row=4,column=0)
        self.avsharelab.grid(row=6,column=0)
        self.stsym_field = Entry(self)
        self.stcomp_field = Entry(self)
        self.avshare_field = Entry(self)
        self.stsym_field.grid(row=2,column=2,ipadx="100")
        self.stcomp_field.grid(row=4,column=2,ipadx="100")
        self.avshare_field.grid(row=6,column=2,ipadx="100")
        self.submit = Button(self,text="Submit",fg="Black",bg="Yellow",command=self.insert)

        self.submit.grid(row=8,column=0)

        self.pack()
        
    def gobac(self):
        self.rot.switch_frame('AdminDashb',self.usename)
        self.destroy()
        
    def insert(self):
        #code inserting stock symbol
        if (self.stsym_field.get() == "" or
            self.stcomp_field.get() == "" or
            self.avshare_field.get() == ""):
            messagebox.showinfo("","empty input")
            return
        
        StSym = self.stsym_field.get()
        CompName = self.stcomp_field.get()
        AvShare = self.avshare_field.get()
        try:
            AvShare = int(AvShare)
        except ValueError as e:
            messagebox.showerror('Error','Invalid Number of Share')
            return
        
        if AvShare<0:
            messagebox.showerror('Error','Invalid Number of Share')
            return
        
        cur=self.con.cursor()
        cur.execute("""SELECT stsymb FROM stock WHERE stsymb=:param1""",{'param1':StSym})
        rows = cur.fetchall()
        rowcount = len(rows)
        print(rowcount)
        if rowcount==0:
            cur2 = self.con.cursor()
            lastp = StockServ.getLastPrice(StSym)
            cur2.execute('INSERT INTO stock VALUES(:1,:2,:3,:4)',(StSym,CompName,lastp,AvShare))
            self.con.commit()
            messagebox.showinfo("Form", "Stock Insertion successful")
            self.clear()
        else:
            messagebox.showerror("Error","Stock Symbol already exists")
            
    def clear(self):
        self.stsym_field.delete(0,END)
        self.stcomp_field.delete(0,END)
        self.avshare_field.delete(0,END)
