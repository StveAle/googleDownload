from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

#Esta función verifica que esté actualizado el controlador de Chrome
def verificarDriver():

    chrome_options=Options()
    chrome_options.add_argument("--headless")
    thisFolder=os.getcwd()
    rutaDriver=r'./chromedriver.exe'
    try:
        driver=webdriver.Chrome(rutaDriver, options=chrome_options)
    except:
        print('El controlador de chrome está desactualizado o no se encuentra en la ruta definida')
        print('Puedes descargar el controlador en: https://sites.google.com/a/chromium.org/chromedriver/home')
        input(f'Recuerda guardar el driver en: {thisFolder}')
        exit()
        
    return driver

