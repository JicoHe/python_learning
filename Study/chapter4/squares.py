squares = []
# 将前10的次方数加到square数列当中
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares_2 = [value ** 2 for value in range(1, 11)]  # 列表推导式
print(squares_2)

# 4-3 counting to twenty
for value in range(1, 21):
    print(value)

# 4-4 one million
million = []
for value in range(1, 1000001):
    million.append(value)
print(million)

# 4-5 summing a million
print(min(million))
print(max(million))
print(sum(million))

# 4-6 odd numbers
odd_numbers = [value for value in range(1, 20, 2)]
print(odd_numbers)

# 4-7 threes
three_numbers = [value for value in range(3, 31, 3)]
print(three_numbers)

# 4-8 - 4-9 cube
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
