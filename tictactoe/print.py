from bot_token import bot
from logger import load

chat_id = load()

def print_matrix(mas, n):
    row1 = []
    row1.append('//1')
    for i in range (2, n+1):
        row1.append(f'|{i}')
    rr = "".join(row1)
    bot.send_message(chat_id, f'{rr}')
    row1.clear()
    for i in range(n):
        row1.append(str(i+1))
        for j in range(n):
            if mas[i][j] == '':
                row1.append('|_')
            else:
                row1.append(f'|{mas[i][j]}')
        row1.append('|')
        tt = "".join(row1)
        bot.send_message(chat_id, f'{tt}')
        row1.clear()