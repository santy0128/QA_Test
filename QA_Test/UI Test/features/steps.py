from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Im on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")

@when('I type "{text}" into the search field')
def step_impl(context, text):
    search=context.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
    search.send_keys(text)

@when('I click the Google Search button')
def step_impl(context):
    search_button = context.driver.find_element_by_name('btnK')
    search_button.click()
    time.sleep(2)  # Espera corta para que los resultados se carguen completamente

@then('I go to the search results page, and the first 3 results contain the word "{keyword}"')
def step_impl(context, keyword):
    search_results=driver.find_elements(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']")
    results_text = [result.text.lower() for result in search_results[:3]]
    assert all(keyword.lower() in result for result in results_text)

@given('I Search by keyword')
def step_impl(context):
    pass  

@when('I click on the first result link')
def step_impl(context):
    first_result = context.driver.find_element_by_css_selector('div.g h3 a')
    first_result.click()
    time.sleep(2)  # Espera corta para que la página cargue completamente

@then('I go to the page, and the page title contains the word "{keyword}"')
def step_impl(context, keyword):
    assert keyword.lower() in context.driver.title.lower()

    # Cerrar el navegador después de la prueba

    context.driver.quit()