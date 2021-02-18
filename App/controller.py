

import config as cf
import model
import csv



# Inicialización del Catálogo de libros
def initCatalogo():
    catalogo = model.newCatalogo()
    return catalogo
# Funciones para la carga de datos

def loadDatos(catalogo):
 
    loadVideos(catalogo)
    loadCategorias(catalogo)
    loadTags(catalogo)
    sortVideos(catalogo)

def loadVideos(catalogo):
    
  
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videosfile in input_file:
        model.addVideo(catalogo, videosfile)

def loadCategorias(catalogo):
   
    tagsfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for categoria in input_file:
        model.addCategoria(catalogo, tagsfile)

def loadTags(catalogo):
    videostagsfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videostagsfile, encoding='utf-8'))
    for categoria in input_file:
        model.addTag(catalogo, videostagsfile)

# Funciones de ordenamiento
def sortVideos(catalogo):
   
    pass

# Funciones de consulta sobre el catálogo


def getTendenciaXpais(catalogo, country):
    
   pass

