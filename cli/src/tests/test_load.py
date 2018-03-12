from pytest import fixture
from pytest import raises

from context import load

@fixture
def teardown_resources():
    cedhu_file_name = './src/tests/resources/resultado.csv'
    if files.exists(cedhu_file_name):
        files.remove(cedhu_file_name)
    yield teardown_resources

def test_load_non_existent_dir():
    dir_path = './src/tests/not_existent'
    expected_message = 'El directorio ./src/tests/not_existent no existe'
    with raises(IOError, message=expected_message) as dir_not_found:
        load.load(dir_path)
    assert expected_message in str(dir_not_found.value)

def test_load_empty_directory():
    dir_path = './src/tests/empty'
    expected_message = 'El directorio ./src/tests/empty está vacío'
    with raises(IOError, message=expected_message) as empty_dir:
        load.load(dir_path)
    assert expected_message in str (empty_dir.value)

'''
def test_load_non_existent_file():
    dir_path = './src/tests/resources'
    expected_message = 'El archivo ./src/tests/resources/not_existent.xlsx no existe o no es posible leerlo'
    with raises(IOError, message=expected_message) as file_not_found:
        load.load(dir_path)
    assert expected_message in str(file_not_found.value)
'''
