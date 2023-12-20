from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

t=.5
count=3#cantidad de links
Palabra_clave="automation" #palabra clave de busqueda y acceso a links
palabra_busqueda="Test automation"#palabra de busqueda
print(f"Los parametros de busqueda son: \nPalabra de busqueda: {palabra_busqueda}\nPalabra clave: {Palabra_clave}")
driver=webdriver.Edge()
driver.get("https://www.google.com/") #busqueda de pagina web solicitada
driver.maximize_window()

Search=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea") #busqueda del cuadro de texto
 
Search.send_keys(palabra_busqueda)
Search.send_keys(Keys.ENTER)
time.sleep(t)
int_error=0
search_results=driver.find_elements(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']")#busqueda de links
intentos=0#contador para links
for result in search_results: 
  time.sleep(t)
  if Palabra_clave in result.text.lower(): #determina si el link contiene palabra clave
    result.click()
    time.sleep(t)
    intentos = intentos + 1
    print(f"\nEl titulo de la pagina {intentos} es: {driver.title} y el link es: {driver.current_url}\n")
    driver.back()
    
    if intentos == count:  # Detiene el bucle después de hacer clic en los tres enlaces
      print("Prueba finalizada")
      break 
  
driver.quit()

    
    
    

