#Nombre del alumno: Fernando Javier Noh Requena 
#Matricula: 19070052
#Semestre y fecha de entrega: 17 de Mayo del 2022

#Librerias usadas en este programa: 
import math 
from math import sqrt

#Optimizacion local
#Ejercicio 1: Área de un circulo =============================================================================

#Precalcular expresiones constantes:
#Antes
radio=5
area=math.pi*math.pow(radio,2)
print("El area del circulo es: " +str(area))

#Despuess
radio=5
pi=3.1416 #Expresión constante, ya que π nunca cambia. 
radio2=radio*radio #Expresion constante
area=pi*radio2
print("El area del circulo es: ")
print(area)

#Ejercicio 2: Área de un cuadrado ============================================================================
#Antes: 
lado=10
mult=math.pow(lado,2)
print("El area del cuadrado es: " +str(mult))

#Despues:
lado=10
mult=lado*lado
print("El area del cuadrado es: " +str(mult))

#Ejercicio 3: Suma (Precalculo de valores) ===================================================================
#Antes: 
numero1=3
numero2=4
numero3=6
suma=numero1+numero2+numero3
print(suma)

#Despues:
numero1=3 
numero2=4
numero3=6
suma=13
print(suma)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Optimizacion Global
#Ejercicio 4: Hola mundo (Subexpresiones constantes globales)====================================================================
#Antes
saludo = 'Hola Mundo' 
print(saludo)

#Despues 
def saludar():
	print(saludo)

saludo = 'Hola, Mundo' #variable global definida en el cuerpo principal del programa
saludar()

#Ejercicio 5: ==================================================================================================
#Antes
suma=4+9+32+20
resta=4-9-32-20
multiplicacion=4*9*32*20
division=4+9/32+20

print("El resultado de la suma es: " +str(suma))
print("El resultado de la resta es: " +str(resta))
print("El resultado de la multiplicacion es: " +str(multiplicacion))
print("El resultado de la multiplicacion es: " +str(division))

#Despues
n1=4
n2=9
n3=32
n4=20

suma=n1+n2+n3+n4
resta=n1+n2+n3+n4
multiplicacion=n1*n2*n3*n4
division=n1+n2/n3+n4

print("El resultado de la suma es: " +str(suma))
print("El resultado de la resta es: " +str(resta))
print("El resultado de la multiplicacion es: " +str(multiplicacion))
print("El resultado de la multiplicacion es: " +str(division))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Optimizacion de bucle

#Ejercicio 6: Dias de la semana (Reducción de frecuencias)=================================================================================================
#antes
dia = 0    
while dia < 7:
    semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    print("Hoy es " + semana[dia])
    dia += 1

#Despues
dia = 0    
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
while dia < 7:
   print("Hoy es " + semana[dia])
   dia += 1

#Ejercicio 7: Meses del año (Reducción de frecuencias)=================================================================================================
#Antes
meses = 0    
while meses < 12:
    anio = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre']
    print("El mes en el que estamos es:  " + anio[meses])
    meses += 1

#Despues
meses = 0    
anio = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre']
while meses < 12:
    print("El mes en el que estamos es:  " + anio[meses])
    meses += 1


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Optimizacion de mirilla

#Ejercicio 8 ==================================================================================================
#Antes 
variable=100
for variable in range(variable): 
  print(variable)

#Despues
#Optimizado con break: 
variable=100
for variable in range(variable): 
  print(variable)
  if variable == 20: 
    break


#Ejercicio 9: =================================================================================================
#Antes
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")

#Despues 
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)


#Ejericicio 10: ================================================================================================
#Antes
for numero in range(10):
    print("El numero es: "+str(numero))

#Despues
for numero in range(10):
    if numero == 5:
        continue   
    print("El numero es: "+str(numero))
