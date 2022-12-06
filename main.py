# pythonProject4

# БОТ, ДЛЯ TELEGRAM-КАНАЛА С АНЕКДОТАМИ
# Параллельное выполнение двух задач
# Задача 1: по нажатию кнопки бот присылает случайный анекдот в личку
# Задача 2: бот получает список анекдотов из файла и случайные шутки через случайные периоды времени постит в канал.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с анекдотами должен лежать в папке data рядом со скриптом бота.

from multiprocessing import Process
from telebot import types
import telebot
import random
import time
from config import token, channel

# Загружаем список анекдотов из файла
# если текстовый файл находится не в каталоге программы, то пишем полный путь к нему
# "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
f = open('fun.txt', 'r', encoding='UTF-8')
funs = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel


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
    # Запускаем бота, присылающего анекдоты в личку - задача 1
    bot.polling(none_stop=True, interval=0)


def second_process():
    # запускаем бота, посылающего анекдоты в канал - задача 2
    fl_go = 'go'
    while fl_go == 'go':
        # таймер работы бота
        time.sleep(random.randint(60, 3600))
        fl = 'start'
        if fl == 'start':
            bot.send_message(CHANNEL_NAME, random.choice(funs))
            fl = 'stop'


# запускаем два процесса параллельно
if __name__ == '__main__':
    p1 = Process(target=first_process, daemon=True)
    p2 = Process(target=second_process, daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
