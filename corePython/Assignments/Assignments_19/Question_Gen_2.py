# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindrome(start):
    
    while True:
        n = start
        rev = 0 
        while(n > 0):
            d = n % 10
            rev = rev * 10 + d
            n //= 10
        if start == rev:
            yield start
        start += 1

p = palindrome(11)    

print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))