#### lambda Function
#1. One line function
#2. Anonymous function
#3. lambda parameters: expression

add = lambda a, b: a + b
print("Addition:-",add(20,30))

rect = lambda l, b: l * b
print("Area of rectangle:-",rect(5.2, 20))

marks = lambda h, e, s, m, gk: (h + e + s + m + gk) / 5
print("percentage of 5 sub marks:-",marks(60, 80, 50, 78, 70))
