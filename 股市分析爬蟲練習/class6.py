today = {'早餐': 45,
         '坐捷運': 30,
         '工作': 25,
         '中餐': 100
         }
print(today['早餐'])

today['早餐'] = 80
print(today['早餐'])

del today['中餐']
print(today)
