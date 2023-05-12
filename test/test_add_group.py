# этот скрипт пишет разработчик по тестам
# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#from data.add_group import testdata
from data.add_group import constant as testdata #удобно, если нужно использовать фиксированные значения и при этом эту константу можно переименовать

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()   #count() выступает в роли хеш функции
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
