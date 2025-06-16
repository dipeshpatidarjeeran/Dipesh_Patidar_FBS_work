"""
    Enter number of students from user. For those many 
    students accept marks of 5 subject marks from user and 
    calculate percentage. Display all percentage and average 
    percentage of students.
"""
n = int(input("enter the number of student:-"))
total_per_sum = 0

for i in range(1,n+1):
    total_mark = 0
    for j in range(1,6):
        sub = int(input(f"enter the {j} subject marks:-"))
        total_mark += sub

    per = total_mark/5

    total_per_sum += per
    print(f"percentage of student {i} is {per}%")

avg_per = total_per_sum/n
print(f"average percentage of all student is {avg_per}%")