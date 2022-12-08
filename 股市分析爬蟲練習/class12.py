from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [18, 21, 4, 4, 6, 31, 23, 18, 6]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = [14, 19, 6, 8, 21, 4, 5, 16, 27]

plt.plot(x, y, linewidth=1)
plt.plot(x2, y2, linewidth=1)
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.show()
