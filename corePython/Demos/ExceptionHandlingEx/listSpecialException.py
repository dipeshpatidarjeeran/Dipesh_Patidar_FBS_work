li = [10,20,30]
di = {'name':'abc','age':24}
try:
    # li.remove(50)
    # name = li[0] + "name"
    # value = li[5]
    # add = di['address']
    # print(x)
    # "hello".push()
    # import wrongmodule
    result = 10 / 0



except ValueError as e:
    print("ValueError:", e)

except TypeError as e:
    print('TypeError:',e)

except IndexError as e:
    print("IndexError:",e)

except KeyError as e:
    print("KeyError:",e)

except NameError as e:
    print("NameError:",e)

except AttributeError as e:
    print("AttributeError:",e)

except ModuleNotFoundError as e:
    print("ModuleNotFoundError:",e)

except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)

else:
    print(li)