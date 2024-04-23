import json

archivo_json = "C:/Users/Uniminuto Tibu/Desktop/large-file.json"

with open(archivo_json, encoding="utf-8") as archivo:
    datos_json = json.load(archivo)


variable = datos_json["type"]  
print(datos_json) 



print()
print ("                M E N U              ")
print("1 Recorrer eventos en la base de datos")
print("2 crear")
print("3 actuaizar")
print("4 eliminar")
print()

opc=int(input("ingrese un opcion del 1 al 4 :"))

if opc == 1:
    print(datos_json)
if opc == 2:
    print("")

