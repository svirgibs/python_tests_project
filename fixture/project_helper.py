from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        self.go_to_manage_projects()
        self.init_create_new_project()
        self.fill_form(project)
        self.submit_create()
        self.return_to_projects_page()

    def delete_project_by_name(self, name):
        self.go_to_manage_projects()
        self.go_to_project_by_name(name)
        self.click_on_delete_button()
        self.submit_delete()

    def submit_delete(self):
        self.click_on_delete_button()

    def click_on_delete_button(self):
        wd = self.app.wd
        wd.find_element("xpath", "//input[@value='Delete Project']").click()

    def go_to_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element("link text", name).click()

    def get_project_list(self):
        wd = self.app.wd
        self.app.navigator.go_to_manage()
        self.go_to_manage_projects()
        project_list =[]
        elements = wd.find_elements("xpath", "//table[3]//tbody/tr")
        elements = elements[2:]
        for row in elements:
            td_list = row.find_elements("xpath", "td")
            project_list.append(Project(name=td_list[0].text,
                                        status=td_list[1].text,
                                        enabled=td_list[2].text,
                                        view_status=td_list[3].text,
                                        description=td_list[4].text))
        return project_list

    def return_to_projects_page(self):
        wd = self.app.wd
        wd.find_element("link text", "Proceed").click()

    def submit_create(self):
        wd = self.app.wd
        wd.find_element("xpath", "//input[@value='Add Project']").click()

    def fill_form(self, project):
        self.app.change_field_value_by_name("name", project.name)

    def init_create_new_project(self):
        wd = self.app.wd
        wd.find_element("xpath", "//input[@value='Create New Project']").click()

    def go_to_manage_projects(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element("link text", "Manage Projects").click()
