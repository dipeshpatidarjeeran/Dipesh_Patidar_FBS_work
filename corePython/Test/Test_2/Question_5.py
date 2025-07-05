pro1 = int(input("Enter the product 1 price:-"))
pro2 = int(input("Enter the product 2 price:-"))
pro3 = int(input("Enter the product 3 price:-"))
pro4 = int(input("Enter the product 4 price:-"))
pro5 = int(input("Enter the product 5 price:-"))

total = pro1+pro2+pro3+pro4+pro5

print("total bill is ",total)
print("include 18% GST ",total*18/100)
total_bill = total + total*18/100

print("total bill is ",total_bill)