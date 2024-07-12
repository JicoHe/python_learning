# 8-1
def display_message():
    print("I will learn function in this chapter")


display_message()


# 8-2
def favorite_books(title):
    print(f"One of my favorite books is {title}")


favorite_books("Python Crash Course")

# 8-3
def make_shirt(size='large', message='I love Python'):
    print(f"Your size of T-shirt is {size}")
    print(f"The message on the T-shirt are {message}")


make_shirt('small', "I like Python")

# 8-4 见上
# 8-5
def describe_city(name='reykjavik', country='Iceland'):
    print(f"{name} is in {country}")
