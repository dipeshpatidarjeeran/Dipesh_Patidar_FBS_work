#1. structure -set(),{1,2,3} {} with only values
s = {1,2,3}
s = set() 
print(type(s))

#2. Heterogenous
s = {1,'a',3.14}

#3. Unordered
print(s)

#4. Changable: Mutable, but not editable
s.add('c')

#5. Only unique values are allowed.
# print(s[0])