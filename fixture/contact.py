from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.LINK_TEXT, "Last name")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # wd.find_element(By.LINK_TEXT, "home").click()
        self.open_contact_page()
        # select first contact
        # wd.find_element(By.NAME, "selected[]").click()
        self.select_contact_by_index(index)
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
        wd.find_element(By.NAME, "submit").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # self.select_contact_by_index(index)
        # open modification form
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
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
        # self.change_field_value("//input[@name='photo']", contact.photo)
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
        # Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        if contact.bday:
            Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        # Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        if contact.bmonth:
            Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        if contact.aday:
            Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        # Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                #print("\nthe id is:", id)
                cells = element.find_elements(By.TAG_NAME, "td")
                firstname = cells[2].text #в списке девтулса выбрать td 3-й по счету
                #print("\nthis is firstname:", firstname, "\nfirstnameend")
                lastname = cells[1].text #в списке девтулса выбрать td 2-й по счету
                #print("\nthis is lastname:", lastname, "\nlastnameend")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7] #выбрать рисунок карандашик для редактирования контакта. в списке девтулса выбрать td 8-й по счету (это элемент карандашика)
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6] #выбрать рисунок человечка для просмотра контакта. в списке девтулса выбрать td 7-й по счету (это элемент человечка)
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address, email=email, email2=email2, email3=email3,
                       home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone, phone2=phone2)