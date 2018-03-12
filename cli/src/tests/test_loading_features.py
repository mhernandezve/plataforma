from pytest import raises
from context import files

"""
Dado el directorio 'resources' que contien los archivos para cargar
Cuando ejecuto la carga
Entonces obtengo el archivo resultado.csv en la misma carpeta
"""
def test_load_files_in_directory():
    dir_path = './src/tests/resources'
    load(dir_path)
    assert files.exists('./src/tests/resources/resultado.csv') == True

def test_load_non_existent_file():
    dir_path = './src/tests/not_existent'
    expected_message = 'El archivo ./src/tests/not_existent/cedhu.xlsx no existe o no es posible leerlo'
    with raises(IOError, message=expected_message) as file_not_found:
        load(dir_path)
    assert expected_message in str(file_not_found.value)

def load(dir_path):
    cedhu_file_name = '{dir}/cedhu.xlsx'.format(dir=dir_path)
    if not files.exists(cedhu_file_name):
        error_message = 'El archivo {file} no existe o no es posible leerlo'.format(file=cedhu_file_name)
        raise IOError(error_message)

    result_file_name = '{dir}/resultado.csv'.format(dir=dir_path)
    with open(result_file_name, 'w+') as file:
        file.write('\n')
    return True
