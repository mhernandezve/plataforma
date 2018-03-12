import subprocess

from context import files

"""
vivas --cargar carpeta/
[-----------  70%]
yastá
hay x filas que podrían estar repetidast
el resultado está en carpeta/resultado.csv

vivas --reportar estadisticas
el resultado está en carpeta/datos-agregados.csv

vivas --reportar historias
el resultado está en carpeta/potenciales-historias.csv
(este resultado es del último mes)
"""

def test_stats_generation_jouney():
    cmd_load = './bin/python src/vivas.py --cargar -dir=target'
    out_load = subprocess.check_output(cmd_load, shell=True).decode("utf-8")
    assert out_load.strip('\n') == 'vivas> Carga finalizada. Ver target/resultado.csv'
    assert files.exists('target/resultado.csv') == True

    cmd_report = './bin/python src/vivas.py --reportar estadisticas'
    out_report = subprocess.check_output(cmd_report, shell=True).decode("utf-8")
    assert out_report.strip('\n') == 'vivas> Ver target/estadisticas.csv'
    assert files.exists('target/estadisticas.csv') == True

