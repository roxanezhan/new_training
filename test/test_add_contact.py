# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2 #генератор случайных символов в строке, где " "*10 означает увеличение частоты пробелов в 10 раз
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генератор случайных строк

def random_numbers(maxlen):
    numbers = string.digits + "-"*3
    return "".join(
        [random.choice(numbers) for i in range(maxlen)])  # генератор случайных числовых последовательностей

def random_emails_homepage(prefix, postfix, maxlen):
    symbolsemail = string.ascii_letters + string.digits #генератор случайных символов в строке, где " "*10 означает увеличение частоты пробелов в 10 раз
    return prefix + "".join(
        [random.choice(symbolsemail) for i in range(random.randrange(maxlen))]) + postfix # генератор случайных строк

#сначала проверяется тест на пустых данных, потом цикл из случайно сгенерированнх полей:
testdata_C = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                      lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                      title=random_string("title", 10), company=random_string("company", 10),
                      address=random_string("address", 10), home_phone=random_numbers(10),
                      mobile_phone=random_numbers(10), work_phone=random_numbers(10), fax=random_numbers(10),
                      email=random_emails_homepage("email", "@gmail.kz", 10),
                      email2=random_emails_homepage("email2", "@gmail.kz", 10),
                      email3=random_emails_homepage("email3", "@gmail.kz", 10),
                      homepage=random_emails_homepage("page", ".kz", 10), bday=random.choice('123456789'),
                      bmonth="April", byear="1973", aday=random.choice('123456789'), amonth="January",
                      ayear="2000", address2=random_string("address2", 10),
                      phone2=random_numbers(10), notes=random_string("notes", 10), photo="C:\\GitProjetcs\\new_training\\icons\\camomille.jpg")
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata_C, ids=[repr(x) for x in testdata_C])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    #print("len old contacts", len(old_contacts))
    #print("count new contacts", app.contact.count())
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", \
#                      title="", company="", address="", home_phone="", \
#                      mobile_phone="", work_phone="", fax="", email="", \
#                      email2="", email3="", homepage="", bday="", bmonth="", \
#                      byear="", aday="", amonth="", ayear="", address2="", \
#                      phone2="", notes="", photo="")
#    app.contact.add_new(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)