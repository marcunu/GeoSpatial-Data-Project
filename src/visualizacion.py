import numpy as np


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
    delete = f"rm -rf {endopint}.zip"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Move the csv to uour data folder
    move_and_delete = f"mv *.csv data"
    return os.system(move_and_delete)


def cambio_minutos(valor):
    '''
    Change a time format string from HH:MM:SS to minutes integer
    '''
    try:
        horas = float(valor[0])*60
        minut = float(valor[2] + valor[3])
        seg = float(valor[5] + valor[6]) /60
        tiempo = round(horas + minut + seg, 2)
        return tiempo
    except:
        return np.nan