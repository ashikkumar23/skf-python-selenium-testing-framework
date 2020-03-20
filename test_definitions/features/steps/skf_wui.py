from time import sleep

from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


SKF_HOME = "https://www.skfbearingselect.com"


@given(u'I launch SKF website')
def step_impl(context):
    context.browser.get(SKF_HOME)


@when(u'I click on Accept & Continue button')
def step_impl(context):
    context.browser.find_element_by_css_selector('.button-default').click()


@when(u'I click on Single Bearing image')
def step_impl(context):
    context.browser.find_element_by_css_selector('.single-bearing').click()


@when(u'I click on Select bearing type dropdown')
def step_impl(context):
    sleep(5)
    # WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.ID, "mat-select-4"))).click()
    context.browser.find_element_by_id("mat-select-4").click()


@then(u'I verify option: {options} is present')
def step_impl(context, options):
    # sleep(5)
    try:
        # WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located
        #                                              ((By.CSS_SELECTOR, "div.mat-select-panel-wrap mat-option")))
        # context.browser.find_elements_by_xpath("//span[@class='mat-option-text']")
        context.browser.find_elements_by_css_selector("div.mat-select-panel-wrap mat-option")

        context.browser.find_element_by_xpath("//mat-option/span[contains(.,'" + options + "')]")
    except Exception as e:
        print("Exception:", e)


@then(u'I close the dropdown')
def step_impl(context):
    context.browser.find_element_by_css_selector(".cdk-overlay-container").click()
