from context import files

def load(dir_path):
    if not files.exists(dir_path):
        error_message = 'El directorio {dir} no existe'.format(dir=dir_path)
        raise IOError(error_message)

    if files.is_empty(dir_path):
        error_message = 'El directorio {dir} está vacío'.format(dir=dir_path)
        raise IOError(error_message)

    cedhu_file_name = '{dir}/cedhu.xlsx'.format(dir=dir_path)
    if not files.exists(cedhu_file_name):
        error_message = 'El archivo {file} no existe o no es posible leerlo'.format(file=cedhu_file_name)
        raise IOError(error_message)

    result_file_name = '{dir}/resultado.csv'.format(dir=dir_path)
    with open(result_file_name, 'w+') as file:
        file.write('\n')
    return True
