# Write a program to create three lists of numbers, their squares and cubes
li = [1,2,3,4]
square = []
cube = []
for i in li:
    square.append(i**2)
    cube.append(i**3)

print('Square list:',square)
print('cube list:',cube)