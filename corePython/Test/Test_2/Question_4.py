a = int(input("enter the size of walls:"))
cost_price = 12     # per squeare feet

#calculate area of four equal sized walls
area = 4*a**2

total_cost = area * cost_price

print(f"total painting cost price is {total_cost}")