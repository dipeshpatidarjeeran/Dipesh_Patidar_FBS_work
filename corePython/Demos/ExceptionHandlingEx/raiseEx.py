# raise is a user define except
from userException import UserException
age = int(input("enter the age:-"))

if (age < 1 or age > 120):
    raise UserException(age)