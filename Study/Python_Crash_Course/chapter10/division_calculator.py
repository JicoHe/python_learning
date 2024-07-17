# 处理会出现错误的情况
print("give me two numbers, and I'll divide them")
print("(Enter 'q' to quit)")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: \n")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print("The result is {}".format(answer))

