from bot_token import bot
from logger import load

chat_id = load()

def move_cross(list1, row, column):
    if list1[row][column] != '':
        bot.send_message(chat_id, 'Ошибка, место занято. Выберите новое с той же командой')
        new_row = int(input('Cтрока = '))
        new_column = int(input('Cтолбец = '))
        move_cross(list1, new_row - 1, new_column - 1)
    else:
        list1[row][column] = 'X'
    return list1

def move_zero(list2, row, column):
    if list2[row][column] != '':
        bot.send_message(chat_id, 'Ошибка, место занято. Выберите новое')
        new_row = int(input('Cтрока = '))
        new_column = int(input('Cтолбец = '))
        move_cross(list2, new_row - 1, new_column - 1)
    else:
        list2[row][column] = '0'
    return list2

   