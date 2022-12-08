from matplotlib import pyplot as plt
from matplotlib import style

# 背景
style.use('ggplot')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [18, 21, 4, 3, 45, 17, 16, 5, 6]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = [16, 19, 5, 4, 44, 18, 17, 6, 8]

# 分別顯示兩張圖
plt.subplot(211)
plt.plot(x, y, linewidth=1, color='b', label='True Value')
plt.plot(x2, y2, linewidth=1, marker='o', color='r', linestyle='-', label='Prediction')
plt.legend()

plt.subplot(212)
plt.bar(x, y, align='center', label='True Value')
plt.bar(x2, y2, align='center', label='Prediction')
plt.legend()

plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.show()
