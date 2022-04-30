import inicializar as bt
import funciones_utiles as fu
import pyinputplus

######################################################################
#                           PENDIENTES
# 1-Eliminar los mensajes de error
# 2-Cerrar el driver cuando finalice el script                        
#
#######################################################################


if __name__=='__main__':
    find=input('Ingrese la o las palabras clave de lo que quiere buscar: ')
    driver=bt.verificarDriver()
    fu.buscarImg(driver,find)    
    #solo numeros enteros
    nImagenes=pyinputplus.inputInt('¿Cuantas imagenes desea descargar?: ')

    #carpeta nueva o una existente?
    yn=pyinputplus.inputYesNo('¿Quiere guardar las imagenes en un folder especifico? [Y/N]: ')
    
    if yn=='no': folderAddress=fu.checkFolder(find)
    else: 
        folderAddress=input('Ingrese la dirección de la carpeta destino: ')
    
    folderAddress=folderAddress.replace('"','')        
    folderAddress=r'{}'.format(folderAddress)    
     
    fu.guardarImg(driver,int(nImagenes),folderAddress,find)

    input('LAS IMAGENES FUERON GUARDADES CON EXITO')
    
