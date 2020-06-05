# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:39:27 2020

@author: gpeiro
"""


# Plantilla de preprocesado

# Como importar las librerias 

# numpy es la libreria basica de python para el tratamiento matematico
# la importa con el alias np 
import numpy as np

# importamos la sublibreria es decir no toda la libreria esta enfocado a la 
# representacion grafica
import matplotlib.pyplot as plt

# libreria para la carga de datos desde csv xml ... y su manipulacion 
import pandas as pd


# importamos el dataset
dataset = pd.read_csv("Data.csv")

# se separa en parte independiente
# iloc index localitation selecciono las filas y columnas con el : selecciono todo 
# 0:9 del 0 al 9 o si es todo : para coget odo menos la ultima :-1
# con .values solo cojo valores no las posiciones
# convencion mayusculas matrices minusculas vectores
X = dataset.iloc[:,:-1].values

# vector dependiente
y = dataset.iloc[:,3].values