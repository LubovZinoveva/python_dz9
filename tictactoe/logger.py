import json 

def save(a):
    with open("id.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(a,ensure_ascii=False))
    print('id успешно загружен в id.json')

def load():
    with open("id.json","r",encoding="utf-8") as fh:
        b = json.load(fh)
    return b 