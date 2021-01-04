import tkinter as tk
from Loginform import LoginFr
from TraderDash import TraderDashb
from StockInfo import StInf
from manord import OrderM
from Buystock import Buyst
from AcceptedBuys import Accbuyor
from pendexp import PandEord
from Sellstock import Sellst
from OrderHist import Ordhis
from ReCoSell import RecComp
from traderreg import TraderR
from BrokerReg import BrokerR
from traderdetails import Traderdetail
from BrokerDash import BrokerDashb
from brokerdetails import Brokerdetail
from bmanord import BOrderM
from accbuy import Baccbuy
from accsell import Baccsell
from AdminDash import AdminDashb
from AddSt import AddStock
from portfolio import Stockdetail
from brokerage import Brokerage
from BOrdhis import BOrdhis

class SampleApp(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.pns = {}
        
        for F in (LoginFr, TraderDashb,StInf,OrderM,Buyst,Accbuyor,PandEord,Sellst,Ordhis,RecComp,TraderR,BrokerR,Traderdetail,BrokerDashb,Brokerdetail,BOrderM,Baccbuy,Baccsell,AdminDashb,Stockdetail,Brokerage,BOrdhis,AddStock):
            page_name = F.__name__
            self.pns[page_name] = F
        self.switch_frame('LoginFr','')
        
    def switch_frame(self, frame_class,params):
        
        F = self.pns[frame_class]
        new_frame = F(self,params)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
        
root = SampleApp()
root.mainloop()