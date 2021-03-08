from DISClib.DataStructures.arraylist import getElement, isPresent
import config as cf
import time
from DISClib.ADT import list as lt
import DISClib.DataStructures.listiterator as it
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

# Construccion de modelos
def NCatalogo():
    catalogo = {'videos': None,
            'categorias': None,
            'paises': None,
            'cat_vid': None}

    catalogo['videos'] = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    catalogo['categorias'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
    catalogo['paises'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
    catalogo['cat_vid'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
    return catalogo
   
# Funciones para agregar informacion al catalogo
def addV(catalog, video):
    lt.addLast(catalog['videos'], video)
    paises = video['country']
    categorias = video['category_id']
    addPais(catalog, paises, video)
    addCatVid(catalog, categorias, video)

def addCat(catalog, categoria):
    b = newCat(categoria['name'], categoria['id'])
    lt.addLast(catalog['categorias'], b)

def addPais(catalog, pais, video):
    paises = catalog['paises']
    posP = lt.isPresent(paises, pais)
    if posP > 0:
        paisN = lt.getElement(paises, posP)
    else:
        paisN = newP(pais)
        lt.addLast(paises, paisN)
    lt.addLast(paisN['videos'], video)

def addCatVid(catalog, cate, video):
    categorias = catalog['cat_vid']
    posC = lt.isPresent(categorias, cate)
    if posC > 0:
        catN = lt.getElement(categorias, posC)
    else:
        catN = newP(cate)
        lt.addLast(categorias, catN)
    lt.addLast(catN['videos'], video)

# Funciones para creacion de datos
def newCat(name, id):
    cat = {'nombre': '', 'cat_id': ''}
    cat['nombre'] = name
    cat['cat_id'] = id
    return cat

def newP(name):
    pais = {'nombre': '', 'videos': None}
    pais['nombre'] = name
    pais['videos'] = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    return pais

# Funciones de consulta
def TendPais(catalogo, pais, cate):
    pais = pais.lower()
    cate = cate.lower()
    ide = getID(catalogo, cate)
    paises = getLtPais(catalogo, pais)
    categorias = getltCat(catalogo, ide['cat_id'])
    pCheat = []
    cCheat = []
    final = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    iterator = it.newIterator(paises['videos'])
    while it.hasNext(iterator):
        x = it.next(iterator)
        x = frozenset(x.items())
        pCheat.append(x)
    iterator = it.newIterator(categorias['videos'])
    while it.hasNext(iterator):
        x = it.next(iterator)
        x = frozenset(x.items())
        cCheat.append(x)
    if len(pCheat) < len(cCheat):
        SuperCheat = list(set(pCheat).intersection(cCheat))
    else:
        SuperCheat = list(set(cCheat).intersection(pCheat))
    for x in SuperCheat:
        lt.addLast(final, dict(x))
    top = sortVideos(final, cmpViews, quick)
    return top

def DiasPais(catalogo, pais):
    pass

def DiasCat(catalogo, categoria):
    cat = categoria.lower()
    c_id = getID(catalogo, cat)
    videos = getltCat(catalogo, c_id['cat_id'])
    #Para usar videos hay que usar videos['videos']
    cont = {}
    iterator = it.newIterator(videos['videos'])
    while it.hasNext(iterator):
        x = it.next(iterator)
        if x['video_id'] in cont:
            cont[x['video_id']] +=1
        else:
            cont[x['video_id']] = 1
    if '#NAME?' in cont:
        cont.pop('#NAME?')     
    v_id = list(cont.keys())
    days = list(cont.values())
    id_max = v_id[days.index(max(days))]
    return lt.getElement(videos['videos'], lt.isPresent(videos['videos'], id_max)), max(days)

def LikesTag(catalogo, tag):
    videos = catalogo['videos']
    tag = tag.lower()
    iterator = it.newIterator(videos)
    likes = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    while it.hasNext(iterator):
        x = it.next(iterator)
        if tag in x['tags'].lower():
            lt.addLast(likes, x)
    topDup = sortVideos(likes, cmpLikes, quick)
    top = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    iterator = it.newIterator(topDup)
    vidIDs = set()
    while it.hasNext(iterator):
        x = it.next(iterator)
        if x['video_id'] not in vidIDs:
            lt.addLast(top, x)
            vidIDs.add(x['video_id'])
    return top

# Funciones adicionales
def getLtPais(catalogo, pais):
    pos = lt.isPresent(catalogo['paises'], pais)
    if pos != 0:
        videos = lt.getElement(catalogo['paises'], pos)
        return videos

def getID(catalogo, cate):
    pos = lt.isPresent(catalogo['categorias'], cate)
    if pos != 0:
        ide = getElement(catalogo['categorias'], pos)
        return ide

def getltCat(catalogo, c_id):
    pos = lt.isPresent(catalogo['cat_vid'], c_id)
    if pos != 0:
        videos = lt.getElement(catalogo['cat_vid'], pos)
        return videos

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpViews(v1, v2):
    result = float(v1['views']) > float(v2['views'])
    return result

def cmpPais(name, pais):
    if (name.lower() in pais['nombre'].lower()):
        return 0
    return -1

def cmpV_id(name, vid):
    if (name.lower() in vid['video_id'].lower()):
        return 0
    return -1

def cmpLikes(v1, v2):
    result = float(v1['likes']) > float(v2['likes'])
    return result

# Funciones de ordenamiento
def sortVideos(lista, cmp_f, orde):
    lista = lista.copy()
    orde.sort(lista, cmp_f)
    return lista

#DEBUG
def debug(catalogo):
    '''Para que el computador no muera hay que hacer un break en
    controller.py con la cantidad de archivos deseados.'''
    print('\n', '\033[30m', '\033[1m', '\033[103m', 'No se han configurado opciones de debug.', '\033[0m', '\n')
    #print(catalogo['videos'])
    #print(catalogo['cat_vid'])
    #print(catalogo['paises'])
    #print(catalogo['categorias'])
    #print(lt.getElement(catalogo['paises'], 1))
    #print(lt.getElement(catalogo['cat_vid'], 1))
    