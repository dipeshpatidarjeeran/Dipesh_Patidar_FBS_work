#### Rules:
#1. contains alphabets, digits & underscore
#2. can't starts with digits
#3. no limitation for name of variable
#4. can't use space
#5. can't use special symbol except underscore

# abc : true
# total_no : true
# no1 :   true
# 1no : false
# total no  :  false

abc = """
    contains alphabets, digits & underscore
    can not start with digits
    """
print(abc)
print(type(abc))
