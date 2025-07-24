# Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.
class StepZeroException(Exception):
    def __init__(self, str1):
        self.str1 = str1

    def __str__(self):
        return self.str1

def custom_range(start, stop=None, step=1):
    try:
        if step == 0:
            raise StepZeroException("step must not be Zero")
    except StepZeroException as e:
        return e
    
    if stop == None:
        stop = start
        start = 0
    # print(start, stop, step)
    # li = []
    if step > 0:
        while stop > start:
            # li.append(start)
            yield start
            start += step
    else:
        while stop < start:
            # li.append(start)
            yield start
            start += step

    # return li

c = custom_range(10,4,0)

print(next(c))
print(next(c))
print(next(c))
