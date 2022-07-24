
class NavigatorHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php")):
            wd.find_element("link text", "Manage").click()
