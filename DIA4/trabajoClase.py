print("*********************************BIENVENIDO******************************************")
print("con este programa vamos a determinar las monedas necesarias para entregar como cambio")
print("*********************************BIENVENIDO******************************************")

def calCambio (dinero): #definimos la variable dinero
    valores = [10,5,1] #le damos los valores de las modenas disponibles dentro de una lista 

    valores10 = dinero /10 #el total del dinero ingresado sera dividido por la moneda de mayor valor primero para optimizar
    dinero %= 10

    valores5 = dinero /5 #el total del dinero ingresad sera divido por la segunda moneda de mayor valor
    dinero %=5

    valores1 = dinero /1 #el total del dinero ingresado sera divido por la moneda de menor valor para llegar a sumar el valor exacto del cambio
    dinero %=1
 
    return valores10, valores5 ,valores1 #retornamos a los valores de cada moneda para posteriormente saber cuantas de cada una se utilizo para llegar al total del cambio
    
dinero = int(input("ingrese el dinero : ")) #pedimos al usuario ingresar el valor al cual se le desea hacer el cambio con las correspondientes monedas
valores10, valores5 , valores1 = calCambio(dinero) #agregamos el valor de cada moneda al dinero
print("las monedas de 10 que se utilizaron fue : ",valores10) #mostramos en pantalla las monedas que usó de cada uno
print("las monedas de 1 que se utilizaron fue : ",valores5)  
print("las monedas de 5 que se utilizaron fue : ",valores1)  
   