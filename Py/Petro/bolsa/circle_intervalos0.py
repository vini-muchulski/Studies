# -*- coding: utf-8 -*-
"""circle_intervalos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eaxr8nPaLZoTEVsSznWIPzlDc8NdKh0T

A função `np.linspace(start, stop, num)` do numpy gera uma sequência de números igualmente espaçados entre `start` (início) e `stop` (fim). O parâmetro `num` especifica o número de amostras a serem geradas.

No caso de `angulos = np.linspace(self.angulo_inicial, self.angulo_final, 100)`, a função está gerando 100 ângulos igualmente espaçados entre `self.angulo_inicial` e `self.angulo_final`.

Isso é útil para desenhar o círculo, pois permite calcular as coordenadas x e y para 100 pontos ao longo da circunferência do círculo, resultando em um desenho suave do círculo ou do arco do círculo.
"""

import numpy as np
import matplotlib.pyplot as plt

class Circulo:

    def __init__(self, raio, angulo_inicial, angulo_final, raio_deslocado=0, angulo_deslocado=0):
        self.raio = raio
        self.angulo_inicial = angulo_inicial
        self.angulo_final = angulo_final
        self.raio_deslocado = raio_deslocado
        self.angulo_deslocado = angulo_deslocado


    def comprimento_de_arco(self):
        s = np.pi * self.raio *((self.angulo_final- self.angulo_inicial)/180)
        return s

    def get_angulo(self):
        return np.radians((self.angulo_final- self.angulo_inicial))

    def get_raio(self):
        return self.raio

    def x_circle(self):
        angulos = np.linspace(self.angulo_inicial, self.angulo_final, 100) #gera 100 angulos dentro do intervalo

        x = self.raio * np.cos(np.radians(angulos)) + self.raio_deslocado * np.cos(np.radians(self.angulo_deslocado))
        #print(x)
        #print(angulos)

        return x

    def y_circle(self):
        angulos = np.linspace(self.angulo_inicial, self.angulo_final, 100)

        y = self.raio * np.sin(np.radians(angulos)) + self.raio_deslocado * np.sin(np.radians(self.angulo_deslocado))
        #print(y)
        #print(angulos)

        return y

circulo = Circulo(raio=4,angulo_inicial=0,angulo_final=180) # raio, ang inicial, angulo final

x = circulo.x_circle()
y = circulo.y_circle()

fig, ax = plt.subplots() #  cria uma nova figura com eixos
ax.plot(x, y, color="red") # plota o circulo

# traça a linha da origem até um ponto no círculo
ax.plot([0, x[-1]], [0, y[-1]], color='blue')

ax.axis('equal') # proporcao entre os eixos fica igual =  equal ou auto

plt.show()

circulo = Circulo(raio=4,angulo_inicial=0,angulo_final=180)

x = circulo.x_circle()
y = circulo.y_circle()




circle_ = plt.Circle((x,y),circulo.get_raio(),color="red",fill=False)

fig, ax = plt.subplots() # cria uma nova figura com eixos
#ax.add_patch(circle_) #eh usado para adicionar formas aos seus gráficos

plt.axis("auto")


#ax.plot([x, x - circulo.get_raio() ], [y, y - circulo.get_raio()], color='blue')
#ax.plot([0, x  ], [0, y ], color='blue')

circulo = Circulo(4, 0, 180)  # cria um círculo que vai de 0 a 180 graus

x = circulo.x_circle()
y = circulo.y_circle()

plt.plot(x, y, color="red")
plt.axis("equal")
plt.show()

circulo = Circulo(4,0,180)

x = circulo.x_circle()
y = circulo.y_circle()




circle_ = plt.plot(x,y,color="red")
plt.axis("equal")
fig, ax = plt.subplots() # cria uma nova figura com eixos




#ax.plot([x, x - circulo.get_raio() ], [y, y - circulo.get_raio()], color='blue')
#ax.plot([0, circulo.x  ], [0, circulo.x ], color='blue')



#plt.xticks(np.arange(min(x,0),10,step=1))
#plt.yticks(np.arange(min(y,0),10,step=1))

#plt.xticks([0,2,4,6,8])
#plt.yticks([0,2,4,6,8])

# plots the line from origin to a point on the circle
ax.plot([0, x[-1]], [0, y[-1]], color='blue')

ax.axis('equal') # ensures the aspect ratio is equal - auto

plt.show()