import sys 
import math as mt
import numpy

def fft(funcion):
    n = len(funcion)
    if n == 1:
        return funcion
    else:
        pares = [ funcion[2*i] for i in range(n//2)]
        impares = [ funcion[2*i+1] for i in range(n//2)]    

        pares = fft(pares[:n//2])
        impares = fft(impares[:n//2])        
        resultado = [0 for i in range(n)]        
                
        for i in range(n//2):
            w = complex(mt.cos(2*mt.pi*i/(n)),-mt.sin(2*mt.pi*i/(n)))            
            resultado[i] = pares[i] +w*impares[i]
            resultado[n//2 + i] = pares[i] -w*impares[i]            
        
        return resultado

funcion = [1,1]
print("Numpy:")
for i in numpy.fft.fft(funcion):
    print(i)
print("FFT:")
for i in fft(funcion):
    print(i)
