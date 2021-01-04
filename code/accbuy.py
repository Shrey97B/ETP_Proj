from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon
import cx_Oracle

class Baccbuy(Frame):
    
    def __init__(self,mw,usern):
        self.curid=-1
        self.usenam = usern

        dbc = DatabaseCon()
        self.con = dbc.getConnection()

        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Accept Buy Orders")
        super().__init__(mw)
        self.rot = mw
        self.tf = Frame()
        self.tf.place(relx=0.01)
        self.lb = Listbox(self.tf,width=18,height=70,font=('Helvetica',11))
        self.lb.pack()

        self.accumulateOrderData()
        
        self.bf = Frame()
        self.bf.place(relx = 0.3)
        self.lone = Label(self.bf,text='Accept Buy Orders',font=('ARIAL',15))
        self.lone.grid(row=0,column=0)
        self.backb = Button(self.bf,text='BACK',command=self.gobac)
        self.backb.grid(row=0,column=1,padx = 60,pady=10)
        
        self.thf = Frame()
        self.thf.place(relx=0.3,rely=0.2)
        self.lb.bind('<<ListboxSelect>>', self.showorddet)
        
        self.pack()
        
    def accumulateOrderData(self):
        cur = self.con.cursor()
        
        strq1 = 'select * from orders where br_un=:1 and otype=:2 and status=:3 order by ocreat'
        
        t = (self.usenam,'B','P')
        cur.execute(strq1,t)
        res = cur.fetchall()
        self.orderids = []
        self.stsymbs = []
        self.traderids = []
        self.numshares = []
        self.datecreat = []
        self.brokerages = []
        
        for x in range(len(res)):
            self.lb.insert(END,'Order Number ' + str(x+1))
            self.orderids.append(res[x][0])
            self.stsymbs.append(res[x][2])
            self.traderids.append(res[x][1])
            self.numshares.append(res[x][5])
            self.brokerages.append(res[x][7])
            dc = str(res[x][10])
            self.datecreat.append(dc)

    def showorddet(self,evt):
        self.thf.destroy()
        self.thf = Frame()
        self.thf.place(relx=0.3,rely=0.2)
        widg = evt.widget
        self.ind = int(widg.curselection()[0])
        currst = self.stsymbs[self.ind]
        self.curid = self.orderids[self.ind]
        self.stlab = Label(self.thf,text='Stock Name:',width=20,anchor=E,font=(9))
        self.stlabd = Label(self.thf,text = currst,font=(9))
        self.stlab.grid(row=0,column=0,padx=5)
        self.stlabd.grid(row=0,column=1)
        self.tridlab = Label(self.thf,text='Trader Id:',width=20,anchor=E,font=(9))
        self.tridlabd = Label(self.thf,text=self.traderids[self.ind],font=(9))
        self.tridlab.grid(row=1,column=0,padx=5)
        self.tridlabd.grid(row=1,column=1)
        self.nslab = Label(self.thf,text='Number of shares to buy:',width=20,anchor=E,font=(9))
        self.nslabd = Label(self.thf,text=self.numshares[self.ind],font=(9))
        self.nslab.grid(row=2,column=0,padx=5)
        self.nslabd.grid(row=2,column=1)
        self.broklab = Label(self.thf,text='Brokerage:',width=20,anchor=E,font=(9))
        self.broklabd = Label(self.thf,text=self.brokerages[self.ind],font=(9))
        self.broklab.grid(row=3,column=0,padx=5)
        self.broklabd.grid(row=3,column=1)
        self.ordat = Label(self.thf,text='Order creation date:',width=20,anchor=E,font=(9))
        self.ordatd = Label(self.thf,text=self.datecreat[self.ind],font=(9))
        self.ordat.grid(row=4,column=0,padx=5)
        self.ordatd.grid(row=4,column=1)
        self.dumlab = Label(self.thf,text='')
        self.dumlab.grid(row=5,column=0,pady=4)
        self.payb = Button(self.thf,text='Accept Order',command=self.accord,bg='yellow')
        self.payb.grid(row=6,column=0)
        
    def destroyf(self):
        self.tf.destroy()
        self.bf.destroy()
        self.thf.destroy()
        
    def gobac(self):
        self.rot.switch_frame('BOrderM',self.usenam)
        self.destroyf()
        self.destroy()
        
    def accord(self):
        orid = self.orderids[self.ind]
        selq='select status from orders where order_id=' + str(orid) + ''
        cur = self.con.cursor()
        cur.execute(selq)
        res = cur.fetchall()
        stat = res[0][0]
        if(stat != 'P'):
            messagebox.showinfo('','Order has expired')
            self.rot.switch_frame('Baccbuy',self.usenam)
            self.destroyf()
            self.destroy()
            return
        else:
            updq = "update orders set status='A' where order_id=" + str(orid) + ""
            cur.execute(updq)
            self.con.commit()
            messagebox.showinfo('','Order has been accepted')
            self.rot.switch_frame('Baccbuy',self.usenam)
            self.destroyf()
            self.destroy()
            return