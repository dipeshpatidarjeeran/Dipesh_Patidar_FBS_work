"""
    Write a program to input any alphabet and check whether it is vowel or consonant.
"""
str1 = input("enter the one alphabet:-")
list1 = ['a','e','i','o','u']

if str1 in list1:
    print("alphabet is consonant.")
else:
    print("alphabet is vowel.")