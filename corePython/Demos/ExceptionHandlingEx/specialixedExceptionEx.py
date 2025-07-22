li = [10,20,30,40]
try:
    li.index(60)
    li.pop(7)

# specialized Exception
except ValueError as e:
    print("ValueError:",e)

except IndexError as e:
    print("IndexError:",e)

    
# generalized exception
except Exception as e:
    print("Error:",e)

print("Program successfully executed.")