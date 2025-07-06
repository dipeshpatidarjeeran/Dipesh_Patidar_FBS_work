# Write a Python program that finds all pairs of elements in a set whose
# sum is equal to a given value.
s = {1,2,3,4,5,6,7,8,9}
value = int(input(f"Enter the value:-"))
s1 = set()
for i in s:
    for j in s:
        if i+j == value and i != j:
            a = sorted([i,j])
            
            s1.add(tuple(a))
print(f"finds all pairs of elements in a set whose sum is equal {value}")
print(s1)
