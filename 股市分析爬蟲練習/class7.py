# if else

number = 11
if number == 10:
    print('等於10')
else:
    print('不等於10')

saving = int(input('請輸入你的數字：'))
if 10000 < saving <= 50000:
    print('零股投資')
elif 50000 <= saving <= 100000:
    print('可考慮整股投資')
elif saving >= 100000:
    print('整股投資')
else:
    print('對不起，請確認您的存款')
