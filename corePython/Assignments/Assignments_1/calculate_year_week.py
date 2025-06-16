"""
    write a program to convert days into years, weeks, days.
"""
days = int(input("enter the days:-"))

# calculate years
years = days // 365
day = days % 365

# calculate weeks
weeks = day // 7
day = day % 7

print(f"{days} days is equivalent to {years} years, {weeks} weeks, and {day} days")