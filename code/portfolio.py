


from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle
import os
class Stockdetail(Frame):

    def __init__(self,mw,username):
        
        super().__init__(mw)
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("600x600")
        mw.title("Portfolio")
        super().__init__(mw)
        self.usename = username
        self.rot = mw
        
        self.lab1 = Label(self,text='Portfolio',font=('Helvetica',16))
        self.lab1.pack()
        
        self.bacb = Button(self,text='BACK',command=self.gobac,bg='#f27979')
        self.bacb.place(relx=0.8,rely=0.02)
        self.dumlab = Label(self,text='')
        self.dumlab.pack()
        self.canvas = Canvas(self)
        self.tf = Frame(self.canvas)
        myscrollbar=Scrollbar(self,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side='right',fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0,0),window=self.tf,anchor='nw')
        self.tf.bind("<Configure>",self.myfunction)
        
        rows = self.fetchPortfolioData()

        width = 3
        b = Entry(self.tf,justify='center')
        b.insert(END,'Stock Name')
        b.config(state=DISABLED)
        b.grid(row=0,column=0)
        b = Entry(self.tf,justify='center')
        b.insert(END,'Stock Symbol')
        b.config(state=DISABLED)
        b.grid(row=0,column=1)
        b = Entry(self.tf,justify='center')
        b.insert(END,'Quantity')
        b.config(state=DISABLED)
        b.grid(row=0,column=2)
       
        for i in range(len(rows)):
                ty = rows[i]
                for j in range(width):                     
                     b = Entry(self.tf,justify='center')
                     b.insert(END,ty[j])
                     b.config(state=DISABLED)
                     b.grid(row=i+1,column=j)
        self.pack()
        
    
    def fetchPortfolioData(self):
        cur = self.con.cursor()
        cur.execute("""SELECT STOCK.STSYMB,STOCK.STNAME,PORTFOLIO.QUANTITY FROM PORTFOLIO INNER JOIN STOCK ON PORTFOLIO.STSYMB = STOCK.STSYMB AND Tr_un = :param1""",{'param1':self.usename})
        rows = cur.fetchall()
        print(rows)
        return rows
    
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=350,height=400)
            
    def gobac(self):
        self.rot.switch_frame('TraderDashb',self.usename)
        self.tf.destroy()
        
        self.destroy()
