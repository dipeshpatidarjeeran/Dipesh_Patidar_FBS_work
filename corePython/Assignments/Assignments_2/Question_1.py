"""
    Convert the time enteredin hh, min and sec into seconds.
"""

seconds = int(input("enter the seconds:-"))

#calculate hours
hours = seconds // 3600
second = seconds % 3600

# calculate minutes
mins = second // 60
second = second % 60

print(f"{seconds} seconds is equivalent to {hours} hours, {mins} minutes, and {second} second")