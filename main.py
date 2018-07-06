################################################################################
#Universidad Nacional Autónoma de México
#Instituto de Ciencias Nucleares
################################################################################
#Programa: COLMENA
#Director: Dr. Gustavo Adolfo Medina Tanco
################################################################################
#Simulador de formacion de clusters de elementos dispersos en un área arbitraria
################################################################################
#Desarrollador: Ing. Led Eduardo Ruvalcaba Tamés
################################################################################
#Actualizado 07/06/18 0029 hrs UTC-6
################################################################################

import numpy as np
import lobulo
import Iteracion as It
import parametros as pa


def simulacion():
    iteracion = It.Iteracion()
    for x in range(0, pa.NumeroCorridas):
        iteracion.corrida()


simulacion()
