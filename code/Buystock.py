from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class Buyst(Frame):
    
    def __init__(self,mw,usern):
        self.usenam = usern
        dbc = DatabaseCon()
        self.con = dbc.getConnection()
        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Buy Stock")
        super().__init__(mw)
        self.rot = mw
        
        self.lab1 = Label(self,text='Buy Stock',font=('Helvetica',16))
        self.lab1.grid(row=0,column=0,pady=15)
        
        self.bacb = Button(self,text='BACK',command=self.gobac,bg='#f27979')
        self.bacb.grid(row=0,column=1,padx=38)
        
        self.tf = Frame()
 
        self.lab2 = Label(self,text='')
        self.lab2.grid(row=1,column=0)
        self.tf.place(relx = 0.15,rely=0.15)
        self.lab3 = Label(self.tf,text='Select the stock')
        self.lab3.grid(row=2,column=0,padx=5)
        
        res = self.fetchstocks()

        self.stsymbs = []
        self.stnam = {}
        for x in res:
            self.stsymbs.append(x[0])
            self.stnam[x[0]] = x[1]
        
        print(self.stsymbs)
        self.selstock = StringVar(self)
        self.selstock.set(self.stsymbs[0])
        self.stocks = OptionMenu(self.tf,self.selstock,*self.stsymbs,command=self.stchan)
        self.stocks.config(bg='orange')
        self.stocks.grid(row=2,column=1,padx=5)
        self.lab3 = Label(self.tf,text='Company Name')
        self.lab4 = Label(self.tf,text=self.stnam[self.stsymbs[0]])
        self.lab3.grid(row=3,column=0,pady=4)
        self.lab4.grid(row=3,column=1,pady=4)
        
        res = self.fetchbrokers()
        
        self.brokerids = []
        self.brokernames = {}
        self.brokerages = {}

        for x in res:
            self.brokerids.append(x[0])
            self.brokernames[x[0]] = x[1]
            self.brokerages[x[0]] = x[2]
        
        self.dumlab = Label(self.tf,text='')
        self.dumlab.grid(row=4,column=0,pady=4)
        self.br1lab = Label(self.tf,text='Select broker using id')
        self.br1lab.grid(row=5,column=0)
        self.selbr = StringVar(self)
        self.selbr.set(self.brokerids[0])
        self.brokers = OptionMenu(self.tf,self.selbr,*self.brokerids,command=self.brchan)
        self.brokers.config(bg='cyan')
        self.brokers.grid(row=5,column=1)
        self.br2lab = Label(self.tf,text='Broker Name')
        self.brname = Label(self.tf,text=self.brokernames[self.brokerids[0]])
        self.br2lab.grid(row=6,column=0)
        self.brname.grid(row=6,column=1)
        self.br3lab = Label(self.tf,text='Brokerage')
        self.broklab = Label(self.tf,text=self.brokerages[self.brokerids[0]])
        self.br3lab.grid(row=7,column=0)
        self.broklab.grid(row=7,column=1)
        self.dumlab2 = Label(self.tf,text='')
        self.dumlab2.grid(row=8,column=0,pady=4)
        
        self.numshlab = Label(self.tf,text='Number of shares to purchase:')
        self.numshen = Entry(self.tf)
        self.numshlab.grid(row=9,column=0)
        self.numshen.grid(row=9,column=1)
        
        self.dumlab3 = Label(self.tf,text='')
        self.dumlab3.grid(row=10,column=0,pady=4)
        self.dumlab4 = Label(self.tf,text='')
        self.dumlab4.grid(row=11,column=0,pady=4)
        self.dumlab5 = Label(self.tf,text='')
        self.dumlab5.grid(row=12,column=0,pady=4)
        
        self.buyb = Button(self.tf,text='Buy Stocks',command=self.insbuyord,bg='blue')
        self.buyb.place(relx=0.5,rely=0.8)
        
        self.pack()
        
    def fetchstocks(self):
        cur = self.con.cursor()
        stocksq = 'select stsymb,stname from stock'
        cur.execute(stocksq)
        res = cur.fetchall()
        return res
    
    def fetchbrokers(self):
        cur = self.con.cursor()
        brokersq = 'select br_un, name, brokerage from broker'
        cur.execute(brokersq)
        res = cur.fetchall()
        return res
        
    def insbuyord(self):
        cur = self.con.cursor()
        trunam = self.usenam
        stsymb = self.selstock.get()
        brunam = self.selbr.get()
        brf = self.brokerages[brunam]
        try:
            ns = int(self.numshen.get())
        except ValueError as e:
            messagebox.showinfo("Invalid info","Number of shares are invalid")
            return
        
        if(ns<=0):
            messagebox.showinfo("Invalid info","Number of shares are invalid")
            return
        
        insq1 = 'insert into orders(Order_Id,Tr_un,stsymb,br_un,otype,num_share,status,ocreat,brfee) values(Order_Ids.nextval,:1,:2,:3,:4,:5,:6,sysdate,:7) returning Order_Id into :8'
        newid = cur.var(str)
        sql_params = (trunam,stsymb,brunam,'B',ns,'P',brf,newid)
        cur.execute(insq1, sql_params)
        print(newid)
        nid= (newid.getvalue())[0]
        print(nid)
        
        dbc = DatabaseCon()
        dbc.createExecuteBuyOrderExpJob(self.con,nid)
        print(nid)
        messagebox.showinfo('','Order Request has been placed.\nIt will expire after 5 minutes if not completed')
        self.numshen.delete(0,END)
        return
    
    def brchan(self,event):
        self.brname.config(text=self.brokernames[self.selbr.get()])
        self.broklab.config(text=self.brokerages[self.selbr.get()])
        
    def stchan(self,event):
        self.lab4.config(text=self.stnam[self.selstock.get()])
    
    def gobac(self):
        self.rot.switch_frame('OrderM',self.usenam)
        self.tf.destroy()
        self.destroy()