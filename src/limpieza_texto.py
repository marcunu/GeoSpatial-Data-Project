import geopy
from geopy.geocoders import Nominatim
import numpy as np
from functools import reduce
from pandas import json_normalize
import operator
import requests
import json
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

import src.limpieza_texto as lt

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)


def find_locations(tipo_sitio, limite, nuevo_nombre):
    
    '''
    This functions returns a json file with the location of the types of places desired.
    
    Parameters:
        -tipo_sitio: kind of place to search (F.E.: vegan)
        -limite: number of places we want.
        -Nuevo_nombre: name for the json file.
        
    '''

    tok1 = os.getenv("tok_id")
    tok2 = os.getenv("tok_s")

    san_francisco = {'type': 'Point', 'coordinates': [37.7579, -122.4192]}
    
    
    url_query = 'https://api.foursquare.com/v2/venues/explore'
    
    parametros = {
    "client_id": tok1,
    "client_secret": tok2,
    "v": "20180323",
    "ll": f"{san_francisco.get('coordinates')[0]},{san_francisco.get('coordinates')[1]}",
    "query": f"{tipo_sitio}", 
    "limit": limite    
    }
    
    resp = requests.get(url= url_query, params = parametros).json()
    
    decode = resp.get("response").get("groups")[0]
    
    json_normalize(decode)
    
    decode_otravez = decode.get("items")
    
    mapa_nombre =  ["venue", "name"]
    mapa_latitud = ["venue", "location", "lat"]
    mapa_longitud = ["venue", "location", "lng"]
    
    coord = []
    for dic in decode_otravez:
        paralista = {}
        paralista["name"] = lt.getFromDict(dic, mapa_nombre)
        paralista["latitud"]= lt.getFromDict(dic, mapa_latitud)
        paralista["longitud"] = lt.getFromDict(dic,mapa_longitud)
        coord.append(paralista)
        
    documentos = []
    for diccionario in coord:
        temporal = {
            "name" : diccionario.get("name"),
            "location" : {"type" : "Point", "coordinates" : [diccionario.get("longitud"),diccionario.get("latitud")]}
        }
        documentos.append(temporal)
        
    df = pd.DataFrame(documentos)
    
    df.to_json(f"./json/{nuevo_nombre}.json", orient = "records")

    return df

def lat(coord):
    return coord.get("coordinates")[0]

def lon(coord):
    return coord.get("coordinates")[1]