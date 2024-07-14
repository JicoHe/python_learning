# 花括号多行
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")

point_value = favorite_languages.get('points', 'No point value assigned')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
for name in favorite_languages.keys():
    print(name.title())

# 遍历对应的好伙伴才打印
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    #  如果时好朋友则加上值
    if name in friends:
        print(f"{name.title()}'s favorite language is {favorite_languages[name].title()}")
# 按顺序对keys进行遍历
for name in sorted(favorite_languages.keys()):
    print(name.title())

# 单独遍历value，用values()
for language in favorite_languages.values():
    print(language.title())
print("\n")
# set()消除重复的内容
for language in set(favorite_languages.values()):
    print(language.title())
