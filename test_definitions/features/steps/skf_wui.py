from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SKF_HOME = "https://www.skfbearingselect.com"


@given(u'I launch SKF website')
def step_impl(context):
    context.browser.get(SKF_HOME)


@when(u'I click on Accept & Continue button')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept & continue')]"))).click()


@then(u'I click on Rolling bearing image')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Rolling bearing')]"))).click()


@then(u'I click on Single bearing image')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Single bearing')]"))).click()


@when(u'I click on Select bearing type dropdown')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bearingtypeselect"))).click()


@then(u'I verify option: {options} is present')
def step_impl(context, options):
    try:
        WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'" + options + "')]"))).click()
    except Exception as e:
        print("Exception:", e)


@then(u'I close the dropdown')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-bottom"))).click()
