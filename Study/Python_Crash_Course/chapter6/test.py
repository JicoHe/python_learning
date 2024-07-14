# 6-1 person
JicoHe = {'first_name': 'Jico', 'last_name': 'He', 'age': 19, 'city': 'Jianmeng'}
print(JicoHe['first_name'])

# 6-2 favorite numbers
fav_nums = {
    'JicoHe': 6,
    'yeahRed': 7,
    'me': 4
}
print(f"Jico's favorite number is {fav_nums['JicoHe']}")

# 6-5 rivers
rivers = {
    'nile': 'egypt',
    'China': 'yangzi river',
 }
for country , river in rivers.items():
    print(f"The {country} runs through {river}")
for country in rivers.keys():
    print(country)
for river in rivers.values():
    print(river)

# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people = ['sarah', 'phil', 'JicoHe']
for person in people:
    if person in favorite_languages.keys():
        print(f"{person}, you have already taken the poll")
    else:
        print(f"{person}, you haven't already taken the poll")
