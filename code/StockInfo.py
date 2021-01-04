from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Services.DBconn import DatabaseCon
from configparser import ConfigParser
from Services.StockService import StockServ
import cx_Oracle
import numpy

class StInf(Frame):
    
    def __init__(self,mw,lis):
        self.usenam = lis[0]
        self.backcl = lis[1]
        db = DatabaseCon()
        self.con = db.getConnection()
        mw.geometry("900x600")
        mw.resizable(0,0)
        mw.title("Stock Information")
        super().__init__(mw)
        self.rot = mw
        self.tf = Frame()
        self.tf.place(relx=0.01)
        self.lb = Listbox(self.tf,width=18,height=70,font=('Helvetica',11))
        
        self.lb.pack()
        self.bf = Frame()
        self.bf.place(relx = 0.3)
        self.lone = Label(self.bf,text='STOCK INFORMATION',font=('ARIAL',15))
        self.lone.grid(row=0,column=0)
        self.backb = Button(self.bf,text='BACK',command=self.gobac,bg='#f27979')
        self.backb.grid(row=0,column=1)
        self.v = [0]
        self.x = [0]
        self.fig = Figure(figsize=(6,3))
        self.a = self.fig.add_subplot(111)
        self.line1, = self.a.plot(self.v,self.x,color='red')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.bf)
        self.canvas.get_tk_widget().grid(row=1,column=0)
        self.canvas.draw()
        self.thf = Frame()
        self.thf.place(relx=0.2,rely=0.6)
        height = 1
        width = 5
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = Entry(self.thf, text="",state=DISABLED)
                b.grid(row=i, column=j)
        self.pack()
        self.lb.bind('<<ListboxSelect>>', self.changedata)
        self.populatestocks()
        
    def gobac(self):
        self.rot.switch_frame(self.backcl,self.usenam)
        self.destroyf()
        self.destroy()
        
    def destroyf(self):
        self.tf.destroy()
        self.bf.destroy()
        self.thf.destroy()
        
    def changedata(self,evt):
        widg = evt.widget
        ind = int(widg.curselection()[0])
        stsym = widg.get(ind)        
        
        x1,y1,z1,data = StockServ.getStockHistory(stsym)
        print(x1)
        print(y1)
        print(z1)
        self.changeg(x1,y1,z1)
        self.thf.destroy()
        self.thf = Frame()
        self.thf.place(relx=0.2,rely=0.5)
        strq = 'select stname,avshare from stock where stsymb=:1'
        ls = [stsym]
        t = tuple(ls)
        print(t)
        cur = self.con.cursor()
        cur.execute(strq,t)
        res = cur.fetchall()
        labt = Label(self.thf,text='Company Name: ' + str(res[0][0]))
        labt.grid(row=0,column=0)
        b = Entry(self.thf)
        b.insert(END,'Time')
        b.config(state='disabled')
        b.grid(row=2,column=0)
        b = Entry(self.thf)
        b.insert(END,'Open')
        b.config(state='disabled')
        b.grid(row=2,column=1)
        b = Entry(self.thf)
        b.insert(END,'Close')
        b.config(state='disabled')
        b.grid(row=2,column=2)
        b = Entry(self.thf)
        b.insert(END,'Last')
        b.config(state='disabled')
        b.grid(row=2,column=3)
        b = Entry(self.thf)
        b.insert(END,'Turnover (in Lacs)')
        b.config(state='disabled')
        b.grid(row=2,column=4)
        height = len(data)
        for i in range(height):
            ind = height - i -1
            b = Entry(self.thf)
            b.insert(END,data[ind][0])
            b.config(state='disabled')
            b.grid(row=i+3, column=0)
            b = Entry(self.thf)
            b.insert(END,data[ind][1])
            b.config(state='disabled')
            b.grid(row=i+3, column=1)
            b = Entry(self.thf)
            b.insert(END,data[ind][2])
            b.config(state='disabled')
            b.grid(row=i+3, column=2)
            b = Entry(self.thf)
            b.insert(END,data[ind][3])
            b.config(state='disabled')
            b.grid(row=i+3, column=3)
            b = Entry(self.thf)
            b.insert(END,data[ind][4])
            b.config(state='disabled')
            b.grid(row=i+3, column=4)

        
    def changeg(self,x1,y1,z1):
        self.line1.set_xdata(x1)
        self.line1.set_ydata(y1)
        ax = self.canvas.figure.axes[0]
        ax.set_xlim(min(x1), max(x1))
        ax.set_ylim(min(y1)-1, max(y1)+1)
        ax.set_xticklabels(z1)
        self.canvas.draw()

    def populatestocks(self):
        cur = self.con.cursor()
        srtq = 'select * from stock'
        cur.execute(srtq)
        res = cur.fetchall()
        for x in res:
            self.lb.insert(END,x[0])
        
        