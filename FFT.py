#--------------------------------------------------------------------------------------------------------- 
# INSTITUTO POLITÉCNICO NACIONAL - ESCUELA SUPERIOR DE CÓMPUTO
# Materia: Teoría de Comunicaciones y señales
# Bonilla Reyes José Luis
# Domínguez Morales José Manuel
#---------------------------------------------------------------------------------------------------------

import sys 
from sys import platform
import math as mt
import numpy

import os

def clearScreen():
    """Description: Funcion que detecta el sistema operativo y relaciona su comando para borrar la pantalla
    """
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def ingresa_secuencia():
    """Description: Funcion que guarda la secuencia de N los elementos introducidos por el usuario
    
    :return s : list
    Regresa una lista, que es la secuencia   
    """
    s = []
    nom = "X(n)"
    N = int(input("Ingresa el numero de muestras N: "))
    while(N%2 != 0):
        print("N debe ser potencia de 2")
        N = int(input("Ingresa el numero de muestras N: "))

    print("Ingresa la secuencia " + nom + " :\n ")
    while( len(s) < N):
    	number = input(( nom +" = " + str(s) + ": "))
    	#try:
    	number = complex(number)
    	#except ValueError :
    	#	number = float(number)
        

    	s.append(number)
    clearScreen()
    print(nom + " = " + str(s))
    return s


def fft(funcion):
    """Description: funcion que obtiene la transformada discreta de fourier usando el algoritmo FFT
    
    :param funcion : list
        señal discreta
    
    :return resultado : list
    señal discreta despues de la FFT

    """
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

def ifft(funcion):
    """Description: obtiene la transformada inversa discreta de fourier usando una modificacion del algoritmo FFT

    :param funcion : list
    señal discreta previamente transformada

    :return resultado : list
    señal discrtea despues de la IFFT
    
    """
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
            w = complex(mt.cos(2*mt.pi*i/(n)),mt.sin(2*mt.pi*i/(n))) 
            resultado[i] = ((pares[i]+w*impares[i])/n)#.conjugate()
            resultado[n//2 + i] = ((pares[i]-w*impares[i])/n)#.conjugate()

        return resultado

funcion = ingresa_secuencia()
#print("\nFFT(numpy): ")
#print(numpy.fft.fft(funcion))
print("\nFFT: ")
print(fft(funcion))
#print("\nIFFT(numpy): ")
#print(numpy.fft.ifft(funcion))
print("\nIFFT: ")
print(ifft(funcion))
