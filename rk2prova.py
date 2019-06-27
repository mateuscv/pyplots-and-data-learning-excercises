import matplotlib.pyplot as pyplot
import math

def f(y):
    return -0.4*y

def k1calc(yi):
    return f(yi)

def k2(yi, h, k1):
    return f(yi+h*k1)

def rk2(t, y):
    i = 0
    while i<3:
        k1=k1calc(y[i])
        yimais1 = y[i]+(0.500000*h)*(k1+k2(y[i],h,k1))
        y.append(yimais1)
        t.append(t[i]+h)
        i+=1
    return t,y

def solAl(t):
    return 4*math.exp(-0.4*t)

t=[0]
y=[4]
h=0.25

t,y = rk2(t, y)

yanal = []

for i in t:
    yanal.append(solAl(i))

pyplot.plot(t, y, label='Numérica (RK2)')
pyplot.plot(t, yanal, label='Sol. Analítica')
pyplot.title("RK2 vs. Sol Analítica")
pyplot.grid(True)
pyplot.legend()
pyplot.show()