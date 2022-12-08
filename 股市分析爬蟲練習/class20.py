# Yahoo Finance 抓取資料
import pandas_datareader.data as web
from matplotlib import pyplot as plt

# 新建2330.csv檔案
import csv
# csv_file = './新建2330.csv'
# out_csv = csv.writer(open(csv_file, 'w'))

import yfinance as yf
import datetime as dt
import pandas as pd
import csv

yf.pdr_override()
Analysis = './3017.csv'
start = dt.datetime(2021, 9, 29)
end = dt.datetime(2022, 9, 29)

df = web.get_data_yahoo(['3017.TW'], start, end)
df.to_csv(Analysis)

data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')  # Date當作水平顯示(x軸)
price = data['Close']
price.head()

plt.plot(price)
plt.show()
