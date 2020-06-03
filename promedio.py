#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:35:18 2020

@author: san_raul
"""

name = input("Introduce el nombre del alumno:" )

x1 = float(input("Introduce la calificacion de materias: "))
x2 = float(input("Introduce la calificacion de materias: "))
x3 = float(input("Introduce la calificacion de materias: "))

prom_to = float((x1+x2+x3)/3) 

if prom_to > 7: 
    print(name, "pasó de año con ", prom_to)
else: 
    print(name, "Reprobó")

