import numpy as np
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd


def markers(dataframe, etiqueta, icono, color_f, color_i):
    
    '''
    This functions make markers with the selected dataframe.
    
    Parameters:
        -DataFrame: the dataframe with the location.
        -Etiqueta: name for the label.
        -icon: the shape of the icon.
        -color_f: background color.
        -Color_i: color for the icon.
        
    '''
    
    df = dataframe
    
    for i in df["location"]:
        dicc = {
            "location" : [i.get("coordinates")[1], i.get("coordinates")[0]],
            "tooltip" : etiqueta        
        }
    
        ic = Icon (color = color_f,
                prefix = "fa",
                icon = icono,
                icon_color = color_i)
    
        Marker(**dicc, icon = ic).add_to(san_f)


def heat_map(columna, dat, nombre_grupo, nombre_capa, mapa):
    '''
    This function creates a heat map
    parameters:
        -columna: column from the dataframe 
        -dat: dataframe
        -nombre_grupo: name for the group to create.
        -nomber capa: layer name
        -mapa: map where the layer is going to be added.
    '''
    df = dat[dat.type == columna]
    nombre_grupo = folium.FeatureGroup(name = nombre_capa)
    HeatMap(data= df[["latitud","longitud"]], radius = 15).add_to(nombre_grupo)
    nombre_grupo.add_to(mapa)


def query_dist(local, distancia):
    '''
    this function returns the companies that are in the desired radius.

    Parameters:
        -Local: type of company
        -Distancia: max distance

    '''

    san_francisco = [-122.40651979413546, 37.76528668651395]
    coord_point = {"type":"Point", "coordinates": san_francisco}
    
    cond = {"location":{"$near":{"$geometry":coord_point, "$maxDistance": distancia}}}
    query = local.find(cond)
    df = pd.DataFrame(list(query))
    
    return df