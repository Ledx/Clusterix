import parametros
import math as m

def giro(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

def avance(x,i):
    x[i].posicion[0] += parametros.PASO * m.cos((x[i].thetha * (m.PI / 180)));
    x[i].posicion[1] += parametros.PASO * m.sin((x[i].thetha * (m.PI / 180)));