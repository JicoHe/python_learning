# 10-3
with open('guest.txt','a') as f1:
    while True:
        guest = input("Enter your name:")
        if guest == 'q':
            break
        else:
            f1.write(guest)

# 10-4
with open('guest_book.txt','a') as f2:
    while True:
        greeting = input()
        if greeting == 'q':
            break
        else:
            print(f"Welcome to my world!{greeting}")
            f2.write(greeting + '\n')
