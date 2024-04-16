def ubi (digitos, target):
    nums={}
    for i ,num in enumerate(digitos):
        añade= target - num 
        if añade in nums:
            return [nums[añade],i]
        
        nums[num]=i

    return["no se encontró resultado posible"]  


digitos=[1,2,5,10,15]  
target=12
print(digitos)
print(ubi(digitos, target))

