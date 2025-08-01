import re
data = """
Mr. Akshay Kumar 56
Mrs. Twinkle Kumar 54
Mr. Ajay Devgan 57
Mrs. Kajol Devgan 54
"""
res = re.findall(r'Mr.?s?.? \w+ \w+', data)
print(res)