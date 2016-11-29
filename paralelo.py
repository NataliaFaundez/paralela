from sympy import *
from timeit import timeit
from time import time
import sys
import numpy
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE


tiempo_inicial = time()


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


i = 0
s = int(sys.argv[1])


t=Symbol('t')
valor=float(s)/size
aux=0
vec=[None]
vec[0]=0
j=0


while j< size:
	aux+=valor
	vec.append(aux)
	j=j+1


local_a = vec[rank]
local_b = vec[rank+1]
inte = numpy.zeros(1)
recv_buffer = numpy.zeros(1)
expresion = (exp(-t)*t**3)
uno=integrate(expresion)
dos=uno.evalf(subs={t:local_a})
tres=uno.evalf(subs={t:local_b})


inte[0] = tres-dos


if rank == 0:
		print "expresion inicial: "
		print expresion
		print "expresion integrada: "
		print uno
		total = inte[0]
		for i in range(1, size):
			comm.Recv(recv_buffer, ANY_SOURCE)
			total += recv_buffer[0] 
		tiempo_final = time() - tiempo_inicial
		print "tiempo total de ejecucion: " + str(tiempo_final)
else:
	comm.Send(inte)


if comm.rank == 0:
        print "valor ="+ str(total)


