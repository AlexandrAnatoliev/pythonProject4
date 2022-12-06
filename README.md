# pythonProject4

[Ru] БОТ, ДЛЯ TELEGRAM-КАНАЛА С АНЕКДОТАМИ. 
## Описание
Параллельное выполнение двух задач. Задача 1: по нажатию кнопки бот присылает случайный анекдот в личку. Задача 2: бот получает список анекдотов из файла и случайные шутки через случайные периоды времени постит в канал.

## Требования

* Установить внешние зависимости
* $ pip install -r requirements.txt
* Создать свой канал в Telegram, добавить в подписчики канала нашего бота и назначить его администратором канала с
  правом публиковать сообщения.
* Создать файл с анекдотами fun.txt и размесить в папке со скриптом бота. ВАЖНО! Каждый анекдот должен начинаться с новой строки
* создать файл config.py, в котором будут храниться токен для доступа к боту и адрес канала в виде
```python
token = "1234567890:ASDFGHH..."
channel = '@topjokes...'
```

## Где взять токен?
* https://xakep.ru/2021/11/28/python-telegram-bots/

## Подключаем модули
```python
from multiprocessing import Process
from telebot import types
import telebot
import random
import time
from config import token, channel
```

## Примеры использования

#### # Загружаем список анекдотов из файла
```python
f = open('fun.txt', 'r', encoding='UTF-8')
funs = f.read().split('\n')
f.close()
```
#### Если текстовый файл находится не в каталоге программы, то пишем полный путь к нему: "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)

#### Добавляем кнопку
```python
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
```
#### запускаем два процесса параллельно
```python
if __name__ == '__main__':
    p1 = Process(target=first_process, daemon=True)
    p2 = Process(target=second_process, daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```
#### Первый процесс - бот посылает анекдот пользователю в личку
```python
def first_process():
    # Запускаем бота, присылающего анекдоты в личку - задача 1
    bot.polling(none_stop=True, interval=0)
```

#### Отрабатываем сообщение от пользователя - нажатие кнопки "Анекдот"
```python
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный анекдот
    if message.text.strip() == 'Анекдот':
        answer = random.choice(funs)
        # Отсылаем юзеру сообщение в его чат
        bot.send_message(message.chat.id, answer)
```
#### Второй процесс - бот посылает случайный анекдот в канал через случайный период времени
```python
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
```