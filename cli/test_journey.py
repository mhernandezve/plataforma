import subprocess
import os
import os.path as paths

"""
vivas --cargar carpeta/
[-----------  70%]
yastá
hay x filas que podrían estar repetidas
el resultado está en carpeta/resultado.csv

vivas --reportar estadisticas
el resultado está en carpeta/datos-agregados.csv

vivas --reportar historias
el resultado está en carpeta/potenciales-historias.csv
(este resultado es del último mes)
"""

def test_stats_generation_jouney():
    cmd_load = './bin/python vivas.py --cargar -dir=target'
    out_load = subprocess.check_output(cmd_load, shell=True).decode("utf-8")
    assert out_load.strip('\n') == 'vivas> Carga finalizada. Ver target/resultado.csv'
    assert assert_exists('target/resultado.csv') == True

    cmd_report = './bin/python vivas.py --reportar estadisticas'
    out_report = subprocess.check_output(cmd_report, shell=True).decode("utf-8")
    assert out_report.strip('\n') == 'vivas> Ver target/estadisticas.csv'
    assert assert_exists('target/estadisticas.csv') == True

def assert_exists(file):
    return paths.isfile(file) and os.access(file, os.R_OK)
