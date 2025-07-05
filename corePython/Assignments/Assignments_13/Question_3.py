# Python Program to Check if a Given Key Exists in a Dictionary or Not
dict1 = {1:"python",2:"java",3:"C",4:"R"}
key = int(input("Enter the key:-"))

for i in dict1.keys():
    if i == key:
        print(f"key {key} present in dict {dict1}")
        break
else:
    print(f"key {key} not present in dict {dict1}")
