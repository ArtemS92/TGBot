import telebot

from telebot import types
import emoji

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!')
    bot.send_message(message.chat.id,
                     'Для перехода в Главное меню нажмите:\n/menu\nДля вызова команды помощи нажмите:\n/help')


@bot.message_handler(commands=['menu'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(emoji.emojize('💈💇Услуги'))
    item2 = types.KeyboardButton(emoji.emojize('📷 Фото работ'))
    item3 = types.KeyboardButton(emoji.emojize('💵 Цены'))
    item4 = types.KeyboardButton(emoji.emojize('🏢 Адрес'))
    item5 = types.KeyboardButton(emoji.emojize('📔 Запись'))
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Выберите, что бы вы хотели узнать:', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                     '/start - команда запуска бота\n/menu - команда выхода в Главное меню\n/help - команда помощи\n')


@bot.message_handler(content_types=['text'])
def button_message(message):
    if message.text == '💵 Цены':
        img = open('venv/price.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text == emoji.emojize('📷 Фото работ'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Ботокс')
        item2 = types.KeyboardButton('Кератин')
        item3 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выберите примеры', reply_markup=markup)
    elif message.text == 'Ботокс':
        img1 = open('venv/2.jpg', 'rb')
        bot.send_photo(message.chat.id, img1)
    elif message.text == 'Кератин':
        img1 = open('venv/keratin.jpg', 'rb')
        bot.send_photo(message.chat.id, img1)
    elif message.text == '💈💇Услуги':
        bot.send_message(message.chat.id, 'Стрижки мужские и женские\nОкрашивание\nКератин\nБотокс')
    elif message.text == '🏢 Адрес':
        bot.send_message(message.chat.id, 'Московская область\nг. Истра\nул.9 Гвардейской дивизии\nд.42')
    elif message.text == '📔 Запись':
        bot.send_message(message.chat.id, 'Для записи позвоните по телефону:\n+79999999999')
    elif message.text == 'Назад':
        return main_menu(message)


bot.polling()
