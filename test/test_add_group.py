# этот скрипт пишет разработчик по тестам

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.group.create(Group(name="testgroup", header="testheader", footer="testfooter"))
    app.manager.session.logout()

def test_add_empty_group(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.group.create(Group(name="", header="", footer=""))
    app.manager.session.logout()