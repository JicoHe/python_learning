# 使用while将列表元素进行移动
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # 对其进行验证后变成Curren
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
confirmed_users.sort()
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())
