import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


#data = yf.download('AAPL', period='5d')
#

curList = ['AAPL', 'NVDA', 'AMD']

end_date = datetime.now() - timedelta(days=5)
start_date = end_date - timedelta(days=5)

#end_date_pri = end_date()

data = yf.download('AAPL', start=start_date, end=end_date)
print(f"Data from {start_date.date()} to {end_date.date()}")
print(data)

#move_perc = {curr_week: ((data['Close'][-1] - data['Close'][0]) / data['Close'][0]) * 100 for curr_week in curList}




for i in curList:
    ticker = yf.Ticker(i)
    hist = ticker.history(period='5d')
    print(f"--------------- {i} CLOSE DATA: ---------------")
    print(hist['Close'])
    print()
    #for i in curList:
        # 100 / end_date_pri price at the end date 
        # for the end date price / 100 take average change from first 
        # #date let that be the psuedo value 
        # #compare every alue ot tha t one for the week   

def donchian_breakout()