from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.LINK_TEXT, "Last name")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # delete confirmation
        wd.switch_to.alert.accept()
        # wait
        time.sleep(2)
        self.contact_cache = None

    def add_new(self, contact):
        wd = self.app.wd
        # init contact createion
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact createion
        wd.find_element(By.NAME,"submit").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "tr[name='entry']"):
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                #text = element.text
                l_name = element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                f_name = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                self.contact_cache.append(Contact(id=id, firstname=f_name, lastname=l_name))
                #print("here is id: ", id)                #print("here is firstname:", f_name)                #print("here is lastname:", l_name)
        return list(self.contact_cache)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        #self.select_first_contact()
        # open modification form
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        if contact.photo:
            wd.find_element(By.XPATH, "//input[@name='photo']").clear()
            wd.find_element(By.XPATH, "//input[@name='photo']").send_keys(contact.photo)
        #self.change_field_value("//input[@name='photo']", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        #Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        if contact.bday:
            Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        #Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        if contact.bmonth:
            Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        #Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        if contact.aday:
            Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        #Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        if contact.amonth:
            Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    #def select_first_contact(self):
        #wd = self.app.wd
        #wd.find_element(By.NAME, "selected[]").click()