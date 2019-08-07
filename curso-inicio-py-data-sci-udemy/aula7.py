#Scatterplot
import matplotlib.pyplot as pyplot

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

pyplot.title("Scatterplot c/ linha")
pyplot.xlabel("Eixo X")
pyplot.ylabel("Eixo Y")

pyplot.scatter(x, y, label="Meus pontos", color="red")
pyplot.plot(x,y)
pyplot.legend() # Mostrar legenda com os labels
pyplot.show()
