from sympy import *

def factorial(n):
    aux=1
    aux2=0
    cierto=false
    for i in range (n+1):
        if(i!=0):
            aux*=i
            if(aux!=n):
                cierto=false
            else:
                cierto=true
                aux2=i
    cierto =true           
    if(cierto==true):
        return aux2
    
x=Symbol('x')
y=Symbol('y')
t=Symbol('t')
cuatro=integrate(exp(-t)*t**3, t)
cinco=factor(cuatro)
print "4.- "+str(cuatro)
print "5.- "+str(cinco)

print str(simplify(cuatro))
siete=integrate((exp(-t)*t**3), (t,0,x))
print str(siete)
ocho=factor(siete)
print str(ocho)
partes=str(ocho).split("*exp(-x)")
print partes[0]
nueve=factor(partes[0])
print nueve
diez=factor(nueve)



    
print str(factorial(6))+"!"