import re
data = """
101 Ganesh 25 ganesh@gmail.com
102 Musa 26 musa@yahoo.com
103 sujit 30 sujit@mail.co.in
"""
res = re.sub(r' \d{2} ', " ** ", data)
print(res)
