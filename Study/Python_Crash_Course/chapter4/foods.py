# copy a list
my_foods = ['apple', 'banana', 'cherry']
friend_foods = my_foods[:]
my_foods.append('orange')
friend_foods.append('mango')
print(my_foods)
print(friend_foods)

# 4-10
for food in my_foods[:3]:
    print(food.title())
print('\n')
for food in my_foods[1:4]:
    print(food.title())
print('\n')
for food in my_foods[-3:]:
    print(food.title())
