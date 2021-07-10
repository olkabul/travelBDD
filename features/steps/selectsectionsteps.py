from behave import *
from selenium import webdriver
from features.Pages.dashboard_page import DashboardPage
from features.Pages.admin_page import AdminPage
from features.driver_helper import get_elm_by_text

@when('Open the "{menu}" menu')
def open_section(context,menu):
    context.dashboard_page = DashboardPage(context.driver)
    buttons = context.dashboard_page.get_buttons()
    selected_button = get_elm_by_text(menu, buttons)
    selected_button.click()

@when('Click on "{submenu}" section')
def click_section(context, submenu):
    sbbuttons = context.dashboard_page.get_sbbuttons()
    sbbutton = get_elm_by_text(submenu, sbbuttons)
    sbbutton.click()

@then('I must see the "{formname}" page')
def verify_page(context,formname):
    expect_text = formname
    admin_page = AdminPage(context.driver)
    actual_text = admin_page.get_form_name().text
    assert expect_text in actual_text, \
        "expected to see text {} but was {}".format(expect_text, actual_text)
    context.driver.close()
