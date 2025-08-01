import re
data = """
101 Ganesh 25 ganesh@gmail.com
102 Musa 26 musa@yahoo.com
103 sujit 30 sujit@mail.co.in
"""

#\w - alphanumeric
res = re.findall(r'\w', data)

#\W - Not alphanumeric
res = re.findall(r'\W', data)

# \d - digits
res = re.findall(r'\d', data)

# \D - Not digits
res = re.findall(r'\D', data)

# \s - \n, \t, space
res = re.findall(r'\s', data)

#\S - Not \n, \t, space
res = re.findall(r'\S', data)

#{3} exactly 3 occurances
res = re.findall(r'\w{3}', data)

# + 1 or more occurances
res = re.findall(r"\w+",data)

# * 0 or more occurances
res = re.findall(r"\w*", data)

# ? 0 or 1 occurance
res = re.findall(r'\w?',data)

# [abc] - a or b or c

# a|b - a or b

str1 = """Firstbit solutions is an educational institude
firstbit solutions located on FC road pune"""

#^ pattern at begining
res = re.findall(r'^\w+', str1)

# $ pattern at ending
res = re.findall(r"\w+$", str1)

res = re.findall(r"^\w+|\w+$", str1)

# re.M - for multiline check
res = re.findall(r"^Firstbit", str1, re.M)

# re.I - for ignoring upper and lower case
res = re.findall(r"^firstbit", str1, re.M|re.I)
print(res)
