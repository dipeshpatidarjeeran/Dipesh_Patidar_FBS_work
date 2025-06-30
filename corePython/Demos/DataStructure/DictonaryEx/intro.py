#1. structure: {}, {1:'a'}
dict1 = {1:'a'}
print(type(dict1))

#2. Types of data: Key is unique, dubplicate values can be allowed.
dict1 = {1:'python',2:"java",2:"C",3:"python"} # 'c' will overwrite 'java'
print(dict1)

#3. sequence: Orderd
# print(dict1)

#4. changable: value-mutable, pair-mutable, key-Immutable
dict1[3] = "R"
dict1[4] = "c++"

print(dict1)

#5. mutable data structure can not allowed as key
dict2 = {'abc':12,[1,2,3]:123}
print(dict2)