# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

#использование константных данных удобно при тесте фиксированных данных.
# После успешного прохождения теста с фиксированными данными, можно проверять тесты с рандомными данными
constant = [
    Group(name="constantname1", header="constantheader1", footer="constantfooter1"),
    Group(name="constantname2", header="constantheader2", footer="constantfooter2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10 #генератор случайных символов в строке, где " "*10 означает увеличение частоты пробелов в 10 раз
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генератор случайных строк

#сначала проверяется тест на пустых данных, потом цикл из случайно сгенерированнх полей:
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)
]

#чередование пустых и непустых полей в тесте с использованием list comprehension. На выходе будет 8 возможных вариантов:
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)] #цикл for пробегает по 2м возможным значением (пустое и случайное)
#    for header in ["", random_string("header", 20)]
#    for footer in ["", random_string("footer", 20)]
#]