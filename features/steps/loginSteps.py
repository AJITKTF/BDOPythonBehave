from behave import *

from features.Pages.Loginpage import LoginPage


@given(u'User launches BDO application and enters username"{user}",password"{password}"')
def step_impl(context,user,password):
    context.login = LoginPage(context.driver)
    context.login.enter_username_textbox(user)
    context.login.enter_password_textbox(password)

@given(u'User clicks on SignIn button')
def step_impl(context):
    context.login.click_on_signin()

@then(u'User validates succesfull login and clicks on continue button')
def step_impl(context):
    assert context.login.validate_login_successful()
    context.login.click_continue_button()

@then(u'User clicks on Logout')
def step_impl(context):
    context.login.click_logout_button()


