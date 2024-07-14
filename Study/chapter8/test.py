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

# 8-6
def city_country(city, country):
    str = f"{city}, {country}"
    return str
print(city_country("Reykjavik", "Iceland"))

# 8-7
def make_album(name, title, songs=None):
    album = {'name': name, 'title': title}
    if songs:
        album['songs_num'] = songs
    return album
album1 = make_album("Novo Aram", "Weather")
album2 = make_album("Joji", "Ew")
album3 = make_album('linkinpark', 'one more night',11)
print(album1)
print(album2)
print(album3)

# 8-8
flag = True
while flag:
    name = input("Enter artist's name: ")
    if name == 'q':
        flag = False
        break
    title = input("Enter your favorite album's title: ")
    if title == 'q':
        flag = False
        break
    your_favorite_album = make_album(name, title)
    print(f"your favorite album  is {your_favorite_album}")
