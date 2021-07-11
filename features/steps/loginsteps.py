from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.Pages.login_page import LoginPage
from features.Pages.dashboard_page import DashboardPage

@step('I launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@step('I open PHPTRAVEL login page')
def open_login_page(context):
    context.driver.get("https://www.phptravels.net/admin")

@step('Enter email "{email}" and password "{pwd}"')
def enter_credentials(context,email,pwd):

    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(pwd)


@step('Click on login button')
def click_login(context):
    context.login_page.click_login()

@step('I am redirected to a page with a "{msg}" message')
def verify_login(context,msg):
    expected_text = msg
    context.dashboard_page = DashboardPage(context.driver)
    actual_text = context.dashboard_page.get_header().text
    assert expected_text in actual_text, \
        "expected to see text {} but was {}".format(expected_text, actual_text)
    context.driver.close()

@step('I make sure I am on "{pnlname}"')
def verify_login_fail(context,pnlname):
    expected_text = pnlname
    actual_text = context.login_page.get_panel().text
    assert expected_text in actual_text, \
        "expected to see text {} but was {}".format(expected_text, actual_text)

@step('I see an error message "{error_wrn}"')
def verify_error_text(context,error_wrn):
    wait = WebDriverWait(context.driver, 5)
    wait.until(EC.visibility_of(context.login_page.get_error_msg()))
    expected_text = error_wrn
    actual_text = context.login_page.get_error_msg().text
    assert expected_text in actual_text, \
        "expected to see text {} but was {}".format(expected_text, actual_text)
    context.driver.close()