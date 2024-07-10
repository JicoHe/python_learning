# simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 使用变量调用字典的值
new_points = alien_0['points'] + 10  # 得到15的积分
print(new_points)

# 添加新的元素
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 新建一个空的字典
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 10
print(alien_1)

# 与if一起使用
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f'Original position: {alien_0["x_position"]}')

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'fast':
    x_increment = 5
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New position: {alien_0["x_position"]}')

del alien_0['speed']
print(alien_0)

