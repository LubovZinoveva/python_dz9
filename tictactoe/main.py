import telebot
from random import *
from telebot import types
from random import randint 
from bot_token import bot
from logger import save
from logger import load
from print import print_matrix
from move import *
from chek_win import win_check
from bot_token import bot
from logger import load

first_move = randint(1, 2)
num = -1
variant = -1
name = ''
name1 = ''
name2 = ''
my_step = 1
my_playing_field = []
my_row = -1
my_column = -1
round = -1
step = 1
first = ''
second = ''
chat_id = load()
 

@bot.message_handler(commands=['start'])
def start_message(message):
    start = ['Привет, сыграем партеечку :)', 'Здарова, братюнь', 'Кого я вижу, какая встреча!)', 'Проходи, гостем будешь']
    index = randint(0, 3)
    bot.send_message(message.chat.id, start[index])
    bot.send_message(message.chat.id,"Выбери размерность поля, напиши: /size")
    id = message.chat.id
    save(id)

@bot.message_handler(commands=['size'])
def size(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3=types.KeyboardButton("3")
    item4=types.KeyboardButton("4")
    item5=types.KeyboardButton("5")
    item6=types.KeyboardButton("6")
    item7=types.KeyboardButton("7")
    item8=types.KeyboardButton("8")
    item9=types.KeyboardButton("9")
    markup.add(item3, item4, item5, item6, item7, item8, item9)
    bot.send_message(message.chat.id,'Жмякай кнопку', reply_markup=markup)

    @bot.message_handler(content_types='text')
    def message_reply(message):
        listsize = [3, 4, 5, 6, 7, 8, 9]
        for el in listsize:
            if str(el) in message.text:
                global num
                num = el
                a = telebot.types.ReplyKeyboardRemove()
                bot.send_message(message.chat.id,'Отлично! Теперь определимся с режимом игры, пиши /mode', reply_markup=a)

@bot.message_handler(commands=['mode'])
def mode(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("/1 C другом")
    item2=types.KeyboardButton("/2 C ботом")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Выбирай скорее', reply_markup=markup)

@bot.message_handler(commands=['1'])
def var1(message):
    global variant
    variant = 1
    b = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Послдний шаг перед игрой! Пиши /name', reply_markup=b)
    
@bot.message_handler(commands=['2'])
def var2(message):
    global variant
    variant = 2
    b = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Последний шаг перед игрой! Пиши /name', reply_markup=b)

@bot.message_handler(commands=['name'])
def name(message):
    global variant
    bot.send_message(message.chat.id,'Познакомимся немного ближе)')
    if variant == 1:
        bot.send_message(message.chat.id,'Напиши имя первого игрока /player1 Имя. Например: /player1 Няшка')
        bot.send_message(message.chat.id,'А затем имя второго игрока /player2 Имя')
    elif variant == 2:
        bot.send_message(message.chat.id,'Напиши как хочешь, чтобы я тебя называл через /player Имя. Например: /player Пирожок')

@bot.message_handler(commands=['player1'])
def name1(message):
    global name1 
    n1 = message.text.split()[1:]
    name1 = ' '.join(n1)
    bot.send_message(message.chat.id,'Гуд! Теперь давай второе')

@bot.message_handler(commands=['player2'])
def name2(message):
    global name2 
    quest = message.text.split()[1:]
    name2 = ' '.join(quest)
    bot.send_message(message.chat.id, 'Время приключений! Погнали, пиши /play')

@bot.message_handler(commands=['player'])
def name(message):
    global name 
    quest = message.text.split()[1:]
    name = ' '.join(quest)
    print(name)
    bot.send_message(message.chat.id,f'Время приключений, {name}! Погнали, пиши /play')    

@bot.message_handler(commands=['play'])
def play(message):
    if variant == 1:
        play_with_friend(num, name1, name2, first_move)
    elif variant == 2:
        play_with_bot(num, name, first_move)

def bot_move(array):
    result = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '':
                result.append(i)
                result.append(j)
                break
    return result 

@bot.message_handler(commands=['step1'])
def bot1_step(message):
    global my_playing_field
    bot.send_message(chat_id, f'ХОД {step}') 
    print_matrix(my_playing_field, num)
    bot.send_message(chat_id, 'Бот ходит. Делает выбор..')
    b_move = bot_move(my_playing_field)
    bot.send_message(chat_id, f'Строка = {b_move[0]+1}')
    bot.send_message(chat_id, f'Столбец = {b_move[1]+1}')
    my_row = b_move[0]
    my_column = b_move[1]
    my_playing_field = move_cross(my_playing_field, my_row, my_column)
    if step > 2:
        if win_check(my_playing_field):
            print_matrix(my_playing_field, num)
            bot.stop_polling()
    if step == round - 1:    
        bot.send_message(chat_id, 'Ничья! Конец игры :)')
        bot.stop_polling()
    else:
        print_matrix(my_playing_field, num)
        bot.send_message(chat_id, f'{name} ходит. Выберите позицию на поле')
        bot.send_message(chat_id, 'Напишите /n №строки')    

@bot.message_handler(commands=['my_step'])
def my_step(message):
    bot.send_message(chat_id, f'ХОД {step}') 
    print_matrix(my_playing_field, num)
    bot.send_message(chat_id, 'Ведите номер строки. Напишите /r №строки')

@bot.message_handler(commands=['r'])
def my_row(message):
    global my_row
    my_row = int(message.text.split()[1])
    bot.send_message(chat_id, 'А теперь /m №столбца')

@bot.message_handler(commands=['n'])
def row(message):
    global my_row
    mes = message.text.split()[1:]
    my_row = int(message.text.split()[1])
    bot.send_message(chat_id, 'А теперь /st №столбца')

@bot.message_handler(commands=['st'])
def my_column(message):
    global step
    global my_column
    global my_playing_field
    my_column = int(message.text.split()[1])
    my_playing_field = move_zero(my_playing_field, my_row - 1, my_column - 1)
    if win_check(my_playing_field):
        print_matrix(my_playing_field, num)
        bot.stop_polling()
    else:
        bot.send_message(chat_id, 'Едем дальше. Жми /step1') 
    step += 1
    
@bot.message_handler(commands=['m'])
def column(message):
    global step
    global my_column
    global my_playing_field
    global my_row
    my_column = int(message.text.split()[1])
    my_playing_field = move_cross(my_playing_field, my_row - 1, my_column - 1)
    if step > 2:
        if win_check(my_playing_field):
            print_matrix(my_playing_field, num)
            bot.stop_polling()
        if step == round - 1:
            bot.send_message(chat_id, 'Ничья! Конец игры :)')    
            bot.stop_polling()
    print_matrix(my_playing_field, num)
    bot.send_message(chat_id, 'Бот ходит. Выбирает позицию..')
    b_move = bot_move(my_playing_field)
    bot.send_message(chat_id, f'Строка = {b_move[0]+1}')
    bot.send_message(chat_id, f'Столбец = {b_move[1]+1}')
    my_row = b_move[0]
    my_column = b_move[1]
    my_playing_field = move_zero(my_playing_field, my_row, my_column)
    if win_check(my_playing_field):
        print_matrix(my_playing_field, num)
        bot.stop_polling()
    else:
        bot.send_message(chat_id, 'Едем дальше. Жми /my_step')        
    step += 1
    bot.send_message(chat_id, 'Едем дальше. Жми /my_step')

def play_with_bot(N, player, move1):
    global round
    global my_playing_field
    global step
    global chat_id 
    step = 1
    chat_id = load()
    my_playing_field = []
    for i in range(N):
        my_playing_field.append(["" for _ in range(N)])
    round = (N*N)//2 + 1
    if N % 2 != 0:
        round += 1
    if move1 == 1:
        bot.send_message(chat_id, f'{player} ходит первым, играет крестиками')
        bot.send_message(chat_id, 'Бот играет ноликами')
        bot.send_message(chat_id, 'Жми /my_step')
    else:
        bot.send_message(chat_id, 'Бот ходит первым, играет крестиками')
        bot.send_message(chat_id, f'{player} играет ноликами')
        bot.send_message(chat_id, 'Жми /step1')

@bot.message_handler(commands=['move1'])
def move1(message):
    bot.send_message(chat_id, f'ХОД {step}') 
    print_matrix(my_playing_field, num)
    bot.send_message(chat_id, 'Ведите номер строки и столбца. Напиши /ss №строки № столбца. Например, /ss 3 1')

@bot.message_handler(commands=['ss'])
def ss(message):
    global my_playing_field
    qq = message.text.split()[1:]
    my_row = int(qq[0])
    my_column = int(qq[1])
    my_playing_field = move_cross(my_playing_field, my_row - 1, my_column - 1)
    if win_check(my_playing_field):
        bot.stop_polling()
    elif num*num % 2 != 0 and step == round - 1:
            bot.send_message(chat_id, 'Ничья! Конец игры :)')    
            bot.stop_polling()
    else:
        bot.send_message(chat_id, f'{second}, твоя очередь. Напиши /tt №строки № столбца')
    print_matrix(my_playing_field, num)
   
@bot.message_handler(commands=['tt'])
def move1(message):
    global my_playing_field
    global step
    qq = message.text.split()[1:]
    my_row = int(qq[0])
    my_column = int(qq[1])
    my_playing_field = move_zero(my_playing_field, my_row - 1, my_column - 1)
    if step > 2:
        if win_check(my_playing_field):
            print_matrix(my_playing_field, num)
            bot.stop_polling()
    elif step == round - 1:    
        bot.send_message(chat_id, 'Ничья! Конец игры :)')
        bot.stop_polling()
    else: 
        bot.send_message(chat_id, 'Продолжим, жмите /move1')
    step += 1
        
def play_with_friend(N, player1, player2, move1):
    global round
    global step
    global first
    global second
    global chat_id 
    chat_id = load()
    if move1 == 1:
        bot.send_message(chat_id, f'{player1} ходит первым, играет крестиками')
        bot.send_message(chat_id, f'{player2} играет ноликами')
        first = player1
        second = player2
    else:
        bot.send_message(chat_id, f'{player2} ходит первым, играет крестиками')
        bot.send_message(chat_id, f'{player1} играет ноликами')
        first = player2
        second = player1
    for i in range(N):
        my_playing_field.append(["" for _ in range(N)])
    round = (N*N)//2 + 1
    if N*N % 2 != 0:
        round += 1
    bot.send_message(chat_id, 'Вперед, в игру! жми /move1')

bot.polling()