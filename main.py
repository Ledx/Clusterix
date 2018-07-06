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
import movilidad
import parametros

for x in [-1, 0, 1]:
    print(lobulo.lobuloEliptico(x))