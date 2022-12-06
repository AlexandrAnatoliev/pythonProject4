# pythonProject4

# БОТ, ДЛЯ TELEGRAM-КАНАЛА С АНЕКДОТАМИ
# Параллельное выполнение двух задач
# По нажатию кнопки бот присылает случайный анекдот в личку

from multiprocessing import Process
import time
import telebot
import random
from telebot import types
from config import token

# Загружаем список анекдотов из файла
# если текстовый файл находится не в каталоге программы, то пишем полный путь к нему
# "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
f = open('fun.txt', 'r', encoding='UTF-8')
funs = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot(token)


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем кнопку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Анекдот")
    markup.add(item1)
    bot.send_message(m.chat.id,
                     'Нажми: \nАнекдот для получения интересного анекдота ',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный анекдот
    if message.text.strip() == 'Анекдот':
        answer = random.choice(funs)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)


def first_process():
    # Запускаем бота присылающего анекдоты в личку
    bot.polling(none_stop=True, interval=0)


def second_process(word):
    fl = 'start'
    while fl == 'start':
        print('Запущен', word)
        time.sleep(3)

# запускаем два процесса параллельно
if __name__ == '__main__':
    p1 = Process(target=first_process, daemon=True)
    p2 = Process(target=second_process, args=('второй процесс',), daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
