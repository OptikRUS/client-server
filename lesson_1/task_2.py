"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов(не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = ['class', 'function', 'method']

for i in words:
    bytes_string = bytes(i, 'ascii')
    print(bytes_string, type(bytes_string), len(bytes_string))
