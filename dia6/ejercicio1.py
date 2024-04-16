lista = [8,7,1,4,20,1,15,1,1,4,3,6,7,8,9,1,1,1,3,3,1,2,10] #defino los valores que deseo reorganizar o remover de la lista
lista = list(set(lista)) #con el comando set hacemos que tome valores unicos de una lista sin repetirlos
lista.sort()
print(lista)