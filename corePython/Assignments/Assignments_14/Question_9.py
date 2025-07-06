# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.
nums = [2, 4, 3, 5, 7, 8, 1]
target = 15
s1 = set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k] == target:
                a = sorted([nums[i],nums[j],nums[k]])
                
                s1.add(tuple(a))
print(s1)

