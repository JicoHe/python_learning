# 传递列表给函数
def greet_users(names):
    for name in names:
        msg = f"Hello {name}"
        print(msg)
usernames = ['John', 'Doe', 'Smith']
greet_users(usernames)