from mpi4py import MPI

comm = MPI.COMM_WORLD #comunicador entre procesadores
size = comm.Get_rank() #cantidad de procesadores
rank = comm.Get_rank() #procesador actual

root = 0 

buf = 0
buf_list = None
if rank == root: #procesador 0, madre
    buf = 777  #bur se modifica en procesador 0 

print "[%d]: Before Bcast, buf is %d\n"%(rank, buf) # se imprime en todos los procesadores 
#porque esta afuera y solo la madre es 777 el resto es 0
buf = comm.bcast(buf, root=root)  #en todos los procesadores (1 al 3)el buf es modificado a 777 por el buf que esta en madre 
print "[%d]: Before Bcast, buf is %d\n"%(rank, buf) # se imprime en todos los procesadores
buf = buf + rank # a cada buf se le agrega la posicion del procesador
buf_list = comm.gather(buf, root=root) #agarra los buf de los procesadores y los devuelve a la lista buf en el procesador madre

if rank ==root: #estando en posicion madre
    print buf_list #imprime lista buf