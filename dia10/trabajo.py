#primer ejercicio
nums= [1,3,5,6]
print(nums)
print(nums.index(5))
print()


#segundo ejercicio

objetivo=int(input("ingresa numero objetivo : "))
nun=[1,3,5,6]

cont=0
nun.append(objetivo)


for i in nun:
    cont+=1
    if objetivo == i:
     nun.sort()
     print(nun)
     print(cont-1)
     break


