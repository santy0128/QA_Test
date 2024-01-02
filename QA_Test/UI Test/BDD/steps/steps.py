from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

@given('Im on the homepage')
def step_impl(context):
    context.driver=webdriver.Edge()
    context.driver.get("https://www.google.com")
    time.sleep(1)
    

@when('I type "{text}" into the search field')
def step_impl(context, text): 
    search=context.driver.find_element(By.XPATH,"//*[@id='APjFqb']") #busqueda del cuadro de texto
    search.send_keys("test automation")
    

@when('I click the Google Search button')
def step_impl(context):
    
    search_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
    search_button.click()

    time.sleep(2) # Espera para que los resultados se carguen completamente

@then('I go to the search results page, and the first 3 results contain the word "{keyword}"')
def step_impl(context,keyword):
    matrix=[]
    search_results=context.driver.find_elements(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']")
    contador_links=0
    for element in search_results:
        if keyword in element.text:
            contador_links=contador_links+1
            if contador_links==3:
                break

    assert contador_links==3, f"No hay coincidencias de la palabra {keyword} en los enlaces "

@given('I Search by keyword')
def step_impl(context):
    context.driver=webdriver.Edge()
    context.driver.get("https://www.google.com/") #busqueda de pagina web solicitada
    Search=context.driver.find_element(By.XPATH,"//*[@id='APjFqb']") #busqueda del cuadro de texto
    Search.send_keys("Test automation")
    Search.send_keys(Keys.ENTER)
    time.sleep(2)    

@when('I click on the first result link')
def step_impl(context):
    search_results=context.driver.find_elements(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']")#busqueda de links
    time.sleep(1)
    for result in search_results: 
        time.sleep(1)
        search=context.driver.find_element(By.PARTIAL_LINK_TEXT,result.text)
        search.click()
        time.sleep(1)
        break


@then('I go to the page, and the page title contains the word "{keyword}"')
def step_impl(context, keyword):
    
    assert keyword.lower() in context.driver.title.lower(), f"El titulo de la pagina no contiene la palabra {keyword}"

    # Cerrar el navegador después de la prueba
    context.driver.quit()
