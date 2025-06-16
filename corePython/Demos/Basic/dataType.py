#### Numeric
#1. int(integer)
x= 10

#2. float(floating point)
x= 3.144565676567477574

#3. complex
x = 10 +5j

print(x)
print(type(x))



### Text
#1. str (string)
str = 'firstbit solution 1234@.'
str = "student's data"
str = 'Quote: "Tis is money"'
str = '''this is first line
this is second line'''
print(type(str))
print(str)



### sequential
#1. list
li = [10,20,30,50]
print(type(li))

#2. tuple 
tu = (10, 20, 40 ,5)
print(type(tu))
print(tu)

#3. range
obj = range(1,10)
print(type(obj))
print(obj)


### Mapping
#1. dict (distionary)
dict1 = {1:"python's", 2:"java",3:"C"}
print(type(dict1))
print(dict1)


####set Unsequatial
#1. set
s1 = { 10, 20, 30, 40}
print(type(s1))

#2 frozenset
s1 = frozenset({10,20,30,40})
print(type(s1))
print(s1)


####Boolean
#1. True
a = True

#2. False
b = False
print(type(a))



#### NoneType
x= None
print(type(x))


#### Binary
#1. bytes
x = b'firstbit'
print(type(x))
print(x)

#2. bytearray
x = bytearray(b'firstbit')
print(type(x))
print(x)

#3. memorytview
x = memoryview(b'firstbit')
print(type(x))




a= "computer"
for i in range(len(a)):
    for j in range(i+1):
        print(a[j], end='')
    print()