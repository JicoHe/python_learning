# 7-1
rental_car = input("What kind of rental car you would like:")
print(f"Ler me see if I can find you a {rental_car}")

# 7-2
people_num = int(input("How many people are in your dinner group:"))
if people_num > 8:
    print("You will have to wait for a table")
else:
    print("The table is ready")
# 7-3
num_guess = int(input("give me a number and show you if it is a multiples of 10:"))
if num_guess % 10 == 0:
    print("Yes")
else:
    print("No")

# 7-4 输入quit的用法
pizza_topping = "What is the pizza topping you would like:"
flag = True
while flag:
    topping = input(pizza_topping)
    if topping == 'quit':
        flag = False
    else:
        print(f"I'll add {topping} to your pizza")

# 7-8
sandwich_orders = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

# 7-9
sandwich_orders = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for value in range(3):
    sandwich_orders.append('pastrami')
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)