# 利用python創造.csv檔，並將.txt檔案內的資料寫入
# 處理.csv檔畫圖

import csv
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

Analysis = './Data.txt'
csv_file = './Data.csv'

# # 讀取.txt檔
# open_txt = csv.reader(open(Analysis, 'r'), delimiter=',')
# # 創造.csv檔
# out_csv = csv.writer(open(csv_file, 'w'))
#
# out_csv.writerow(['筆數', '價格'])
# out_csv.writerows(open_txt)

# 想plot出來的東西是價格，用筆數當x軸
data = pd.read_csv(csv_file, parse_dates=True, index_col='筆數')
print(data.head())  # 顯示csv檔

price = data['價格']  # 顯示csv檔裡的價格
plt.plot(price)
plt.show()
