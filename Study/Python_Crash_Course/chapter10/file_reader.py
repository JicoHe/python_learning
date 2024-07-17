with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pl_string = ''
for line in lines:
    pl_string += line.strip()

birthday = input('What is your birthday? ')
if birthday in pl_string:
    print('Your birthday appears in pi_digits.txt.')
else:
    print('Your birthday does not appear in pi_digits.txt.')
print(pl_string)
print(len(pl_string))