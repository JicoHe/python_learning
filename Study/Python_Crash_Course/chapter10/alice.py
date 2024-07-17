filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has {num_words} words.")    