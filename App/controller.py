import config as cf
import model
import csv

def iniciarC(n):
    cat = model.NCatalogo(n)
    return cat

# Funciones para la carga de datos

def loadData(catalogo):

    loadV(catalogo)
    loadT(catalogo)

def loadV(catalogo):

    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videosfile in input_file:
        model.addV(catalogo, videosfile)

def loadT(catalogo):
   
    tagsfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'), delimiter = '\t')
    for tag in input_file:
        model.addT(catalogo, tag)

# Funciones de ordenamiento
def sortVideos(catalogo):
   return model.sortVideos(catalogo)

# Funciones de consulta sobre el catálogo
def getTendPais(catalogo, n, pais, orde):
    
    tendencia = model.getTendPais(catalogo, n, pais, orde)
    return tendencia










