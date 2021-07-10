class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_field_name = "email"
        self.password_field_name = "password"
        self.login_css_selector = "form > button"
        self.login_panel_css_selector = "form .form-heading.text-center"

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_field_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_field_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_css_selector(self.login_css_selector).click()

    def get_panel(self):
        panel = self.driver.find_element_by_css_selector(self.login_panel_css_selector)
        return panel