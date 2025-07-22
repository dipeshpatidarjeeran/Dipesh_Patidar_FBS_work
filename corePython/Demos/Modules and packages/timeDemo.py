import time

### return current time in second
# print(time.time())

#### pause the program(sleep program execution)
# print("wait for 3 seconds.......")
# time.sleep(3)
# print('Hello')

#### get time in (day month date current_time year) format
# print(time.ctime())

#### get structured current time 
# print(time.localtime())
# print(time.localtime().tm_year)
# print(time.localtime().tm_mon)
# print(time.localtime().tm_mday)
# print(time.localtime().tm_hour)

#### format time
# formart_time = time.strftime('%d-%m-%Y %H:%M:%S',time.localtime())
# print(formart_time)

#### string format time
# st = '21-07-2025 18:30:00'
# par = time.strptime(st,'%d-%m-%Y %H:%M:%S')
# print(par)


####
# start = time.perf_counter()
# time.sleep(5)
# end = time.perf_counter()

# print("Execution Time:", end - start, "seconds")