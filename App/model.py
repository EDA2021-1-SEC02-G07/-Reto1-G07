import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalogo():

    catalogo = {'videos': None,
               'categorias': None,
               'tags': None}

    catalogo['videos'] = lt.newList()
    catalogo['categorias'] = lt.newList('ARRAY_LIST')
    catalogo['tags'] = lt.newList('ARRAY_LIST')

    return catalogo

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategoria(catalog, categoria):
    lt.addLast(catalog['categorias'], categoria)

def addTag(catalog, tag):
    lt.addLast(catalog['tags'], tag)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento