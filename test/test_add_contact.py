# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

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