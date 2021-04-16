import geopy
from geopy.geocoders import Nominatim
import numpy as np

def ciudad(lon_lat):

    '''
    This function returns take the latitude and longitude and returns the name of the city.

    Atributtes:
        -lon_lat: longitude and latitude.

    '''
    locator = Nominatim(user_agent="myGeocoder")
    coord = lon_lat
    rgeocode = locator.reverse(coord)
    info = rgeocode.raw
    city = info ['address']['city']
    return city

def comunidad(lon_lat):
    '''
    This function returns take the latitude and longitude and returns the name of the state.

    Atributtes:
        -lon_lat: longitude and latitude.
        
    '''
    locator = Nominatim(user_agent="myGeocoder")    
    coord = lon_lat
    rgeocode = locator.reverse(coord)
    info = rgeocode.raw
    comu = info ['address']['state']
    return comu

def pais(lon_lat):
    
    '''
    This function returns take the latitude and longitude and returns the name of the country.

    Atributtes:
        -lon_lat: longitude and latitude.
        
    '''
    locator = Nominatim(user_agent="myGeocoder")
    coord = lon_lat
    rgeocode = locator.reverse(coord)
    info = rgeocode.raw
    pais = info ['address']['country']
    return pais

def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded and unzipped csv
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]

    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}"
    decompress = f"tar -xzvf {endopint}.zip"
    delete = f"del {endopint}.zip"
 
    for i in [download, decompress, delete]:
        os.system(i)
    
    #Move the csv to uour data folder
    move_and_delete = "move hkm.csv data/"
    return os.system(move_and_delete)