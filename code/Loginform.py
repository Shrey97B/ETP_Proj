from tkinter import *
from tkinter import messagebox
from Services.DBconn import DatabaseCon

class LoginFr(Frame):
    
    def __init__(self,mw,params):
        
        db = DatabaseCon()
        self.con = db.getConnection()
        self.createScreen(mw)
        
    def createScreen(self,mw):
        mw.geometry("600x600")
        mw.resizable(0,0)
        mw.title("Login")
        super().__init__(mw)
        
        
        self.rot = mw
        
        self.tf = Frame(mw)
        self.tf.place(relx=0.4,rely=0.2)
        self.bf = Frame(mw)
        self.bf.place(relx = 0.2,rely = 0.5)
        self.thf = Frame(mw)
        self.thf.place(relx=0.3,rely=0.8)
        self.labtitle = Label(self.tf,text = 'ETP manager',font=(36))
        self.labuser = Label(self.bf,text='Enter your username:')
        self.labpass = Label(self.bf,text='Enter the password:')
        self.usetext = Entry(self.bf)
        self.passtext = Entry(self.bf,show='*')
        users = ["Trader","Broker","Admin"]
        self.variable = StringVar(self.bf)
        self.variable.set("Trader")
        self.usert = OptionMenu(self.bf,self.variable,*users)
        self.usert.config(bg='#78e85f')
        self.loginb = Button(self.bf,text="Login",command=self.lbclick,bg='#f7b22a')
        self.signtb = Button(self.thf,text="Trader Registration",command = self.openTR,bg='#b270f4')
        self.signbb = Button(self.thf,text="Broker Registration",command=self.openBR,bg='#70e3f4')
        
        self.labtitle.grid(row=0,column=0)
        self.labuser.grid(row=1,column=0)
        self.usetext.grid(row = 1,column=1)
        self.labpass.grid(row=2,column=0)
        self.passtext.grid(row=2,column=1)
        self.usert.grid(row=3,column=0)
        self.loginb.grid(row = 4,column=0)
        self.signtb.grid(row=0,column=0)
        self.signbb.grid(row=0,column=1)
        self.pack()
        
        
    def lbclick(self):
        utyp = self.variable.get()
        unam = self.usetext.get()
        pas = self.passtext.get()
        b = self.check(unam,pas,utyp)
        if len(b)==0:
            messagebox.showinfo("Invalid authentication","The user name or password is invalid")
        else:
            messagebox.showinfo("","Welcome")
            if utyp=='Trader':
                self.rot.switch_frame('TraderDashb',unam)
            elif utyp=='Broker':
                self.rot.switch_frame('BrokerDashb',unam)
            elif utyp=='Admin':
                self.rot.switch_frame('AdminDashb',unam)
            self.destF()
            self.destroy()
            
    def openTR(self):
        self.rot.switch_frame('TraderR','')
        self.destF()
        self.destroy()
        
    def openBR(self):
        self.rot.switch_frame('BrokerR','')
        self.destF()
        self.destroy()
            
    def destF(self):
        self.tf.destroy()
        self.bf.destroy()
        self.thf.destroy()
            
    def check(self,unam,pas,utyp):
        cur = self.con.cursor()
        if(utyp=='Trader'):
            strq = 'select * from Trader where tr_un=:1 and password=:2'
        elif utyp=='Broker':
            strq = 'select * from Broker where br_un=:1 and password=:2'
        else:
            strq = 'select * from admin where ad_un=:1 and password=:2'
        
        s  = (unam,pas)
        print(s)
        cur.execute(strq,s)
        res = cur.fetchall()
        return res;
