from mplfinance.original_flavor import candlestick_ohlc  # 畫蠟燭圖
from matplotlib import pyplot as plt
from matplotlib import style

import matplotlib.dates as mdates
import pandas as pd

style.use('dark_background')

Analysis = './AAPL.csv'

data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')

price = data['Close']
price.head()

moving_avg = price.rolling(5).mean()
moving_avg20 = price.rolling(20).mean()


moving_avg_mstd = price.rolling(20).std()

top = plt.subplot2grid((12, 9), (0, 0), rowspan=9, colspan=9)
bottom = plt.subplot2grid((12, 9), (10, 0), rowspan=2, colspan=9)

# 加入網格
top.grid(which='both', alpha=0.3)

data = data.reset_index()
data['Date'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
candlestick = [tuple(x) for x in data[['Date', 'Open', 'High', 'Low', 'Close']].values]
candlestick_ohlc(top, candlestick, width=0.5, colorup='r', colordown='green', alpha=0.7)

top.plot(moving_avg, color='b', linewidth=1, alpha=0.7, label='MA5')
top.plot(moving_avg20, color='r', linewidth=1, alpha=0.7, label='MA20')


#
top.fill_between(moving_avg.index, moving_avg - 2 * moving_avg_mstd, moving_avg + 2 * moving_avg_mstd, color='white',
                 alpha=0.1)
bottom.bar(data.index, data['Volume'])

top.legend()
plt.show()
