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
    df = dat[dat.type == columna]
    nombre_grupo = folium.FeatureGroup(name = nombre_capa)
    HeatMap(data= df[["latitud","longitud"]], radius = 15).add_to(nombre_grupo)
    nombre_grupo.add_to(mapa)


def query_dist(local, distancia):

    san_francisco = [-122.42046743548889, 37.77203444922543]
    coord_point = {"type":"Point", "coordinates": san_francisco}
    
    cond = {"location":{"$near":{"$geometry":coord_point, "$maxDistance": distancia}}}
    query = local.find(cond)
    df = pd.DataFrame(list(query))
    
    return df