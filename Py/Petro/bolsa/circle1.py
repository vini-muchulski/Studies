import numpy as np

class Circle:

    def __init__(self,raio,angulo,raio_deslocado,angulo_deslocado):
        self.raio = raio
        self.angulo = angulo
        self.raio_deslocado = raio_deslocado
        self.angulo_deslocado = angulo_deslocado

    def comprimento_de_arco(self):
        s = np.pi * self.raio *(self.angulo/180)
        return s
    
    def get_angulo(self):
        return self.angulo
    
    def get_raio(self):
        return self.raio
    
    def x_circle(self):
        x = self.raio * np.cos(self.angulo) + self.raio_deslocado * np.cos(self.angulo_deslocado)

        return x
    
    def y_circle(self):
        y = self.raio * np.sin(self.angulo) + self.raio_deslocado * np.sin(self.angulo_deslocado)

        return y
    
    
    

    
circulo = Circle(1,57.8) # 1 radiano aprox = 57,8 graus

arco = circulo.comprimento_de_arco()

print(arco)
    

