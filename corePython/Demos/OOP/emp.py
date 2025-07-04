###Implementations of class
class Employee:
    def setdata(self):  # methods/behaviour
        print("this is setdata method.")

### creating of object
# object_naem = class_name
emp1 = Employee()

### calling behaviour/methods
# object_name.fun_name()
emp1.setdata()

# for storing reference of an object in methods use self keyword
#reduse code inconsintence
# to bind attribute in the self