from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class PandEord(Frame):
    
    def __init__(self,mw,usern):
        self.curid=-1
        self.usenam = usern
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("850x600")
        mw.resizable(0,0)
        mw.title("Pending and Recently Expired Orders")
        super().__init__(mw)
        self.rot = mw
        
        self.dumlab = Label(self,text='',height=1)
        self.dumlab.pack()
        self.lab1 = Label(self,text='Pending & Expired Orders',font=('Helvetica',16))
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
        
        res = self.fetchPendingExpiredOrders()

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
        b.insert(END,'Brokerage percent')
        b.config(state=DISABLED)
        b.grid(row=0,column=4)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Status')
        b.config(state=DISABLED)
        b.grid(row=0,column=5)
        b = Entry(self.tf,width=18,justify='center')
        b.insert(END,'Order Creation Date')
        b.config(state=DISABLED)
        b.grid(row=0,column=6)
        

        indices = [2,3,4,5,7,9,10]
        
        for i in range(len(res)):
            for j in range(7):
                b = Label(self.tf)
                b.grid(row=2*i+1,column=j)
            for j in range(7):
                b = Entry(self.tf,width=18,justify='center')
                if j==2:
                    b.insert(END,'BUY' if res[i][indices[j]]=='B' else 'SELL')
                elif j==5:
                    b.insert(END,'Pending' if res[i][indices[j]]=='P' else 'EXPIRED')
                else:
                    b.insert(END,res[i][indices[j]])
                b.config(state=DISABLED)
                b.grid(row=2*i+2,column=j)
            
        print(self.usenam)
        self.updateExpiredOrders()
        self.pack()
        
    def fetchPendingExpiredOrders(self):
        selq = "select * from orders where tr_un='" + self.usenam + "' and status in ('P','E') order by ocreat desc"
        cur = self.con.cursor(selq)
        cur.execute(selq)
        res = cur.fetchall()
        return res

    def updateExpiredOrders(self):
        cur2 = self.con.cursor()
        updq = "Update orders set status = :1 where status = :2 and tr_un = :3"
        print(updq)
        cur2.execute(updq,('ER','E',self.usenam))
        self.con.commit()                
    
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=800,height=400)
        
    def gobac(self):
        self.rot.switch_frame('OrderM',self.usenam)
        self.tf.destroy()
        self.bf.destroy()
        self.destroy()
