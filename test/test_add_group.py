# этот скрипт пишет разработчик по тестам

# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application_group import Application_group


# если написать "@pytest.fixture", то наша функция из простой функции превращается в фикстуру
@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="testgroup", header="testheader", footer="testfooter"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()