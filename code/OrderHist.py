from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class Ordhis(Frame):
    
    def __init__(self,mw,usern):
        self.curid=-1
        self.usenam = usern
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("1150x600")
        mw.resizable(0,0)
        mw.title("Order History")
        super().__init__(mw)
        self.rot = mw
        
        self.dumlab = Label(self,text='',height=1)
        self.dumlab.pack()
        self.lab1 = Label(self,text='Order History',font=('Helvetica',16))
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
        
        res = self.fetchOrderHistory()
        print(res)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Stock Symbol')
        b.config(state=DISABLED)
        b.grid(row=0,column=0)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Broker ID')
        b.config(state=DISABLED)
        b.grid(row=0,column=1)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Order Type')
        b.config(state=DISABLED)
        b.grid(row=0,column=2)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Number of shares')
        b.config(state=DISABLED)
        b.grid(row=0,column=3)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Price per share')
        b.config(state=DISABLED)
        b.grid(row=0,column=4)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Brokerage percent')
        b.config(state=DISABLED)
        b.grid(row=0,column=5)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Total Charge')
        b.config(state=DISABLED)
        b.grid(row=0,column=6)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Status')
        b.config(state=DISABLED)
        b.grid(row=0,column=7)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Order Creation Date')
        b.config(state=DISABLED)
        b.grid(row=0,column=8)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Order Comp Date')
        b.config(state=DISABLED)
        b.grid(row=0,column=9)
        

        indices = [2,3,4,5,6,7,8,9,10,11]
        
        for i in range(len(res)):
            for j in range(10):
                b = Label(self.tf)
                b.grid(row=2*i+1,column=j)
            for j in range(10):
                b = Entry(self.tf,width=18,justify='center')
                if(res[i][indices[j]] is None):
                    data = ''
                else:
                    data = res[i][indices[j]]
                    if j==2:
                        data = 'BUY' if res[i][indices[j]]=='B' else 'SELL'
                    if j==7:
                        if data[0]=='P':
                            data='Pending'
                        elif data[0]=='A':
                            data = 'Accepted'
                        elif data[0]=='E':
                            data = 'Expired'
                        elif data[0]=='C':
                            data = 'Completed'
                b.insert(END,data)
                b.config(state=DISABLED)
                b.grid(row=2*i+2,column=j)
            
        self.con.commit()
        self.pack()
        
    def fetchOrderHistory(self):
        selq = "select * from orders where tr_un='" + self.usenam + "' order by ocreat desc"
        cur = self.con.cursor(selq)
        cur.execute(selq)
        res = cur.fetchall()
        return res
    
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=1120,height=450)
        
    def gobac(self):
        self.rot.switch_frame('OrderM',self.usenam)
        self.tf.destroy()
        self.bf.destroy()
        self.destroy()
