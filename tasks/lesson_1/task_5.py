"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
from subprocess import Popen, PIPE
from chardet import detect


YANDEX_ARGS = ['ping', 'yandex.ru']
YOUTUBE_ARGS = ['ping', 'youtube.com']

YANDEX_PING = Popen(YANDEX_ARGS, stdout=PIPE)
YOUTUBE_PING = Popen(YOUTUBE_ARGS, stdout=PIPE)

for line in YOUTUBE_PING.stdout:
    result = detect(line)
    print(line.decode(result['encoding']))
