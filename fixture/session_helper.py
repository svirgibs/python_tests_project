

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "username").clear()
        wd.find_element("name", "username").send_keys(username)
        wd.find_element("name", "password").clear()
        wd.find_element("name", "password").send_keys(password)
        wd.find_element("xpath", "//input[@type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()
        wd.find_element("name", "username")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements("link text", "Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element("css selector", "td.login-info-left span").text
