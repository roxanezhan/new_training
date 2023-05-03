from selenium.webdriver.common.by import By
import time

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("%s" % username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        #wd.find_element(By.XPATH, "//input[@value='Login']").click() #этот вариант тоже работает
        #wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click() #старый рабочий вариант
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        #wd.find_elements(By.LINK_TEXT, "Logout")
        time.sleep(2)
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        #wd.find_element(By.XPATH, "//div/div[1]/form/b")
        time.sleep(2)
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        #return wd.find_element(By.XPATH, "//div/div[1]/form/b").text == "(" + username + ")"  #этот вариант тоже работает
        #return wd.find_element(By.XPATH, "//div/div[1]/form/b").text == "(%s)" % username
        return wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)