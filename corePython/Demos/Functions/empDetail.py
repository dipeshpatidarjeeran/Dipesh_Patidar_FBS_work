def employee(id, name, add='Neemuch', sal=54000000):
    eData = f"ID:{id}\nNAME:{name}\nADDRESS:{add}\nSALARY:{sal}"
    return eData

print(employee(101,'Dipesh','jeeran',500000))
print("#"*20)
print(employee(102,"Ram"))