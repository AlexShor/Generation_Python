alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input().split(" ")
new_text = []

for word in text:
    step = 0 
    for char in word: 
        if char.isalpha(): step += 1
    
    new_word = ''
    for i in word:
        if i.isalpha():
            char = alph[(alph.index(i.upper()) + step) % len(alph)]
            new_word += char if i.isupper() else char.lower()
        else:
            new_word += i
    new_text.append(new_word)

print(*new_text)