# 处理不知道函数接受多少个argument的情况
def make_pizza(*toppings, size=None):
    if size:
        print(f"\nMaking a {size}-inch pizza we are about to make.")
    else:
        print("Making a pizza we are about to make.")
    for topping in toppings:
        print(f"- {topping}")


# 建立了一个元组topping，可以接受多个变量
make_pizza('pepperoni', size=16)
make_pizza('green peppers', 'mushrooms', 'extra cheese')
