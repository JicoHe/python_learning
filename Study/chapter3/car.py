# Organizing Lists
car = ['bmw', 'audi', 'toyota', 'suzuki']
car.sort()  # 字母排序
print(car)
car.sort(reverse=True)
print(car)
car.reverse()  # 可以实现同样的效果
print(car)
car.reverse()
print(len(car))

# 3-8 Seeing the World
spot = ['Beijing', 'jiangxi', 'home', 'singapore']
print(spot)
print(sorted(spot))
print(spot)  # Show that your list is still in its original order by printing it
print(sorted(spot, reverse=True))
print(spot)  # the same
spot.reverse()
print(spot)
spot.reverse()
print(spot)
spot.sort()
print(spot)
spot.sort(reverse=True)
print(spot)

# Dinner Guest
guest = ['Tony', 'Juliet', 'Robert']
print(f'I have invited {len(guest)} guest(s) to attend my dinner.')
