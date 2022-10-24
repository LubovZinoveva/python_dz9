from bot_token import bot
from logger import load

chat_id = load()

def check_array(array):
    count = 1
    result = False
    for j in range(len(array)-1):
            if array[j] == array[j + 1]:
                count += 1
                if count == 3:
                    if array[j] == 'X':
                        bot.send_message(chat_id, 'ПОЗДРАВЛЯЕМ, КРЕСТИКИ ВЫИГРАЛИ!')
                        result = True
                        break
                    elif array[j] == '0':
                        bot.send_message(chat_id, 'ПОЗДРАВЛЯЕМ, НОЛИКИ ВЫИГРАЛИ!')
                        result = True
                        break
            else:
                count = 1
    return result

def win_check(arr):
    result = False
    # Проверяем по строкам
    for i in range(len(arr)):
       my_list = [j for j in arr[i]]
       if check_array(my_list):
            result = True
            break

    # Проверяем по столбцам        
    for i in range(len(arr)):
        column = [x[i] for x in arr]
        if check_array(column):
            result = True
            break

    # Проверяем по первым диагоналям
    list_check1 = []
    for i in range(len(arr)-2):
        count = 0
        for j in range(i+2, -1, -1):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()

    for i in range(1, len(arr)-2):
        count = i
        for j in range(len(arr)-2, i-2, -1):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()

    # Проверяем по вторым диагоналям
    
    list_check1 = []
    for i in range(len(arr)-2):
        count = 0
        for j in range(len(arr)-i-3, len(arr)):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()

    for i in range(1, len(arr)-2):
        count = i
        for j in range(len(arr)-i):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()
    
    return result