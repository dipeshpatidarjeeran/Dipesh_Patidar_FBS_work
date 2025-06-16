"""
     write a program to calculate the percentage of student based on marks of ant 5 subjects.
"""

hindi = int(input("enter the Hindi subject marks:-"))
english = int(input("enter the English subject marks:-"))
maths = int(input("enter the Maths subject marks:-"))
science = int(input("enter the Science subject marks:-"))
social_science = int(input("enter the Social Science subject marks:-"))

# calculate the total marks
total_marks = hindi+english+maths+science+social_science

# calculate percentage 
percentage = total_marks/500*100

print(f"percentage of 5 subjects marks is {percentage}%")