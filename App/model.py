import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas:
una para los videos y otra para los tags.
"""

# Construccion de modelos
def NCatalogo(n):
    #Lista de países como author en el ejemplo.
    #Link categorías con países.
    #Se pueden hacer más listas en la pre-carga.
    #Tags, delimeter = |, que apunta a los videos. Toca cambiar el nombre de las categorías. Bien jugado, Mario.
    catalogo = {'videos': None,
            'categorias': None,
            'paises': None}
    if n == 1:
        catalogo['videos'] = lt.newList('ARRAY_LIST')
        catalogo['categorias'] = lt.newList('ARRAY_LIST')
        catalogo['paises'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
        
        return catalogo
    if n == 2:
        catalogo['videos'] = lt.newList('SINGLE_LINKED')
        catalogo['categorias'] = lt.newList('SINGLE_LINKED')
        catalogo['paises'] = lt.newList('SINGLE_LINKED', cmpfunction = cmpPais)
        return catalogo
    else:
        catalogo['videos'] = lt.newList('ARRAY_LIST')
        catalogo['categorias'] = lt.newList('ARRAY_LIST')
        catalogo['paises'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
        return catalogo
   


# Funciones para agregar informacion al catalogo

def addV(catalog, video):
    lt.addLast(catalog['videos'], video)
    paises = video['country']
    addPais(catalog, paises, video)
    
def addCat(catalog, categoria):
    t = newCat(categoria['name'], categoria['id'])
    lt.addLast(catalog['categorias'], t)

def addPais(catalog, pais, video):
    paises = catalog['paises']
    posP = lt.isPresent(paises, pais)
    if posP > 0:
        paisN = lt.getElement(paises, posP)
    else:
        paisN = newP(pais)
        lt.addLast(paises, paisN)
    lt.addLast(paisN['videos'], video)

# Funciones para creacion de datos

def newCat(name, id):
    cat = {'name': '', 'Cat_id': ''}
    cat['name'] = name
    cat['Cat_id'] = id
    return cat

def newP(name):
    pais = {'nombre': '', 'videos': None}
    pais['nombre'] = name
    pais['videos'] = lt.newList('ARRAY_LIST')
    return pais

# Funciones de consulta

def getTendPais(catalogo, n, pais, orde):
    pais = pais.lower()
    if orde == 1:
        top = sortVideos(catalogo, n, cmpViews, shell)
    if orde == 2:
        top = sortVideos(catalogo, n, cmpViews, sel)
    if orde == 3:
        top = sortVideos(catalogo, n, cmpViews, ins)
    if orde == 4:
        top = sortVideos(catalogo, n, cmpViews, merge)
    if orde == 5:
        top = sortVideos(catalogo, n, cmpViews, quick)
    else:
        top = sortVideos(catalogo, n, cmpViews, shell)
 






    #result = []
    #t1 = time.process_time()
    #for x in top[1]['elements']:
    #   if cmpPais(pais, x) == True:
    #      result.append({'Título': x['title'], 'Visitas': x['views'], 'País': x['country']})
    #t2 = time.process_time()
    #t = top[0] + (t2 - t1)
    return top

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpViews(v1, v2):
    result = float(v1['views']) > float(v2['views'])
    return result

def cmpPais(name, pais):
    if (name.lower() in pais['nombre'].lower()):
        return 0
    return -1

def cmpTags(name, tag):
    if (name.lower() in tag['tags'].lower()):
        return 0
    return -1
# Funciones de ordenamiento

def sortVideos(catalogo, size, cmp_f, orde):
    sort_t = None
    sub = lt.subList(catalogo['videos'], 1, size)
    sub = sub.copy()
    start_t = time.process_time()
    orde.sort(sub, cmp_f)
    stop_t = time.process_time()
    time_f = (stop_t - start_t) *1000

    return time_f, sub

