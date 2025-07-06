# Write a Python program to find elements in a given set that are not in another set.
s = {1,2,3,4,5,6}
ele = int(input(f"enter the element find in set {s}:-"))

for i in s:
    if i == ele:
        print(f"{ele} present in set")
        break
else:
    print(f"{ele} not present in set")