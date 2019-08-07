# Bars
import matplotlib.pyplot as pyplot

x = [1, 2, 3, 4, 5] # len(x): numero de barras; cada elemento: 1 barra!
y = [2, 3, 7, 1, 0]

pyplot.title("Gráfico de barras")
pyplot.xlabel("Eixo X")
pyplot.ylabel("Eixo Y")

pyplot.bar(x, y)
pyplot.show()
