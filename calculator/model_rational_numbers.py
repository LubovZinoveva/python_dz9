def actions(a, b, operation): 
    return {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}[operation](a, b)

def priority(text):
    # В выражении без скобок выполняем сначала */, затем +-
    delete = []
    for i in range(len(text)-1):
        if text[i] == '*':
            x = float(text[i-1])
            y = float(text[i+1])
            text[i+1] = actions(x, y, '*')
            delete.append(i-1)
            delete.append(i)
        elif text[i] == '/':
            x = float(text[i-1])
            y = float(text[i+1])
            text[i+1] = actions(x, y, '/')
            delete.append(i-1)
            delete.append(i)
        
    delete.reverse()
    for el in delete:
        text.pop(el)
    
    delete.clear()
    for i in range(len(text)-1):
        if text[i] == '+':
            x = float(text[i-1])
            y = float(text[i+1])
            text[i+1] = actions(x, y, '+')
            delete.append(i-1)
            delete.append(i)
        if text[i] == '-':
            x = float(text[i-1])
            y = float(text[i+1])
            text[i+1] = actions(x, y, '-')
            delete.append(i-1)
            delete.append(i)
    delete.reverse()
    for el in delete:
        text.pop(el)
    return text

def correct_data(data):    
    pop_list = []
    for i in range (len(data)-1):
        if data[i].isdigit() and data[i+1].isdigit():
            data[i+1] = data[i] + data[i+1]
            pop_list.append(i)
    pop_list.reverse()
    for el in pop_list:
        data.pop(el)
    
    pop_list.clear()
    for i in range (len(data)-1):
        if data[i] == '.':
            data[i+1] = str(float(data[i-1] + data[i] + data[i+1]))
            pop_list.append(i-1)
            pop_list.append(i)
    pop_list.reverse()
    for el in pop_list:
        data.pop(el)
    return data

def check_bracket(expression):
    # считаем только выражение в скобках 
    brackets = []
    index = []
    for i in range(len(expression)):
        if expression[i] == '(':
            index.append(i)
            for j in range(i+1, len(expression)):
                if expression[j] == ')':
                    index.append(j)
                    break
                brackets.append(expression[j])
    res = priority(brackets)
    expression[index[0]] = res[0]

    for i in range(index[1], index[0], -1):
        expression.pop(i)
    return expression

def calculator(data):
    data = correct_data(data)
    while '(' in data:
        check_bracket(data) 
    return priority(data)