import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
sys.setrecursionlimit(1000000)
class text:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    BLUE = '\033[34m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def printMenu():
    print(text.CYAN + "\nBienvenido" + text.END)
    print(text.BLUE + "1- Cargar información en el catálogo.")
    print("2- Consultar los n videos con más views en tendencia por país.")
    print("3- Consultar video que más días ha sido tendencia por país.")
    print("4- Consultar video que más días ha sido tendencia por categoría.")
    print("5- Consultar los n videos con más likes por país con un tag.")
    print("0- Salir." + text.END)

def iniciarC():
    return controller.iniciarC()

def loadData(catalog):
    controller.loadData(catalog)

def printTendPais(videos, n, pais):
    if lt.size(videos) != 0:
        if lt.size(videos) >= n:
            print('Los primeros ' + str(n) +  ' videos ordenados de', str(pais).capitalize(), 'son: ')
            i = 1
            while i < (n + 1):
                video =  lt.getElement(videos, i)
                print(text.UNDERLINE + text.YELLOW + str(i) + '.',
                'Fecha en tendencia:' + text.END, video['trending_date'],
                text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video['title'],
                text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video['channel_title'],
                text.YELLOW + text.UNDERLINE + 'Hora de publicación:' + text.END, video['publish_time'],
                text.YELLOW + text.UNDERLINE + 'Visitas:' + text.END, video['views'],
                text.YELLOW + text.UNDERLINE + 'Likes:' + text.END, video['likes'],
                text.YELLOW + text.UNDERLINE + 'Dislikes:' + text.END, video['dislikes'])
                
                i +=1
        else:
            print(text.RED + '\nSolo hay', str(n), 'videos que cumplen con los criterios de búsqueda: ' +
                text.END)
            i = 1
            while i < (lt.size(videos) + 1):
                video =  lt.getElement(videos, i)
                print(text.UNDERLINE + text.YELLOW + str(i) + '.',
                'Fecha en tendencia:' + text.END, video['trending_date'],
                text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video['title'],
                text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video['channel_title'],
                text.YELLOW + text.UNDERLINE + 'Hora de publicación:' + text.END, video['publish_time'],
                text.YELLOW + text.UNDERLINE + 'Visitas:' + text.END, video['views'],
                text.YELLOW + text.UNDERLINE + 'Likes:' + text.END, video['likes'],
                text.YELLOW + text.UNDERLINE + 'Dislikes:' + text.END, video['dislikes'])
                    
                i +=1
    else:
        print(text.RED + '\nNo hay videos que cumplan con los criterios de búsqueda.\n' + text.END)
        sys.exit()

def printDiasPais(video, pais):
    print('El video con más días en tendencia en el país', pais, 'es: ')
    print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video[0]['title'],
    text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video[0]['channel_title'],
    text.YELLOW + text.UNDERLINE + 'Categoría:' + text.END, video[0]['category_id'],
    text.YELLOW + text.UNDERLINE + 'Número de días:' + text.END, video[1])

def printDiasCat(video, cat):
    print('El video con más días en tendencia en la categoría', cat, 'es: ')
    print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video[0]['title'],
    text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video[0]['channel_title'],
    text.YELLOW + text.UNDERLINE + 'Categoría:' + text.END, video[0]['category_id'],
    text.YELLOW + text.UNDERLINE + 'Número de días:' + text.END, video[1])

def printLikesTag(video, tag):
    print('El video con más días en tendencia en el tag', tag, 'es: ')
    print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video[0]['title'],
    text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video[0]['channel_title'],
    text.YELLOW + text.UNDERLINE + 'Categoría:' + text.END, video[0]['category_id'],
    text.YELLOW + text.UNDERLINE + 'Número de días:' + text.END, video[1])

catalog = None

#Menú principal
while True:
    printMenu()
    inputs = input(text.YELLOW + 'Seleccione una opción para continuar\n' + text.END)
    if int(inputs[0]) == 1:
        print(text.PURPLE + "Cargando información de los archivos..." + text.END)
        catalog = iniciarC()
        loadData(catalog)
        print(text.UNDERLINE + text.BOLD + 'Videos cargados:' + text.END + ' ',
        str(lt.size(catalog['videos'])))
        print( text.UNDERLINE + text.BOLD + 'Categorías cargadas:' +text.END + ' ',
        str(lt.size(catalog['categorias'])) + '\n')

    elif int(inputs[0]) == 2:
        n = int(input("\nNúmero de los top videos que desea consultar: "))
        if lt.size(catalog['videos']) >= n:
            pais = input('Escriba el país en el que desee consultar las tendencias: ')
            if lt.isPresent(catalog['paises'], pais) != 0:
                cate = input('Escriba el nombre de la categoría que desea consultar: ')
                if lt.isPresent(catalog['categorias'], cate) != 0:
                    print(text.PURPLE + '\nCargando datos...\n' + text.END)
                    videos = controller.getTendPais(catalog, pais, cate)
                    printTendPais(videos, n, pais)
                else:
                    print(text.RED + '\nCategoría no encontrada.\n' + text.END)
                    sys.exit()
            else:
                print(text.RED + '\nPaís no encontrado.\n' + text.END)
                sys.exit()

        else: 
            print(text.RED + '\nNúmero de tendencias excedido.\n' + text.END)
            sys.exit()
        
    elif int(inputs[0]) == 3:
        p = input("País: ")
        if lt.isPresent(catalog['paises'], p) != 0:
            print(text.PURPLE + '\nCargando datos...\n' + text.END)
            video = controller.getDiasPais(catalog, p)
            printDiasPais(video, p)
        else:
            print(text.RED + '\nPaís no encontrado.\n' + text.END)
            sys.exit()
        

    elif int(inputs[0]) == 4:
        c = input("Categoría: ")
        if lt.isPresent(catalog['categorias'], c) != 0:
            print(text.PURPLE + '\nCargando datos...\n' + text.END)
            video = controller.getDiasCat(catalog, c)
            printDiasCat(video, c)
        else:
            print(text.RED + '\nCategoría no encontrada.\n' + text.END)
            sys.exit()

    elif int(inputs[0]) == 5:
        t = input("Tag: ")
        video = controller.getLikesTag(catalog, t)
        printLikesTag(video, t)

    else:
        sys.exit(0)
sys.exit(0)
