from behave import *
from selenium import webdriver
from features.Pages.dashboard_page import DashboardPage
from features.Pages.admin_page import AdminPage
from features.driver_helper import get_elm_by_text
from features.driver_helper import get_elem_by_name

@when('Disable the Show header/footer option')
def disable_field(context):
    context.admin_page = AdminPage(context.driver)
    context.field = context.admin_page.get_field()
    context.field_text = "Disable"
    context.field.send_keys(context.field_text)
    context.current_text = context.admin_page.get_field().text

@when('Submit the changes')
def click_submit(context):
    # admin = AdminPage(context.driver)
    submit = context.admin_page.get_submit_btn()
    submit.click()

@then('I must see that "Show Header/Footer" option disabled indeed')
def verify_disabled(context):
    # admin = AdminPage(context.driver)
    # actual_text = admin.get_form_name().text
    expected_text = context.field_text
    actual_text = context.current_text
    assert expected_text in actual_text, \
        "expected to see text {} but was {}".format(expected_text, actual_text)
    context.driver.close()