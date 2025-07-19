# Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

n = int(input("how many emp present:-"))
total = 0
for i in range(1,n+1):
    sal = int(input(f"Enter the basic salary emp_{i}:-"))
    if sal < 20000:
        total_sal = sal + sal*10/100 + sal*12/100 +sal*15/100
    else:
        total_sal = sal + sal*15/100 + sal*18/100 +sal*20/100
    total += total_sal
    print(f"Employee_{i} total salary is:-",total_sal)

print("total salary of all Employee:-",total)