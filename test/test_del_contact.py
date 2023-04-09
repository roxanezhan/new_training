from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(
            Contact(firstname="test_name", middlename="test_name", lastname="test_name", nickname="test_name", title="test_title",
                    company="test_company", address="test_address, qqq", home_phone="12-12-12", mobile_phone="111-121-12-12",
                    work_phone="23-23-23", fax="34-34-34", email="111@222.qq", email2="222@222.qq", email3="333@222.qq",
                    homepage="123.kz", bday="6", bmonth="April", byear="1973", aday="1", amonth="January", ayear="2000",
                    address2="address, www", phone2="123", notes="test_qwerty",
                    photo="C:\\GitProjetcs\\new_training\\icons\\camomille.jpg"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts