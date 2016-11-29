from sympy import *
from timeit import timeit
from time import time
import sys


tiempo_inicial = time()
t=Symbol('t')
i = 0;
local_a =0
local_b =0
s = long(sys.argv[1])
size=32
total = float(0)
valor=float(s)/size
aux=0
vec=[None]
vec[0]=0
j=0


while j< size:
	aux+=valor
	vec.append(aux)
	j=j+1

expresion = (exp(-t)*t**3)
uno=integrate(expresion)
j=0
while j< size:
	local_a = vec[j]
	local_b = vec[j+1]
	dos=uno.evalf(subs={t:local_a})
	tres=uno.evalf(subs={t:local_b})
	cuatro=tres-dos
	total+=cuatro
	j=j+1


tiempo_final = time() - tiempo_inicial
j=0

print "expresion inicial: "
print expresion
print "expresion integrada: "
print uno
print "tiempo total de ejecucion: " + str(tiempo_final)
print "valor ="+ str(total)