# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero
class TelevisionException(Exception):
    def __init__(self, str1):
        self.str1 = str1

    def __str__(self):
        return self.str1

class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def getData(self):
        try:
            print("Enter the Television Details....")
            self.model_no = int(input("enter the Model Number:-"))
            self.screen_size = int(input("enter the televisoin screen size:-"))
            self.price = int(input("enter the price:-"))

            if self.model_no > 9999:
                raise TelevisionException(f"Model number must be less than 4 digits")
            if self.screen_size < 12 and self.screen_size > 70:
                raise TelevisionException("screen size greater than 12 and smaller than 70")
            if self.price < 5000:
                raise TelevisionException("price should be greater than 5000")
            
        except ValueError as e:
            print("Error:",e)
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

        except TelevisionException as e:
            print("Error:",e)
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("Television Model Number:",self.model_no)
        print("Television screen size:",self.screen_size)
        print("Television price:",self.price)

if __name__ == "__main__":
    t = Television()
    t.getData()
    t.display()

