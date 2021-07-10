class AdminPage():

    def __init__(self, driver):
        self.driver = driver

        self.form_name_css_selector = "form .panel-title.pull-left"
        self.control_name = "showHeaderFooter"
        self.submit_btn_css_selector = "form button"

    def get_form_name(self):
        form_name = self.driver.find_element_by_css_selector(self.form_name_css_selector)
        return form_name

    def get_field(self):
        field = self.driver.find_element_by_name(self.control_name)
        return field

    def get_control_text(self):
        control_text = self.driver.find_element_by_name(self.control_name).text
        return control_text

    def get_submit_btn(self):
        submit_btn = self.driver.find_element_by_css_selector(self.submit_btn_css_selector)
        return submit_btn
