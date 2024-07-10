magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(magician.title())
    print(f'{magician.title()}, Welcome to Magicians LOOP!\n')

# 4-1 pizzas
pizzas_food = ['chicken', 'potato', 'beef']
for food in pizzas_food:
    print(f'My favorite pizza is {food} pizza')
print('I really love pizza!')

friend_foods = pizzas_food[:]
pizzas_food.append('pig')
friend_foods.append('egg')
print(pizzas_food)
print(friend_foods)