

import config as cf
import model
import csv



# Inicialización del Catálogo de libros
def initCatalogo():
    catalogo = model.newCatalog()
    return catalogo
# Funciones para la carga de datos

def loadDatos(catalogo):
 
    loadvideos(catalogo)
    loadTags(catalogo)
    loadVideosTags(catalogo)
    sortVideos(catalogo)

def loadVideos(catalogo):
    
  
    videosfile = cf.data_dir + 'Data/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videosfile in input_file:
        model.addVideo(catalogo, video)

def loadTags(catalogo):
   
    tagsfile = cf.data_dir + 'Data/Category-id.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for categoria in input_file:
        model.addVideosTag(catalogo, video)

def loadVideosTags(catalogo):
    videostagsfile = cf.data_dir + 'Data/category-id.csv'
    input_file = csv.DictReader(open(videostagsfile, encoding='utf-8'))
    for categoria in input_file:
        model.addVideosTag(catalog, Videostag)

# Funciones de ordenamiento
def sortVideos(catalogo):
   
    pass

# Funciones de consulta sobre el catálogo


def getTendenciaXpais(catalogo, country):
    
   pass

