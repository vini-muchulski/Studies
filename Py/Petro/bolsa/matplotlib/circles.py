import numpy as np
import matplotlib.pyplot as plt


class Circulo:

    def __init__(self,raio,angulo,raio_deslocado=0,angulo_deslocado=0):
        self.raio = raio
        self.angulo = angulo
        self.raio_deslocado = raio_deslocado
        self.angulo_deslocado = angulo_deslocado

    def comprimento_de_arco(self):
        s = np.pi * self.raio *(self.angulo/180)
        return s

    def get_angulo(self):
        return np.radians(self.angulo
)
    def get_raio(self):
        return self.raio

    def x_circle(self):
        x = self.raio * np.cos(np.radians(self.angulo)) + self.raio_deslocado * np.cos(np.radians(self.angulo_deslocado))

        return x

    def y_circle(self):
        y = self.raio * np.sin(np.radians(self.angulo)) + self.raio_deslocado * np.sin(np.radians(self.angulo_deslocado))

        return y





circulo = Circulo(4,30)

x = circulo.x_circle()
y = circulo.y_circle()




circle_ = plt.Circle((x,y),circulo.get_raio(),color="red",fill=False)

fig, ax = plt.subplots() # cria uma nova figura com eixos
ax.add_patch(circle_) #eh usado para adicionar formas aos seus gráficos

plt.axis("auto")


#ax.plot([x, x - circulo.get_raio() ], [y, y - circulo.get_raio()], color='blue')
ax.plot([0, x  ], [0, y ], color='blue')

#plt.xticks(np.arange(min(x,0),10,step=1))
#plt.yticks(np.arange(min(y,0),10,step=1))

#plt.xticks([0,2,4,6,8])
#plt.yticks([0,2,4,6,8])



plt.show()