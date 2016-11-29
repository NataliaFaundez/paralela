from mpi4py import MPI
import random

def prom (lis):
	for i in range(0,len(lis)):
		suma=suma+lis[i]
 	prome= suma/len(lis)
 	return prome



comm = MPI.COMM_WORLD  # comunicador entre dos procesadores #

rank =  comm.rank     # id procesador actual #
size =  comm.size     # tamano procesador #

if rank==0:
    lista=[1,3,5,7,8,9,2,4,6]
    comm.send(lista[0:3], dest=1)
    comm.send(lista[3:6], dest=2)
    comm.send(lista[6:9], dest=3)

if rank==1:
 	recibir=comm.recv(source=0)
 	p=prom(recibir)
 	comm.send(p, dest=0)

if rank==2:
 	recibir=comm.recv(source=0)
 	p=prom(recibir)
 	comm.send(p, dest=0)

if rank==3:
 	recibir=comm.recv(source=0)
 	p=prom(recibir)
 	comm.send(p, dest=0)

if rank==0:
	pro1=comm.recv(source=1)
	pro2=comm.recv(source=2)
	pro3=comm.recv(source=3)	
	
 	print ("prom1 =", pro1, "prom2 ", pro2,"pro3",pro3,)

 