# raise is a user define except
from userException import UserException, NameException
age = int(input("enter the age:-"))

if (age < 1 or age > 120):
    raise UserException(age)

name = input("enter the name:-")
if not name.strip().isalpha():
    raise NameException(name)