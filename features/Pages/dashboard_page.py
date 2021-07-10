class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        self.main_header_id = "mainHeader"
        self.buttons_css_selector = "#social-sidebar-menu>li"
        self.sbbuttons_css_selector = "#social-sidebar-menu ul.in>li"
        self.formname_css_selector = "form .panel-title.pull-left"
        self.logout_id = "Logout"

    def get_header(self):
        header = self.driver.find_element_by_id(self.main_header_id)
        return header

    def get_buttons(self):
        buttons = self.driver.find_elements_by_css_selector(self.buttons_css_selector)
        return buttons

    def get_sbbuttons(self):
        sbbuttons = self.driver.find_elements_by_css_selector(self.sbbuttons_css_selector)
        return sbbuttons