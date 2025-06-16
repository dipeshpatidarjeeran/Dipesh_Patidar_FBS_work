"""
    Input 5 subject marks from user and display grade(eg.First class,Second class ..)
"""
hindi = int(input("enter the hindi marks:-"))
english = int(input("enter the English marks:-"))
maths = int(input("enter the Maths marks:-"))
gk = int(input("enter the Gk marks:-"))
science = int(input("enter the science marks:-"))

total_mark = hindi+english+maths+gk+science
pre = total_mark/5
if pre>=90:
    print(f"presentage is {pre}")
    print("Passed with first grade")
elif pre>=75:
    print(f"presentage is {pre}")
    print("Passed with second grade")
elif pre>=60:
    print(f"presentage is {pre}")
    print("Passed with third grade")
elif pre>=40:
    print(f"presentage is {pre}")
    print("Passed with fourth grade")
else:
    print(f"presentage is {pre}")
    print("Faill")