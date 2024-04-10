#--------------------------------
#---- DIA 1 CHEAT SHEET PYTHON ------
#--------------------------------

#Imprimir hola mundo
print("Hola mundoooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion

#Conversion de tipos de variable

#Bucles For y While

#Funciones (4 Tipos)

#Desarrollado por Jhonatan Omaña - C.C 1091596690
#/////////////////////////////////////////////////////////////////////////////////////////////////
print("////////////////////////////////////////////////////////////////////")
#Ingresa por teclado la infomarcion

print("Hola bienvenido soy Jhonatan")
print("ingresa tu nombre")
nombre = input()
print("Bienvenido  ", nombre, ". Gracias por usar mi programa.", sep="")

#/////////////////////////////////////////////////////////////////////////////////////////////////
print("////////////////////////////////////////////////////////////////////")
#Conversion de tipos de variable
#conversion de un entero a un flotante
numero_entero = 10
numero_flotante =float(numero_entero)
print(numero_flotante)
print("////////////////////////////////////////////////////////////////////")
#coversion de string a entero
edad = "23"
print(edad)
int_edad = int(edad)
print(int_edad)

#/////////////////////////////////////////////////////////////////////////////////////////////////
print("////////////////////////////////////////////////////////////////////")
#Bucles For y While
cadena = "hola,mundo"
for caracter in cadena:
    print(caracter)

print("////////////////////////////////////////////////////////////////////")


contador = 0
while contador < 20:
 print(contador)
 contador+=2
 
 
 
 print("////////////////////////////////////////////////////////////////////")
 
 #funcion sin parametro y sin retorno

n=("Introduccion python")
print(n)
print("////////////////////////////////////////////////////////////////////")
 
 
a=10
b=5
restar=(a-b)
print("la resultado de la resta es:",restar)

print("////////////////////////////////////////////////////////////////////")

print("por favor digita un numero:")
retor=input()
print("el numero es :",retor)

print("////////////////////////////////////////////////////////////////////")
a=10
b=2
divid=(a/b)
print("el resultado de la division es: " ,divid)