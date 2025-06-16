"""
    Convert distant given in feet and inches into meter and centimeter.
"""
feets = int(input("enter the feets:-"))
inches = int(input("enter the inches:-"))
inches = (feets*12)
cm = inches * 2.54                                               # 1 inche = 2.54cm
meter = cm // 100
cm = cm % 100
print(f"{meter} meters {cm} centimeters")



# cm = feets * 30.48                                                # 1 feet = 30.48cm
# meter = cm // 100
# cm = cm % 100
# print(f"{feets} feets = {meter} meters {cm} centimeters")
