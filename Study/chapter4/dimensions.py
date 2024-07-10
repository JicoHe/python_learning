dimensions = (200, 50)  # 不可改变的列表叫元组
print(dimensions[0])
print(dimensions[1])
print('\nModified dimensions')
dimensions = (400, 200)
for dimension in dimensions:
    print(dimension)

# 4-13
buffer_foods = ('hamburger', 'chips', 'cola', 'chicken', 'KFC')
for food in buffer_foods:
    print(food)
buffer_foods = ('hamburger', 'chips', 'cola', 'A', 'B')
print('\nWe update our menus')
for food in buffer_foods:
    print(food)
