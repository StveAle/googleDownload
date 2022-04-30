import inicializar as bt
import funciones_utiles as fu
import os

######################################################################################
#                           PENDIENTES
# 1-Eliminar los mensajes de error
# 2-                            

######################################################################################


if __name__=='__main__':
    find=input('Ingrese la o las palabras clave de lo que quiere buscar: ')
    driver=bt.verificarDriver()
    fu.buscarImg(driver,find)    
    nImagenes=input('¿Cuantas imagenes desea descargar?')
    folderAddress=fu.checkFolder(find)
    fu.guardarImg(driver,nImagenes,folderAddress,find)

    input('LAS IMAGENES FUERON GUARDADES CON EXITO')
    
