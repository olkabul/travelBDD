from behave import *
from selenium import webdriver
from features.Pages.login_page import LoginPage
from features.Pages.dashboard_page import DashboardPage

@step('I launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)

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

@step('I must successfully login to the Dashboard and see the "{msg}" message')
def verify_login(context,msg):
    expected_text = msg
    context.dashboard_page = DashboardPage(context.driver)
    actual_text = context.dashboard_page.get_header().text
    assert expected_text in actual_text, \
        "expected to see text {} but was {}".format(expected_text, actual_text)
    context.driver.close()

@step('I must stay on "{pnlname}"')
def verify_login_fail(context,pnlname):
    expected_text = pnlname
    actual_text = context.login_page.get_panel().text
    assert expected_text in actual_text, \
        "expected to see text {} but was {}".format(expected_text, actual_text)
    context.driver.close()