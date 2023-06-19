import random

words = "Ай Вылущить Гуляка Закодировать Запихать Начетистый Обмозговать Официант Ссутулиться Успокоиться Нормализоваться Полова Прелюд Пригон Свериться Смущаться Сопоставить Терпеливый Хунта Чих Болото Вахтер Выбелить Казахи Прибить Сушняк Хвощ Чванный Электорат Эскиз Ассистировать Ассоциировать Батенька Батрачить Возненавидеть Вроде Гарант Двукратный Отмалчиваться Прок Автоцистерна Броневик Донесение Затеплить Нефрит Просветиться Разогнать Репа Секс-бомба Четырнадцать Абонент Алхимия Болтать Весть Перематывать Помяться Попотчевать Походя Скрепить Эквадорский".upper()
word_list = list(words.split())


def display_hangman(tries):
    stages = [
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(*word_completion)
    while tries >= 0:
        text = ''.upper()
        while text == '' or text.isdigit():
            text = input('Слово или буква:').upper()
            if text in guessed_letters:
                print(display_hangman(tries))
                print('Эта буква уже называлась!')
                print(*word_completion)
                text = ''
        if len(text) > 1:
            if text == word:
                print(display_hangman(tries))
                print("Слово отгадано!")
                print(*word_completion)
                print(*list(text))
                break
            else:
                if text in guessed_words:
                    print(display_hangman(tries))
                    print('Это слово уже называлось, оно не правильное!')
                    print(*word_completion)
                else:
                    tries -= 1
                    print(display_hangman(tries))
                    print('Не верное слово!')
                    print(*word_completion)
                    guessed_words.append(text)
        else:
            if text in word:
                print(display_hangman(tries))
                print('Буква отгадана')
                for i in range(len(word)):
                    if word[i] == text: word_completion[i] = text
                guessed_letters.append(text)
                if '_' not in word_completion:
                    print("Слово отгадано!")
                    break
                print(*word_completion)
            else:
                tries -= 1
                print(display_hangman(tries))
                print('Такой буквы нет!')
                guessed_letters.append(text)
                print(*word_completion)
        if tries == 0:
            print(display_hangman(tries))
            print('Вы проиграли!')
            print('Это было слово:')
            print(*word)
            break
    print("Игра окончена.")


again = 'д'

while again.lower() == 'д':
    play(random.choice(word_list))
    again = input('Играем еще раз? (д = да, н = нет):')

