
from nsetools import Nse
from nsepy import get_history
from datetime import *


class StockServ:
    
    @classmethod
    def getStockHistory(cls,stinf):
        today = date.today()
        delt1 = timedelta(days = -1)
        delt2 = timedelta(days = -10)
        endd = today + delt1
        stad = today + delt2
        data = get_history(symbol=stinf, start=stad, end=endd)
        datelist = data['Close'].keys().tolist()
        closelist = data['Close'].values.tolist()
        openlist = data['Open'].values.tolist()
        lastlist = data['Last'].values.tolist()
        tovlist = data['Turnover'].values.tolist()
        print(datelist)
        print(closelist)
        
        datag = []
        leng = len(datelist)
        
        for i in range(leng):
            cur = []
            cur.append(str(datelist[i]))
            cur.append(openlist[i])
            cur.append(closelist[i])
            cur.append(lastlist[i])
            cur.append(tovlist[i])
            datag.append(cur)
        
        
        nse = Nse()
        q = nse.get_quote(stinf)
        
        secd = q['secDate']
        lastp = q['lastPrice']
        
        secd = (secd.split(' '))[0]
        lastd = datetime.strptime(secd, '%d-%b-%Y').date()
        print(today)
        print(lastd)
        

        if lastd==today:
            datelist.append(lastd)
            closelist.append(lastp)
            
        x = range(len(closelist))
        datestrl = [str(i) for i in datelist]
        return x, closelist, datestrl, datag
    
    @classmethod
    def getLastPrice(cls,stsym):
        nse = Nse()
        q = nse.get_quote(stsym)
        lastp = q['lastPrice']
        return lastp
        