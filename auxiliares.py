import parametros as pa

def potencial(r1,r2):
    pot=pa.E/((abs(r1.thetha-r2.thetha))**pa.ALFA)