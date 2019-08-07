import matplotlib.pyplot as pyplot

x = [1,3,5,7,9]
y = [2,3,7,1,0]
markersSize = [20, 5, 100, 33, 10]

pyplot.title("Scatterplot")
pyplot.xlabel("Eixo X")
pyplot.ylabel("Eixo Y")

pyplot.plot(x, y, color="#FF0000", ls="--") # hexa colors: 2 chars red, 2 green, 2 blue; ls: linestyle
pyplot.scatter(x, y, label="Meus pontos", color="blue", marker="o", s=markersSize) # s: size
pyplot.legend()
#pyplot.grid()
pyplot.show()
