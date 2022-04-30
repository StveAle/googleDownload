from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Bebecita bblin

#sta vivo el pinche proyecto uwu
#A partir de aquí empieza el código espagueti

#Esta función verifica que esté actualizado el controlador de Chrome
def verificarDriver():
    chrome_options=Options()
    rutaDriver='./chromedriver.exce'
    try:
        driver=webdriver.Chrome(rutaDriver, options=chrome_options)
    except:
        print('El controlador de chrome está desactualizado o no se encuentra en la ruta definida')