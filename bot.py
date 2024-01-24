import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from function import load_user_data, save_user_data
from info import list_form, list_character
from config import token

bot = telebot.TeleBot(token=token)

user_data = load_user_data()


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    global user_data
    if str(message.chat.id) not in user_data.keys():
        user_data[str(message.chat.id)] = {'name': message.chat.first_name,
                                           'answers': ''}
        save_user_data(user_data)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if len(user_data[str(message.chat.id)]['answers']) > 0:
        btn1 = KeyboardButton('Продолжить тест')
    else:
        btn1 = KeyboardButton('Начать тест')
    btn2 = KeyboardButton('Перезапуск теста')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}! '
                                      f'Я бот-анкета "Какой у тебя тип личности"\n'
                                      f'Чтобы начать, продолжить или перезапустить тест нажимай на кнопки снизу',
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    bot.send_message(message.chat.id, '/start - бот приветствует тебя и покажет две кнопки снизу\n'
                                      '/help - показывает доступные команды и как пользоваться ботом\n'
                                      '\nКак пользоваться ботом-анкетой?\n'
                                      'Ботом пользоваться легко, просто используй кнопки снизу,'
                                      'которые появятся после команды /start')


@bot.message_handler(content_types=['text'])
def func(message: Message):
    global user_data
    if message.text == 'Перезапуск теста':
        user_data[str(message.chat.id)]['answers'] = ''
        save_user_data(user_data)

    if message.text == list_form[0]['answers'][1]:
        user_data[str(message.chat.id)]['answers'] += 'E'
        save_user_data(user_data)
    elif message.text == list_form[0]['answers'][2]:
        user_data[str(message.chat.id)]['answers'] += 'I'
        save_user_data(user_data)
    elif message.text == list_form[1]['answers'][1]:
        user_data[str(message.chat.id)]['answers'] += 'S'
        save_user_data(user_data)
    elif message.text == list_form[1]['answers'][2]:
        user_data[str(message.chat.id)]['answers'] += 'N'
        save_user_data(user_data)
    elif message.text == list_form[2]['answers'][1]:
        user_data[str(message.chat.id)]['answers'] += 'T'
        save_user_data(user_data)
    elif message.text == list_form[2]['answers'][2]:
        user_data[str(message.chat.id)]['answers'] += 'F'
        save_user_data(user_data)
    elif message.text == list_form[3]['answers'][1]:
        user_data[str(message.chat.id)]['answers'] += 'J'
        save_user_data(user_data)
    elif message.text == list_form[3]['answers'][2]:
        user_data[str(message.chat.id)]['answers'] += 'P'
        save_user_data(user_data)

    if len(user_data[str(message.chat.id)]['answers']) == 0:
        photo = open('capture/question_1.jpg', 'rb')
        markup = ReplyKeyboardMarkup()
        btn1 = KeyboardButton(list_form[0]['answers'][1])
        btn2 = KeyboardButton(list_form[0]['answers'][2])
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, photo, caption=f'{list_form[0]["question"]}', reply_markup=markup)
        photo.close()
    elif len(user_data[str(message.chat.id)]['answers']) == 1:
        photo = open('capture/question_2.jpg', 'rb')
        markup = ReplyKeyboardMarkup()
        btn1 = KeyboardButton(list_form[1]['answers'][1])
        btn2 = KeyboardButton(list_form[1]['answers'][2])
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, photo, caption=f'{list_form[1]["question"]}', reply_markup=markup)
        photo.close()
    elif len(user_data[str(message.chat.id)]['answers']) == 2:
        photo = open('capture/question_3.jpg', 'rb')
        markup = ReplyKeyboardMarkup()
        btn1 = KeyboardButton(list_form[2]['answers'][1])
        btn2 = KeyboardButton(list_form[2]['answers'][2])
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, photo, caption=f'{list_form[2]["question"]}', reply_markup=markup)
        photo.close()
    elif len(user_data[str(message.chat.id)]['answers']) == 3:
        photo = open('capture/question_4.jpg', 'rb')
        markup = ReplyKeyboardMarkup()
        btn1 = KeyboardButton(list_form[3]['answers'][1])
        btn2 = KeyboardButton(list_form[3]['answers'][2])
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, photo, caption=f'{list_form[3]["question"]}', reply_markup=markup)
        photo.close()
    elif len(user_data[str(message.chat.id)]['answers']) == 4:
        for key, value in list_character.items():
            if user_data[str(message.chat.id)]['answers'] in key:
                photo = open(f'capture/{key}.png', 'rb')
                markup = ReplyKeyboardMarkup(resize_keyboard=True)
                btn = KeyboardButton('Перезапуск теста')
                markup.add(btn)
                bot.send_photo(message.chat.id, photo, caption=value, reply_markup=markup)
                photo.close()
                bot.send_message(message.chat.id, 'Спасибо за прохождение анкеты.\n'
                                                  'Можешь попробовать ещё раз')

    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn = KeyboardButton('Перезапуск теста')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Вышла ошибка, попробуй занова', reply_markup=markup)


bot.infinity_polling()
