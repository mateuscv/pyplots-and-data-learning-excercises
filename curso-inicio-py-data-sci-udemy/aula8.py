import matplotlib.pyplot as pyplot

x = [1,3,5,7,9]
y = [2,3,7,1,0]

pyplot.title("Scatterplot")
pyplot.xlabel("Eixo X")
pyplot.ylabel("Eixo Y")

pyplot.plot(x, y, color="red", ls=":") # ls: linestyle
pyplot.scatter(x, y, label="Meus pontos", color="blue", marker="o", s=50) # s: size
pyplot.legend()
#pyplot.grid()
pyplot.show()
