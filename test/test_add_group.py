# этот скрипт пишет разработчик по тестам

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="testgroup", header="testheader", footer="testfooter"))
    #app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))