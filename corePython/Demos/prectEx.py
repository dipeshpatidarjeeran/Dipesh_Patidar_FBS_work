# # perfect number
# n = 28
# add = 0
# i = (n//2)
# while(i > 0):
#     if n%i == 0:
#         add += i
#     i -= 1

# if n == add:
#     print(f"{n} is perfect number")
# else:
#     print(f"{n} is not perfect number")



# # palindrome number
# n = 121
# pal = n
# rev = 0
# while(n>0):
#     d = n % 10
#     rev = rev * 10 + d
#     n //= 10

# if(pal == rev):
#     print(f'{pal} is palindrome number')
# else:
#     print(f'{pal} is not palindrome number')


# # strong number
# n = 145
# st = n
# add = 0
# while(n > 0):
#     d = n % 10
#     fact = 1
#     while(d > 0):
#         fact *= d
#         d -= 1
#     add += fact
#     n //= 10

# if st == add:
#     print(f"{st} is strong number")
# else:
#     print(f"{st} is not strong number")


# # fibonacci series
# n = 6
# a = -1
# b = 1
# while(n > 0):
#     c = a+b
#     print(c)
#     a = b
#     b = c
#     n -= 1


# # how to print 1 to n prime number
# n = 15
# for i in range(2,n+1):
#     j = 2
#     while(i > j):
#         if i%j == 0:
#             break
#         j += 1
#     else:
#         print(i)


# # how to print first n prime number
# n = 10
# count = 0
# first_p = 2
# while(n > count):
#     start = 2
#     while(start < first_p):
#         if first_p % start == 0:
#             break
#         start += 1
#     else:
#         print(first_p)
#         count += 1
#     first_p += 1
    


# # armstrong number
# n = 153
# arm = n
# digit = 0

# while(n > 0):
#     n //= 10
#     digit += 1

# add = 0
# num = arm
# while(num > 0):
#     d = num % 10
#     add += d**digit
#     num //= 10

# if arm == add:
#     print(f"{arm} is armstrong number")
# else:
#     print(f"{arm} is not armstrong number")


