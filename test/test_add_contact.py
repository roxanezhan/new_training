# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.contact.add_new(Contact(firstname="f_name", middlename="m_name", lastname="l_name", nickname="nick_name", title="title", company="company", address="address, qqq", home_phone="12-12-12", mobile_phone="111-121-12-12", work_phone="23-23-23", fax="34-34-34", email="111@222.qq", email2="222@222.qq", email3="333@222.qq", homepage="123.kz", bday="6", bmonth="April", byear="1973", aday="1", amonth="January", ayear="2000", address2="address, www", phone2="123", notes="qwerty", photo="C:\\GitProjetcs\\new_training\\icons\\camomille.jpg"))
