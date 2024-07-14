motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.append('ducati')  # 用append方法将元素置于末端
print(motocycles)

motocycles.insert(0, 'abc')
print(motocycles)

del motocycles[0]
print(motocycles)

poped_motocycles = motocycles.pop(0)
print(motocycles)
print(poped_motocycles)

# 3-4 - 3-7
guest = ['Tony', 'Juliet', 'Robert']
print(guest)
absence = [guest.pop()]
print(absence)
print(guest)

guest.insert(0, 'jenny')
guest.insert(2, 'bob')
guest.append('tom')
print(guest)
print(f"{guest[0].title()}, Welcome to my dinner party")
print(f"{guest.pop()}, i'm gonna let you go!")
print(f"{guest.pop()}, i'm gonna let you go!")
print(f"{guest.pop()}, i'm gonna let you go!") # 将最后一个值拿出列表但可以使用
print(f"{guest[0]}, you stay!")
print(f"{guest[1]}, you stay!")
del guest[0]
del guest[1]
print(guest)
