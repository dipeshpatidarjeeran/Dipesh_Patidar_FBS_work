import re

str1 = """Firstbit solutions is an educational institude
Firstbit solutions located on FC road pune."""

pattern = re.compile(r'Firstbit')
print(pattern)
res = re.findall(pattern, str1)
print(res)

print(re.findall(re.compile(r'Firstbit'), str1))