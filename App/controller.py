import config as cf
import model
import csv

def iniciarC():
    catalogo = model.NCatalogo()
    return catalogo

# Funciones para la carga de datos

def loadData(catalogo):

    loadV(catalogo)
    loadCat(catalogo)

def loadV(catalogo):

    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))

    for videosfile in input_file:
        model.addV(catalogo, videosfile)
    
    
def loadCat(catalogo):
   
    catfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(catfile, encoding='utf-8'), delimiter = '\t')
    for cat in input_file:
        model.addCat(catalogo, cat)

# Funciones de ordenamiento
def sortVideos(catalogo):
   return model.sortVideos(catalogo)

# Funciones de consulta sobre el catálogo
def getTendPais(catalogo, pais, cate):
    tendencia = model.getTendPais(catalogo, pais, cate)
    return tendencia










