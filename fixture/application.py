# этот скрипт пишет разработчик по вспомогательным методам
from selenium import webdriver
from fixture.managerHelpers import ManagerHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.manager = ManagerHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()