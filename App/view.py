import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo.")
    print("2- Consultar los x videos que son tendencia por país.")
    print("3- Consultar video que más días ha sido tendencia por país.")
    print("4- Consultar video que más días ha sido tendencia por categoría.")
    print("5- Consultar los x videos con más likes por país con un tag.")
    print("0- Salir.")

def initCatalogo():
    return controller.initCatalogo()

def loadDatos(catalog):
    controller.loadDatos(catalog)

def PTendenciaXpais(pais):
    if pais:
        print("Estos son los videos en tendencia en " + str(pais))
    else:
        print('País incorrecto')
def PVideoDiasXpais(pais):
    if pais:
        print("Este es el video con más días en tendencia en " + str(pais))
    else:
        print('País incorrecto')
def PVideoDiasXcat(categoria):
    if categoria:
        print("Este es el video con más días en tendencia en la categoría" + str(categoria))
    else:
        print('Categoría no encontrada')
def PMasLikesXtag(tag):
    if pais:
        print("Este es el video con más likes con la tag " + str(tag))
    else:
        print('Tag no econtrada')

catalog = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalogo()
        loadDatos(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['video_id'])))
        print('Categorías cargadas: ' + str(lt.size(catalog['category_id'])))
        print('Tags cargadas: ' + str(lt.size(catalog['tags'])))

    elif int(inputs[0]) == 2:
        n = input("Número de videos en tendencia: ")
        pais = input("País en el que se desea buscar: ")
        cat = input("Categoría que se desea buscar: ")
        videos = controller.getTendenciaXpais(catalog, int(n), pais, cat)
        PTendenciaXpais(videos)

    elif int(inputs[0]) == 3:
        n = input("País para consultar tendencia: ")
        videos = controller.getVideoDiasXpais(catalog, int(n))
        PVideoDiasXpais(videos)

    elif int(inputs[0]) == 4:
        n = input("Categoría para consultar tendencia: ")
        videos = controller.getVideoDiasXcat(catalog, int(n))
        PVideoDiasXcat(videos)

    elif int(inputs[0]) == 5:
        n = input("Tag para consultar videos con más likes: ")
        videos = controller.getMasLikesXtag(catalog, int(n))
        PMasLikesXtag(videos)

    else:
        sys.exit(0)
sys.exit(0)
