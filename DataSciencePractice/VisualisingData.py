# @author: Simranjit Singh
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
start = datetime.datetime(2017,1,1)
end = datetime.datetime(2020,1,1)
att = web.DataReader("T", "yahoo", start, end)
print(att)
highs= att['High'].tolist()
print(highs[-10])
# att['Adj Close'].plot()
# plt.legend()
# plt.show()

att[['High','Close']].plot()
plt.show()