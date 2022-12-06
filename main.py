# pythonProject4
import time
# Параллельное выполнение двух задач
from multiprocessing import Process


def first_process(word):
    fl = 'start'
    while fl == 'start':
        print('Запущен', word)
        time.sleep(2)


def second_process(word):
    fl = 'start'
    while fl == 'start':
        print('Запущен', word)
        time.sleep(3)


if __name__ == '__main__':
    p1 = Process(target=first_process, args=('первый процесс',), daemon=True)
    p2 = Process(target=second_process, args=('второй процесс',), daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
# second_process('основной процесс')
