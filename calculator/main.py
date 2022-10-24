import telebot
from bot_token import bot
from telebot import types
from logger import log_expression as log_ex
from logger import log_ansver as log_ansv

expression_list = []

@bot.message_handler(commands=['start'])
def go_menu(message):
    username = message.from_user.username
    bot.send_message(message.chat.id, f"Приветствую, {username}! Я могу выполнить +-/* с рациональными(включая действия со скобками) или комплексными числами(вводим без скобок, мнимая часть с j). Для продолжения напишите /menu")

@bot.message_handler(commands=['menu'])
def go_menu(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("История вычислений")
    item2=types.KeyboardButton("Рассчитать выражение")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Выберите режим работы', reply_markup=markup)

@bot.message_handler(commands=['answer'])
def answer(message):
    data = expression_list
    print(data)
    log_ex("".join(data))
    if select_model(data) == 'rational':
        from model_rational_numbers import calculator
    else:
        from model_complex_numbers import calculator
    result = calculator(data)
    result = result[0]
    log_ansv(result)
    bot.send_message(message.chat.id, f'Ответ = {result}')
    bot.send_message(message.chat.id, 'Что-то еще? /menu')

@bot.message_handler(content_types='text')
def message_reply(message):
    a = telebot.types.ReplyKeyboardRemove()
    if 'История вычислений' in message.text:
        read_logs = open('log.txt', 'r')
        for line in read_logs:
            bot.send_message(message.chat.id, line)
        read_logs.close()
        bot.send_message(message.chat.id,'Начать заново /menu', reply_markup=a)
    elif 'Рассчитать выражение' in message.text:
        bot.send_message(message.chat.id,'Введите выражение для рассчета без пробелов', reply_markup=a)
    global expression_list
    listsize = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for el in listsize:
        if str(el) in message.text:
            data = message.text
            expression_list = [el for el in message.text]
            bot.send_message(message.chat.id,'Для ответа напишите /answer')
            break

def select_model(text):
    model = 'rational'
    for el in text:
        if el == 'j':
            model = 'complex'
    return model

bot.polling()