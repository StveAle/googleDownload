import inicializar as bt
import funciones_utiles as fu

######################################################################################
#                           PENDIENTES
# 1-Eliminar los mensajes de error
# 2-Cerrar el driver cuando finalice el script
# 3-Escoger una ubicación diferente para guardar las imagenes.                        
#
######################################################################################


if __name__=='__main__':
    find=input('Ingrese la o las palabras clave de lo que quiere buscar: ')
    driver=bt.verificarDriver()
    fu.buscarImg(driver,find)    
    nImagenes=input('¿Cuantas imagenes desea descargar?: ')
    folderAddress=fu.checkFolder(find)

    fu.guardarImg(driver,int(nImagenes),folderAddress,find)

    input('LAS IMAGENES FUERON GUARDADES CON EXITO')
    
