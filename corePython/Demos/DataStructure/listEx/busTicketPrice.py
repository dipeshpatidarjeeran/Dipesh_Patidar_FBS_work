def busTicketPrice(li,dist,source,dest):
    beg = li.index(source)
    end = li.index(dest)
    add_dist = 0
    total_dist = 0
    for i in range(len(dist)):
        total_dist += dist[i]

    if beg < end:
        for i in range(beg, end):
            add_dist += dist[i]

        ticket_price = (add_dist/1000)*5
        return ticket_price
    else:
        for i in range(end, beg):
            add_dist += dist[i]
        ticket_price = (total_dist - add_dist)/1000 * 5
        return ticket_price

li = ['s1','s2','s3','s4','s5','s6']
dist = [1000,2500,3400,4800,2200,6200]
source = input("Enter the starting station name(from):-")
dest = input("Enter thew Ending station name(To):-")
price = busTicketPrice(li,dist,source,dest)
print(f"Station {source} to {dest} ticket price is {price} rupees")


# li = ['s1','s2','s3','s4','s5','s6']
# dist = [1000,2500,3400,4800,2200,6200]
# source = input("Enter the starting station name(from):-")
# dest = input("Enter thew Ending station name(To):-")

# i_src = li.index(source)
# i_dest = li.index(dest)

# i = i_src
# tot_dist = 0
# while(i != i_dest):
#     tot_dist += dist[i]
#     if(i == len(li) - 1):
#         i = 0
#     else:
#         i += 1

# print(tot_dist)
# tick_price = (tot_dist/1000) * 5
# print(tick_price)