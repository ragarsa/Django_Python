#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:02:19 2020

@author: san_raul
"""

name = input("Introduce el nombre de la persona: ")

age = int(input("Introduce la edad de la persona: "))


if age < 6: 
    print(name, "Está en maternal")
elif age <= 6 and age > 12:
    print("Está en primaria")
elif age <= 12 and age > 15:
    print(name, "Está en secundaria")
elif age <= 15 and age < 18:
    print(name, "Está en preparatoria")
elif age <= 18 and age < 23:
    print(name, "Está en universidad")
else: 
    print(name, "Es profesional")