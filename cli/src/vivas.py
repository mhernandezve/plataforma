#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from clint.arguments import Args 
from clint.textui import puts, colored, indent

def create_file(name):
    with open(name, 'w+') as file:
        file.write('\n')

args = Args()

if args.flags[0] == '--cargar':
    with indent(4, quote='vivas> '):
        puts('Carga finalizada. Ver target/resultado.csv')
        create_file('target/resultado.csv')

if args.flags[0] == '--reportar':
    with indent(4, quote='vivas> '):
        puts('Ver target/estadisticas.csv')
        create_file('target/estadisticas.csv')

print()
