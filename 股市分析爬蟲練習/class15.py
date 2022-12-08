# 處理.txt檔畫圖
from matplotlib import pyplot as plt
from matplotlib import style
import csv

# 背景
style.use('ggplot')

x = []
y = []

Analysis = './Data.txt'

# python內建功能-打開檔案數據資料（r=read）
with open(Analysis, 'r') as csvfile:
    # csv讀取檔案功能()，將,兩邊的'文字'分開
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))  # 文字改浮點數
        y.append(float(row[1]))

plt.plot(x, y, linewidth=1, label='Price')
plt.legend()
plt.show()
