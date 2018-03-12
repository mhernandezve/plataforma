from context import load
from context import files

"""
Dado el directorio 'resources' que contie los archivos para cargar
Cuando ejecuto la carga
Entonces obtengo el archivo resultado.csv en la misma carpeta
"""
def test_load_files_in_directory():
    dir_path = './src/tests/resources'
    load.load(dir_path)
    assert files.exists('./src/tests/resources/resultado.csv') == True
