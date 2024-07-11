name = input('What is your name?')
print('\nHello, ', name + '!')

# 进一步拆分两句话,显示多行
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat's your name?"

name = input(prompt)
print('Hello,', name + '!')
