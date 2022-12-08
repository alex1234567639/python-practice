cake = int(input('蛋糕數量：'))
people = int(input('人數：'))

if cake < people:
    print('蛋糕不夠', people, '人分到每人至少1塊')
else:
    print('有', cake, '塊蛋糕可以分給', people, '人')
