from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.project_helper import ProjectHelper
from fixture.navigator_helper import NavigatorHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrezognized browser %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.navigator = NavigatorHelper(self)
        self.base_url =base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except ValueError:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.get(self.base_url)

    def change_field_value_by_name(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def destroy(self):
        self.wd.quit()
