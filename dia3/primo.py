print("********************************************************************")
print("*****************************BIENVENIDO*****************************")
print("********************************************************************")
print("Con este programa vamos a comprobar si un numero que ingreses es primo")
print("********************************************************************")
print("(j) verificar si un numero es primo")
print("(h) Detener programa")
print("(o) informacion adicional")

opcion = input("por favor elige una opcion")

if opcion == "j":
    print(" vas a verificar si un numero x es primo")
    n = int(input("ingrese un numero : "))
    a = 1
    b = 0
    
    while a <= n:
        if n % a == 0:
           b = b + 1
        a = a + 1
    if b == 2:   
        print("el nunero que ingresaste efectivamente es primo" ,)
    else:
        print(" el numero que ingresaste no es primo") 
        break    
            
elif opcion == "h":
    print("Detuviste el programa")
    break
elif opcion == "o":
    print("Informacio a cerca de los numeros primos :")
    print("Los números primos son aquellos que solo son divisibles por ellos mismos.")
else:("ingresa una opcion valida del menú")  

   
