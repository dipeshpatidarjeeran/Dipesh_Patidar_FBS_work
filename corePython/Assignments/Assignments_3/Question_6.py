"""
    Write a program to calculate profit or loss.
"""
sp = int(input("enter the selling price:-"))
cp = int(input("enter the cost price:-"))

if(sp>cp):
    print(f"profit is {sp-cp}")
elif(sp<cp):
    print(f"loss is {cp-sp}")
else:
    print("No profit No loss")