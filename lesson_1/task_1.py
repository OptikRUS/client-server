"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции

ВНИМАНИЕ!!: сдача задания
1) создать папку Lesson_1_Ivanov
2) в папку положить файлы task_1 - task_6 (а также txt-файл для последнего)
3) заархивировать папку! и сдать архив

Все другие варианты сдачи приму только один раз, потом буду ставить НЕ СДАНО
"""

words = ['разработка', 'сокет', 'декоратор']
u_words = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
           '\u0441\u043e\u043a\u0435\u0442',
           '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for word in words:
    print(word, type(word))

for u_word in u_words:
    print(u_word, type(u_word))
