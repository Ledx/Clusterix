from numpy import array
import parametros
import math as m

class Robot:
    def __init__(self):
        self.thetha = 0
        self.radio = 0.5
        self.posicion = array(2)
        self.pasos = 0
        self.carga=100
        self.clustered = 0
        self.clase = 1
        self.vecindad = []

    def giro(self,thetha):
        self.thetha = thetha

    def avance(self):
        self.posicion[0] += parametros.PASO * m.cos((self.thetha * (m.PI / 180)));
        self.posicion[1] += parametros.PASO * m.sin((self.thetha * (m.PI / 180)));