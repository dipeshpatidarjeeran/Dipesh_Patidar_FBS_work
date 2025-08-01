import re
data = """
101 Ganesh 25 ganesh.kasture@gmail.com
102 Musa 26 musa@yahoo.com
103 sujit 30 sujit@mail.co.in
"""
res = re.findall(r'[A-Za-z]+.?\w*@\w+.\w+\.?\w*', data)
res = re.findall(r'\d{3}', data)   # same [0-9]{3}
res = re.findall(r'^\w{3}', data, re.M)   

print(res)
