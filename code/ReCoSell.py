from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class RecComp(Frame):
    
    def __init__(self,mw,usern):
        self.curid=-1
        self.usenam = usern
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("1150x600")
        mw.resizable(0,0)
        mw.title("Recently completed sell orders")
        super().__init__(mw)
        self.rot = mw
        
        self.dumlab = Label(self,text='',height=1)
        self.dumlab.pack()
        self.lab1 = Label(self,text='Recently completed sell orders',font=('Helvetica',16))
        self.lab1.pack()
        self.bf = Frame()
        self.bf.place(relx=0.8,rely=0.04)
        self.bacb = Button(self.bf,text='BACK',command = self.gobac,bg='#f27979')
        self.bacb.pack()
        self.dumlab2 = Label(self,text='',height=1)
        self.dumlab2.pack()
        self.canvas = Canvas(self)
        self.tf = Frame(self.canvas)
        myscrollbar=Scrollbar(self,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side='right',fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0,0),window=self.tf,anchor='nw')
        self.tf.bind("<Configure>",self.myfunction)
        
        res = self.fetchCompletedSellOrders()

        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Stock Symbol')
        b.config(state=DISABLED)
        b.grid(row=0,column=0)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Broker ID')
        b.config(state=DISABLED)
        b.grid(row=0,column=1)
       
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Number of shares')
        b.config(state=DISABLED)
        b.grid(row=0,column=2)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Price per share')
        b.config(state=DISABLED)
        b.grid(row=0,column=3)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Brokerage percent')
        b.config(state=DISABLED)
        b.grid(row=0,column=4)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Total Charge')
        b.config(state=DISABLED)
        b.grid(row=0,column=5)
        
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Order Creation Date')
        b.config(state=DISABLED)
        b.grid(row=0,column=6)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Order Comp Date')
        b.config(state=DISABLED)
        b.grid(row=0,column=7)
        

        indices = [2,3,5,6,7,8,10,11]
        
        for i in range(len(res)):
            for j in range(10):
                b = Label(self.tf)
                b.grid(row=2*i+1,column=j)
            for j in range(8):
                b = Entry(self.tf,width=18,justify='center')
                if(res[i][indices[j]] is None):
                    data = ''
                else:
                    data = res[i][indices[j]]
                b.insert(END,data)
                b.config(state=DISABLED)
                b.grid(row=2*i+2,column=j)
                
        self.updateOrders()
        self.pack()
    
    def fetchCompletedSellOrders(self):
        selq = "select * from orders where tr_un='" + self.usenam + "' and otype='S' and status='CU' order by ocreat desc"
        cur = self.con.cursor(selq)
        cur.execute(selq)
        res = cur.fetchall()
        return res
    
    def updateOrders(self):
        updq = "Update Orders set status='C' where status='CU' and otype='S' and tr_un='" + self.usenam + "'"
        cur2 = self.con.cursor()
        cur2.execute(updq)
        self.con.commit()
    
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=1120,height=450)
        
    def gobac(self):
        self.rot.switch_frame('OrderM',self.usenam)
        self.tf.destroy()
        self.bf.destroy()
        self.destroy()
