import matplotlib.pyplot as plt
import random

vetor = []
for i in range(20):
    vetor.append(random.randint(0,50000))
plt.boxplot(vetor)
plt.title("BoxPlot")
plt.show()