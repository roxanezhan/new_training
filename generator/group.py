import jsonpickle
from model.group import Group
import random
import string
import os.path
import getopt   #для чтения опций командной строки
import sys      #для того, чтобы получить доступ к опциям командной строки

#выполнение генератора данных параметризованным.
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5   #это дефолтные значения
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10 #генератор случайных символов в строке, где " "*10 означает увеличение частоты пробелов в 10 раз
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генератор случайных строк

#сначала проверяется тест на пустых данных, потом цикл из случайно сгенерированнх полей:
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(n)
]

#чередование пустых и непустых полей в тесте с использованием list comprehension. На выходе будет 8 возможных вариантов:
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)] #цикл for пробегает по 2м возможным значением (пустое и случайное)
#    for header in ["", random_string("header", 20)]
#    for footer in ["", random_string("footer", 20)]
#]

#file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json") #мы сейчас находимся в пакете genetaror,
# а нам нужно перейти в пакет data. Для этого переходим на 1 уровень вверх в родительскую директорией командой "../".
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) # и создание параметризованного названия файла
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))