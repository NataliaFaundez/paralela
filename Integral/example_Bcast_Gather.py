from mpi4py import MPI

comm = MPI.COMM_WORLD #comunicador entre procesadores
size = comm.Get_rank() #cantidad de procesadores
rank = comm.Get_rank() #procesador actual

root = 0 

buf = 0
buf_list = None
if rank == root:
    buf = 777

print "[%d]: Before Bcast, buf is %d\n"%(rank, buf)
buf = comm.bcast(buf, root=root)
print "[%d]: Before Bcast, buf is %d\n"%(rank, buf)
buf = buf + rank
buf_list = comm.gather(buf, root=root)

if rank ==root:
    print buf_list