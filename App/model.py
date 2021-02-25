import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
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
    cat = {'videos': None,
            'tags': None}
    if n == 1:
        cat['videos'] = lt.newList('ARRAY_LIST')
        cat['tags'] = lt.newList('ARRAY_LIST')
        return cat
    if n == 2:
        cat['videos'] = lt.newList('LINKED_LIST')
        cat['tags'] = lt.newList('LINKED_LIST')
        return cat
    else:
        cat['videos'] = lt.newList('ARRAY_LIST')
        cat['tags'] = lt.newList('ARRAY_LIST')
        return cat
   


# Funciones para agregar informacion al catalogo

def addV(catalog, video):
    lt.addLast(catalog['videos'], video)

def addT(catalog, tag):
    t = newT(tag['name'], tag['id'])
    lt.addLast(catalog['tags'], t)

# Funciones para creacion de datos

def newT(name, id):
    tag = {'name': '', 'T_id': ''}
    tag['name'] = name
    tag['T_id'] = id
    return tag
# Funciones de consulta
def getTendPais(catalogo, n, pais, orde):
    pais = pais.lower()
    if orde == 1:
        top = sortVideos(catalogo, n, cmpViews, shell)
    if orde == 2:
        top = sortVideos(catalogo, n, cmpViews, sel)
    if orde == 3:
        top = sortVideos(catalogo, n, cmpViews, ins)
 






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

def cmpPais(pais, p):
    if p['country'] == pais:
        return True
    else:
        return False
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

