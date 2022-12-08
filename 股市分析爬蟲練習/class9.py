def first_function():
    print('this is my first function')


first_function()


def calculate(cost, price, order):
    result = (price - cost) * order
    print('淨利：', result)
    return result


answer = calculate(1500, 2000, 10)
print(answer)
