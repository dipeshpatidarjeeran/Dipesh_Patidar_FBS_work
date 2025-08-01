import re
data = """101 Ganesh 25 ganesh@gmail.com
102 Musa 26 musa@yahoo.com
103 sujit 30 sujit@mail.co.in
"""
res = re.match(r'\w+', data)
print(res.group()) # match element in the bigning of the string
