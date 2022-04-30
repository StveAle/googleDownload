from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import urllib.request


#Esta función abre el navegador, ingresa a google y navega en google imagenes.
#La variable find es lo que se va a buscar en google imagenes. 
def buscarImg(driver,find):
    driver.maximize_window()
    driver.get('https://www.google.com')
    buscador=driver.find_element_by_xpath('//input[@maxlength="2048"]')
    buscador.send_keys(find)
    buscador.submit()
    
    #Ingresar a google Imagenes
    driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    #Cargar todas las imagenes de una hoja.
    for i in range(7):
        driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
        time.sleep(0.5)

#Verifica si la carpeta existe, y si no existe la crea
def checkFolder(nameFile):
  location=os.path.dirname(__file__)
  try: os.mkdir(nameFile)
  except: pass
  location=location+'\\{}'.format(nameFile)
  return location

#guarda las imagenes descargadas
def guardarImg(driver,nImg,ruta,name):
    imagenes=[]
    
    #Si la cantidad de imagenes solicitadas supera las 400 carga 2 hojas.
    if nImg>400:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        for i in range(7):
            driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
            time.sleep(0.6)
    
    try:
        imagenes=driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')             
    except:
        print('No se pudo extraer las imágenes')
    
    i=0
    for imagen in imagenes:    
        if nImg==i: break

        try:
            imagen.click()            
            xpathIMG='/html/body/div[3]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'
            srcObject=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,xpathIMG)))
            src=srcObject.get_attribute('src')
            
            ext=src.split('.')[-1:]
            ext='.'+ext[0]
            if len(ext)>5 or len(ext)<2:               
                urllib.request.urlretrieve(src,ruta+'\\'+name+'_'+str(i+1)+'.png')            
                """ if sis=='Linux':               
                    urllib.request.urlretrieve(src,ruta+'/'+name+str(i+1)+'.png') """            
            else:
                urllib.request.urlretrieve(src,ruta+'\\'+name+'_'+str(i+1)+ext)

                """ if sis=='Linux':
                    urllib.request.urlretrieve(src,ruta+'/'+name+str(i+1)+ext) """
                
            print('imagen '+name+' '+str(i+1)+' guardada')
            i+=1    
        except:
            print('no pudo descargarse')