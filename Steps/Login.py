from behave import *

@Given I am on the Sign in page
def step_impl(context):
    context.Browser.go_to('sign-in')


@When I input a valid email
def step_impl(context):
    pass


@When I input a valid password
def step_impl(context):
    pass


@When i click the login button
def step_impl(context):
    pass


@Then I recive the succes message and I am on the main page
def step_impl(context):
    pass
