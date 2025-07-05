print("rectangle length is 50 m and breadth is 40m.")
print("Circular section has radius 20m")

l = 50
b = 40
r = 20
times = 5
price = 35

tot_rec_len = l + b + l
circle_len = (2*22/7*r)/2
total_len = tot_rec_len + circle_len

print("barbed wire 5 times.")
total_bar_time = total_len* times

total_cost = total_bar_time * price

print("total cost of fencing is ",total_cost)