# 5-1 conditional tests
# pass

# 5-3 Alien Colors
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('You just earned 5 points for shooting the alien.')
elif 'yellow' in alien_color:
    print("You just earned 10 points")
elif 'red' in alien_color:
    print("You just earned 15 points")

# 5-6 Stages of Life
age = 11

if age < 2:
    person = 'baby'
elif age < 4:
    person = 'toddler'
elif age < 13:
    person = 'kid'
elif age < 20:
    person = 'teenager'
elif age < 65:
    person = 'adult'
elif age >= 65:
    person = 'elder'
print(f'the person is {person}')

# 5-8
username = ['admin', 'bob', 'tony', 'david', 'joji']
for name in username:
    if name == 'admin':
        print('admin, welcome')
    else:
        print(f'{name} is not admin')
for i in range(len(username)):
    if username:
        username.remove(username[0])
print(len(username))

# 5-10
current_users = ['admin', 'bob', 'tony', 'david', 'joji']
cap_users = current_users[:]
# 让列表所有的名字大写
for i in range(len(cap_users)):
    if cap_users[i]:
        cap_users[i] = cap_users[i].upper()
new_users = ['DAVID', 'joji', 'don']  # 新用户名字
# 确认是否可用
for name in new_users:
    if name not in current_users and name not in cap_users:
        print(f'you can use {name} as your username ')
    else:
        print(f'{name} has been used')
