requested_toppings = ['mushroom']
if requested_toppings != 'anchovies':
    print('Sorry, we don\'t have anchovies')

requested_toppings.append('extra cheese')
if 'mushroom' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

requested_toppings.append('green peppers')
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we don\'t have green peppers.')
    else:
        print('Adding ' + requested_topping)
print("\nFinished making your pizza!")

# 判断是否不是空的列表
if requested_toppings:
    for requested_topping in requested_toppings:
        print(requested_topping)
else:
    print('Sorry, we don\'t have any pizza.')

# 列表与列表的比较
available_toppings = ['mushroom', 'pepperoni', 'extra cheese', 'green peppers', 'Olives', 'Pineapples']
requested_toppings = ['mushroom', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(requested_topping)
    else:
        print('Sorry, we don\'t have ' + requested_topping)
print("\nFinished making your pizza!")
