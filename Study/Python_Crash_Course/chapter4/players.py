players = ['charles', 'martina', 'michael', 'florence', 'elizabeth']
print(players[0:3])
print(players[0:])  # 从开始切
print(players[:3])  # 从开始切切到第3个
print(players[-3:])

# 遍历中使用切片
for player in players[:3]:
    print(player.title())
