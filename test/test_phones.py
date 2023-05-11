import re
from model.contact import Contact
from random import randrange

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_new(
            Contact(firstname="name_again", middlename="middlename_again", lastname="lastname_again",
                    nickname="nickname_again",title="title_again", company="company_again", address="address, again",
                    home_phone="11-12-15", mobile_phone="555-666-77-88", work_phone="23-23-23", fax="34-34-34",
                    email="111@222.qq", email2="222@222.qq", email3="333@222.qq", homepage="123.kz", bday="6",
                    bmonth="April", byear="1973", aday="1", amonth="January", ayear="2000", address2="address, www",
                    phone2="123", notes="test_qwerty", photo="C:\\GitProjetcs\\new_training\\icons\\camomille.jpg"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="", #удаление символа "\n" в конце, если в контакте указано 3 номера, а не 4 (home_phone, work_phone, mobile_phone, phone2). Т.е. фильтруем те значения, которые непустые
                            map(lambda x: clear(x), #со всех параметров contact будут удалены спец.символы "[() -]"
                                filter(lambda x: x is not None, #удалить все пустые строки. Т.е. те значения полей, у которых было задано None
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", # удаление символа "\n" в конце, если в контакте указано 2 email, а не 3 (email, email2, email3). Т.е. фильтруем те значения, которые непустые
                            filter(lambda x: x is not None, # удалить все пустые строки. Т.е. те значения полей, у которых было задано None
                                    [contact.email, contact.email2, contact.email3])))