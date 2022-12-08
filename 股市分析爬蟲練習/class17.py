import csv
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

# 背景
style.use('ggplot')

Analysis = './AAPL.csv'

data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')  # Date當作水平顯示(x軸)
price = data['Close']
price.head()

# pandas的moving average功能
# 畫出MA5
moving_avg5 = price.rolling(5).mean()
# 畫出MA20
moving_avg20 = price.rolling(20).mean()
# 畫出MA20標準差
moving_avg20_mstd = price.rolling(20).std()

plt.plot(price, color='b')
plt.plot(moving_avg5, color='cornflowerblue', linewidth=1, label='MA5')
plt.plot(moving_avg20, color='orange', linewidth=1, label='MA20')
# 'moving_avg20.index': 沿著moving_avg20的日期(x軸)
# alpha：透明度
plt.fill_between(moving_avg20.index, moving_avg20-2*moving_avg20_mstd, moving_avg20+2*moving_avg20_mstd, color='b', alpha=0.2)

plt.legend()
plt.show()
