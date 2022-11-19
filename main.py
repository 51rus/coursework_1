import random


def morse_encode(word):
    """
    Переводит слова с английского в азбуку Морзе
    """
    morse_word = []
    for i in word:
        morse_word += morse_code[i]
        translation_str = "".join(morse_word)
    return translation_str


def get_word():
    """
    Получает случайное слово из списка слов
    """
    random_word = random.choice(translate_words)
    return random_word


def print_statistics(answers):
    """
    Выводит статистику
    """
    count_answers = 0
    for i in answers:
        if i:
            count_answers += 1
    all_lessons = print(f"Всего задачек: {len(answers)}")
    true_lessons = print(f"Отвечено верно: {count_answers}")
    false_lessons = print(f"Отвечено неверно: {len(answers) - count_answers}")
    return all_lessons, true_lessons, false_lessons


# Список английских слов и фраз, которые будете расшифровывать
translate_words = ["code", "bit", "list", "soul", "next"]

# Словарь Морзе
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

# Список, который хранит ответы типа True, False
answers = []

# Приветствие и старт программы
print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
print("Нажмите Enter и начнем")
start = input()

# Счетчик задач
num = 0

# Цикл задавания вопросов
for i in range(0, 5):
    new_word = get_word()
    new_word_morse = morse_encode(new_word)
    num += 1

    print(f"Слово {num} - {new_word_morse}")
    answers_user = input()
    if answers_user == new_word:
        print(f"Верно, {new_word}!")
        answers.append(True)
    else:
        print(f"Неверно, {new_word}!")
        answers.append(False)

print_statistics(answers)
