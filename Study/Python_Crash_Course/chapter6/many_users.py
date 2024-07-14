# 字典中的字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}
for username, user_info in users.items():
    print(f'username: {username}')
    full_name = user_info.get('first') + ' ' + user_info.get('last')
    location = user_info.get('location')

    print(f'full name: {full_name.title()}')
    print(f'location: {location.title()}')