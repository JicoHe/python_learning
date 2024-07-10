favorite_languages = {
    'jen': ['python', 'javascript'],
    'leon': ['ruby', 'go', 'javascript'],
    'Jico': ['C', 'C++', 'Python']
}
for name, languages in favorite_languages.items():
    print(f"{name.title()}‘s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())
