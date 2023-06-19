from random import choice

# Определение изначальных списков слов и подсказок, создание копий (для модификации в процессе игры)
words_list = ['ЛОПАТА', 'МУХОМОР', 'ДРОТИК', 'ПЕРЕПРАВА', 'СПИСОК', 'ПОЛДЕНЬ', 'ЗАБОР', 'КЛЮКВА', 'ГАДЮКА',
              'РУСЛО', 'ИЗМОРОЗЬ', 'КОРАБЛЬ']
help_list = ['ЗЕМЛЕРОЙНЫЙ ИНСТРУМЕНТ', 'НЕСЪЕДОБНЫЙ ГРИБ', 'МЕТАТЕЛЬНЫЙ СНАРЯД', 'ПРЕОДОЛЕНИЕ ВОДНОЙ ПРЕГРАДЫ',
             'ПЕРЕЧЕНЬ ЧЕГО - ЛИБО', 'СЕРЕДИНА ДНЯ', 'СООРУЖЕНИЕ, СЛУЖАЩЕЕ ДЛЯ ОГРАЖДЕНИЯ', 'КИСЛАЯ БОЛОТНАЯ ЯГОДА',
             'ЯДОВИТАЯ ЗМЕЯ', 'УГЛУБЛЕНИЕ В ПОЧВЕ, ПО КОТОРОМУ ТЕЧЕТ РЕКА', 'ПОХОЖИЙ НА ИНЕЙ СНЕЖНЫЙ ОСАДОК',
             'ТО ЖЕ, ЧТО И СУДНО']
words_list_copy = words_list[::]
help_list_copy = help_list[::]
guessed_words = []  # Пустой список угаданных слов
loose_game = False  # Переменная проигрыша (для сброса списков)


#  Функция выбора случайного слова
def get_word(_words_list_copy):
    _word = choice(_words_list_copy)
    return _word


# Функция сброса списков
def game_reset(_words_list, _words_list_copy, _guessed_words, _help_list, _help_list_copy):
    print('Обнуляем список слов...')
    _words_list_copy = _words_list[::]
    _help_list_copy = _help_list[::]
    _guessed_words = []
    return _words_list_copy, _guessed_words, _help_list_copy


# Функция выбора графического отображения оставшихся попыток
def display_lives(_tries):
    stages = ["\033[0;32m\U0001f90D \U0001f90D \U0001f90D \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f90D \U0001f90D \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f90D \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \033[0;0m"]
    return stages[_tries]


# Функция проверки введнного символа
def letter_input():
    while True:
        letter = input('Введите букву: ')
        letter = letter.upper()
        if letter not in "ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ" or len(letter) > 1 or letter == '':
            print('Это не буква !')
        else:
            break
    return letter


# Функция вывода сообщения о проигрыше
def game_over():
    print()
    print('\033[1;30;41mВы проиграли ! \033[0;0m')
    print()


# Функция вывода сообщения о выигрыше
def game_win():
    print()
    print('\033[1;30;42mВы выиграли ! \033[0;0m')
    print()


# Функция отображения статуса игры
def display_stats(_word_completion, _lives, _guessed_letters, _help_word, _guessed_words):
    quiz_word = ' '.join(_word_completion)  # Перевод загаданного слова из списка в строку
    _guessed_letters.sort()  # Сортировка угаданных букв
    u_letters = ' '.join(_guessed_letters)  # Перевод угаданных букв из списка в строку
    print()
    print('* ' * (len(_word_completion) + 2))
    print(f'* {quiz_word} *      ПОПЫТОК: {_lives}')
    print('* ' * (len(_word_completion) + 2))
    print(f'\033[0;36mПОДСКАЗКА: \033[0;0m{_help_word}')
    print(f'\033[0;33mИСПОЛЬЗОВАННЫЕ БУКВЫ:\033[0;0m {u_letters}')
    print('\033[0;33mУГАДАННЫЕ СЛОВА:\033[0;0m', *_guessed_words)


# Функция, осуществляющая игровую сессию
def play_game(_word, _words_list_copy, _guessed_words, _help_list_copy):
    word_completion = list('_' * len(_word))  # Создание списка для загаданного слова с '_' вместо неотгаданных букв
    help_index = _words_list_copy.index(_word)  # Привязка позиции списка подсказок к списку слов
    help_word = _help_list_copy[help_index]  # Получение позиции из списка подсказок
    guessed_letters = []
    tries = 6
    lives = display_lives(tries)
    print('Давайте играть в угадайку слов!')
    while True:  # Основной цикл игровой сессии
        display_stats(word_completion, lives, guessed_letters, help_word, _guessed_words)

        if '_' not in word_completion:  # Проверка, угаданно ли слово
            _guessed_words.append(_word)  # Добавление угаданного слова к списку угаданных слов
            _words_list_copy.remove(_word)  # Удаление угаданного слова из списка слов
            _help_list_copy.remove(help_word)  # Удаление соответствующей позиции из списка подсказок
            display_stats(word_completion, lives, guessed_letters, help_word, _guessed_words)
            game_win()
            return _words_list_copy, _guessed_words, _help_list_copy, loose_game

        ltr = letter_input()  # Ввод буквы

        if ltr in guessed_letters:  # Если введенная буква повторяется
            tries -= 1
            lives = display_lives(tries)
            print('\033[0;31mТакая буква уже была ! \033[0;0m')
        else:
            if ltr in _word:  # Если буква угадана
                guessed_letters.append(ltr)  # Добавление угаданной буквы к списку использованных букв
                for i in range(len(_word)):  # Подстановка угаданной буквы в загаданное слово
                    if _word[i] == ltr:
                        word_completion[i] = ltr
                print('\033[0;32mЕсть такая буква ! \033[0;0m')
            if ltr not in _word:  # Если буква не угаданна
                guessed_letters.append(ltr)
                tries -= 1
                lives = display_lives(tries)
                print('\033[0;31mНет такой буквы в этом слове ! \033[0;0m')

        if tries == 0:  # Если кончились попытки
            _loose_game = True
            display_stats(word_completion, lives, guessed_letters, help_word, _guessed_words)
            game_over()
            return _words_list_copy, _guessed_words, _help_list_copy, _loose_game



# Основной цикл игры
while True:
    if not words_list_copy:  # Сброс, если закончились слова в списке
        print('\033[0;32mПоздравляем ! Вы угадали все слова !\033[0;0m')
        words_list_copy, guessed_words, help_list_copy = game_reset(words_list, words_list_copy, guessed_words,
                                                                    help_list,
                                                                    help_list_copy)
    elif loose_game == True:  # Сброс, если игрок проиграл
        words_list_copy, guessed_words, help_list_copy = game_reset(words_list, words_list_copy, guessed_words,
                                                                    help_list,
                                                                    help_list_copy)

    word = get_word(words_list_copy)
    word_list_copy, guessed_words, help_list_copy, loose_game = play_game(word, words_list_copy, guessed_words,
                                                                          help_list_copy)  # Запуск игровой сессии
    check = input('Еще разок ? (Н/н для выхода): ')  # Проверка окончания игры
    if check.upper() != 'Н':
        continue
    break

print('Спасибо за игру !')