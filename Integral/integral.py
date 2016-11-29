from mpi4py import MPI
from sympy import *
from timeit import timeit
t=Symbol('t')
x=Symbol('x')

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

siete=integrate((exp(-t)*t**3))#, (t,0,x))
t=3
print str(siete)
ocho=factor(siete)
ocho=simplify(ocho)
ocho=ocho/6
ocho=simplify(ocho)
print str(ocho)+" * 6"
print(timeit(" 'Hello, world!' .replace('Hello', 'Goodbye')")/1000)
