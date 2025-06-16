"""
    Write a program to print Armstrong number within a given range
"""
# armstrong number is ex 153 = 1**3 + 5**3 + 3**3
# armstrong number is ex 1634 = 1**4 + 6**4 + 3**4 + 4**4

for i in range(5006):
    arm = i
    power = len(str(i))
    sum = 0
    # print(power)
    while(i>0):
        a = i%10
        sum+= a**power
        i = i//10
    # print(sum)
    if arm == sum:
        print(arm)