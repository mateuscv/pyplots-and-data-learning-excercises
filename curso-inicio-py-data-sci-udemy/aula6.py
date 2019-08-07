# Comparador (Bar)

import matplotlib.pyplot as pyplot

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]


#Legendas
pyplot.title('Gráfico de barras "comparador"')
pyplot.xlabel("Eixo X")
pyplot.ylabel("Eixo Y")

pyplot.bar(x1, y1, label = "Grupo 1")
pyplot.bar(x2, y2, label = "Grupo 2")
pyplot.legend() # Mostrar legenda com os labels

pyplot.show()
