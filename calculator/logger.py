from datetime import datetime as dt

def log_expression(data):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.txt', 'a') as file:
        file.write('Время: {}; {} = '
                    .format(time, data))

def log_ansver(data):
    with open('log.txt', 'a') as file:
        file.write(f'{data}\n')


