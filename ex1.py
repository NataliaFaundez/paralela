from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD  # comunicador entre dos procesadores

rank =  comm.rank     # id procesador actual
size =  comm.size     #

if rank ==0:
    lista_enviar = [1,2,3]   # crea lista
    comm.send (lista_enviar, dest = 1)
    comm.send (lista_enviar, dest = 2)
#    comm.send (lista_enviar, dest = 9)

if rank ==1:
    lista_recibir = comm.recv(source=0)
    lista_recibir.append(10) # agregar al final #
    comm.send(lista_recibir, dest=0)

if rank==2:
    lista_recibir = comm.recv(source=0)
    lista_recibir.append(7) # agregar al final #
    comm.send(lista_recibir, dest=0)

#if rank==9:
#    lista_recibir = comm.recv(source=0)
#    lista_recibir.append(7) # agregar al final #
#    comm.send(lista_recibir, dest=0)

if rank==0:
    lista_uno = comm.recv(source=1)
    lista_dos = comm.recv(source=2)


    print ("He recibido el ")
    print (lista_uno + lista_dos)


