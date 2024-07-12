# 使用函数处理数据
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    return full_name.title()


musician = get_formatted_name('Smith', 'Doe')
print(musician)

while True:
    print("\nPlease enter your name.")
    print("(enter 'q' to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name}!")
