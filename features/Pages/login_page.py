class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

        self.email_field_name = "email"
        self.password_field_name = "password"
        self.login_css_selector = "form > button"
        self.login_panel_css_selector = "form .form-heading.text-center"
        self.login_error_css_selector = ".alert.alert-danger"

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_field_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_field_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_css_selector(self.login_css_selector).click()

    def get_login_btn(self):
        login_btn = self.driver.find_element_by_css_selector(self.login_css_selector)
        return login_btn

    def get_panel(self):
        panel = self.driver.find_element_by_css_selector(self.login_panel_css_selector)
        return panel

    def get_error_msg(self):
        error_msg = self.driver.find_element_by_css_selector(self.login_error_css_selector)
        return error_msg