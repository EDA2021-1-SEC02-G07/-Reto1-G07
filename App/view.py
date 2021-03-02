import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
sys.setrecursionlimit(1000)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo.")
    print("2- Consultar los x videos con más views en tendencia por país.")
    print("3- Consultar video que más días ha sido tendencia por país.")
    print("4- Consultar video que más días ha sido tendencia por categoría.")
    print("5- Consultar los x videos con más likes por país con un tag.")
    print("0- Salir.")

def iniciarC(n):
    return controller.iniciarC(n)

def loadData(catalog):
    controller.loadData(catalog)

def printTendPais(pais):
    print('Los primeros 10 videos ordenados son: ')
    i = 1
    while i < 11:
        video =  lt.getElement(pais, i)
        print('Título: ' + video['title'] + ' Visitas: ' + video['views'])
        i +=1
def PVideoDiasXpais(pais):
    pass
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

#Menú principal

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        n = input('Presione 1 para Array List o presione 2 para Linked List: ')
        print("Cargando información de los archivos...")
        catalog = iniciarC(int(n))
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorías cargadas: ' + str(lt.size(catalog['categorias'])) + '\n')

    elif int(inputs[0]) == 2:
        n = int(input("\nNúmero de videos en tendencia: "))
        if lt.size(catalog['videos']) >= n:
            #pais = input("País en el que se desea buscar: ")
            pais = 'canada'
            orde = int(input('Presione 1 para ShellSort, 2 para SelectionSort, 3 para InsertionSort, 4 para MergeSort o 5 para QuickSort: '))
            print('\nCargando datos...\n')
            videos = controller.getTendPais(catalog, n, pais, orde)
            printTendPais(videos[1])
            print('\nPara la muestra de', n, 'elementos, el tiempo en msec es:', str(videos[0]) + '\n')

        else: 
            print('Número de tendencias excedido')
            sys.exit()
        
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
