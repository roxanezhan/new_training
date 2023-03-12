# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.new_contact(Contact(firstname="f_name", middlename="m_name", lastname="l_name", nickname="nick_name", title="title", company="company", address="address, qqq", home_phone="12-12-12", mobile_phone="111-121-12-12", work_phone="23-23-23", fax="34-34-34", email="111@222.qq", email2="222@222.qq", email3="333@222.qq", homepage="123.kz", bday="6", bmonth="April", byear="1973", aday="1", amonth="January", ayear="2000", address2="address, www", phone2="123", notes="qwerty", photo="C:\\GitProjetcs\\new_training\\icons\\camomille.jpg"))
        app.logout()
