# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to().alert
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.new_contact(wd, Contact(firstname="f_name", middlename="m_name", lastname="l_name", nickname="nick_name", title="title", company="company", address="address, qqq", home_phone="12-12-12", mobile_phone="111-121-12-12", work_phone="23-23-23", fax="34-34-34", email="111@222.qq", email2="222@222.qq", email3="333@222.qq", homepage="123.kz", bday="6", bmonth="April", byear="1973", aday="1", amonth="January", ayear="2000", address2="address, www", phone2="123", notes="qwerty"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def new_contact(self, wd, contact):
        # init contact createion
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        #wd.find_element(By.NAME, "photo").send_keys(contact.photo)
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").send_keys(contact.home_phone)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        wd.find_element(By.NAME, "work").send_keys(contact.work_phone)
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)
        # wd.find_element(By.XPATH, "(//input[@name='submit'])[2]").click()
        # submit contact createion
        wd.find_element(By.NAME,"submit").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("%s" % username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
