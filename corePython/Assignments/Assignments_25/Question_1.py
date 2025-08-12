# Develop a function that takes a text and a list of forbidden words. Replace all
# occurrences of these forbidden words with asterisks (*) using regular expressions.
import re
text = "this is my first coding line"
forbi = ['my', 'line']

pattern = ''
res = re.sub(r'\b(my|line)',lambda m: "*" * len(m.group()), text)
print(res)