### keyword length/ number of argument / parameter
#1. we assign multiple values with parameters in function call.
#2. Muntion two asterisk(**)symbol before parameter name in function definition.
#3. data stored in dictionary

def employee(**data):
    for i,j in data.items():
        print(i,':',j)

# employee(id=101)f
employee(id=102,name='dipesh',sal=45000)