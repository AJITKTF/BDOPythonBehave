from behave import *

from features.Pages.Transactionpage import Transactionpage


@then(u'User navigates to transactions lookup page')
def step_impl(context):
    context.transact = Transactionpage(context.driver)
    context.transact.click_transaction_lookup_page()
    assert context.transact.click_transaction_lookup_page_title()

@when(u'User enters search fields "{start_date}" and "{end_date}" and "{card_number}"')
def step_impl(context, start_date, end_date, card_number):
    context.transact.enter_transaction_search_fields(start_date, end_date, card_number)

@when(u'User clicks on Search button in transaction lookup page')
def step_impl(context):
    context.transact.click_search_button()

@when(u'User searches and validates transcation "{trn_number}" searched in the grid')
def step_impl(context,trn_number):
    context.transact.find_transaction_in_lookup_page(trn_number)

@then(u'User validates POS data in transaction details page "{data1}" and "{data2}" and "{data3}" and "{data4}"')
def step_impl(context, data1, data2, data3, data4):
    context.transact.validate_transaction_details(data1, data2, data3, data4)

@then(u'User validates Other data in transaction details page')
def step_impl(context):
    pass