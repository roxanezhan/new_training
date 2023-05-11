# -*- coding: utf-8 -*-
from model.contact import Contact
from sys import maxsize

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="F. Name", lastname="Fourthname", nickname="Veryn_name", \
                      title="title", company="company", address="address, qqq", home_phone="12-12-12", \
                      mobile_phone="111-121-12-12", work_phone="23-23-23", fax="34-34-34", email="111@222.qq", \
                      email2="222@222.qq", email3="333@222.qq", homepage="123.kz", bday="6", bmonth="April", \
                      byear="1973", aday="1", amonth="January", ayear="2000", address2="address, www", \
                      phone2="123", notes="qwerty", photo="C:\\GitProjetcs\\new_training\\icons\\camomille.jpg")
    app.contact.add_new(contact)
    print("len old contacts", len(old_contacts))
    print("count new contacts", app.contact.count())
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