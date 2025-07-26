import pickle
from emp import Emp

with open("corePython/Demos/FileHandlingEx/pickleDemo.txt", "rb") as fp:
    data = pickle.load(fp)
    print(data)