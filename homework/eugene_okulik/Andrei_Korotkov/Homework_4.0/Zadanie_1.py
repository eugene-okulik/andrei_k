
YELLOW = '\033[93m'
print('=' * 36)
print('Задание: ', 1, sep='№')
print('=' * 36)

slova = ('Etiam tincidunt neque erat, quis molestie enim imperdiet'
         ' vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

slova = slova.split()
fin_words = []
for word in slova:
    if word[-1] in ',.':
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'

    fin_words.append(new_word)

print(' '.join(fin_words))
print('=' * 36)
