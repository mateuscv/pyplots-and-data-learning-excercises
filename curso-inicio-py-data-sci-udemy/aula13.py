# Crescimento da População 1980 ~ 2016 (Datasus)

import matplotlib.pyplot as plt
#from matplotlib.ticker import StrMethodFormatter

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0: # skip header
        linha = dados[i].split(",")
        x.append(int(linha[0])) # preenche anos
        y.append(int(linha[1])) # preenche pop

plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color="#991a1a", ls="--")
plt.xticks(range(min(x), max(x)+1, 3)) # coloca ticks em intervalo determinado
#plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
plt.title("Crescimento da População 1980 ~ 2016 (Datasus)")
plt.xlabel("Ano")
plt.ylabel("População (x 10^8)")
plt.show()
