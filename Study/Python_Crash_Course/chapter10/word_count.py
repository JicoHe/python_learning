def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")


filename = input('Enter a file name: ')
count_words(filename)