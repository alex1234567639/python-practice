'''
List 的用法
'''

shop = ['milk', 'orange', 'juice', 'water', 'beef', 'tea']
print(shop[0])

shop[0] = 'soda'
print(shop[0])
print(shop[-1])  # 陣列倒數

count = [2, 4, 6, 12, 7, 9]
# print(sum(count))
# print(max(count))
# print(min(count))
# print(sorted(count))

total = shop + ['cheese']
print(total)

del shop[0]
print(shop)

shop.append('append')
print(shop)

shop.clear()
print(shop)
