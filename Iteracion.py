import Robot as R
import parametros as pa


class Iteracion:
    def corrida(self):
        robots = []
        for x in range(0, pa.NumeroRobots):
            r = R.Robot()
            robots.append(r)
        print (robots)