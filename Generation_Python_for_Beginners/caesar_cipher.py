alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
direction = input('Choose a direction: \n(+) - Encryption \n(-) - Decryption:\n ')
lang = int(input('Choose the language of the alphabet: \n0 - Russian \n1 - English: \n'))
step = int(direction + input('Enter number, shift step (with right shift): '))
text = input('Enter text to process:\n')


for i in text:
    if i.isalpha():
        char = alph[lang][(alph[lang].index(i.upper()) + step) % len(alph[lang])]
        print(char if i.isupper() else char.lower(), end='')
    else:
        print(i, end='')
