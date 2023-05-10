# этот скрипт пишет разработчик по тестам
# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


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

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()   #count() выступает в роли хеш функции
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
