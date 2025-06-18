#### Keyword argument/parameter
#1. Assign value to parameter in function call
#2. flow in right to left
#3. skip positional parameter concept

def employee(id,name,add,sal):
    eData = f'ID:{id}\nNAME:{name}\nADDRESS:{add}\nSALART:{sal}'
    return eData

print(employee(name='Dipesh Patidar',sal=45000,id=101,add='MP'))
print('#'*30)
print(employee(102,'rahul',sal=45000,add='Neemuch'))