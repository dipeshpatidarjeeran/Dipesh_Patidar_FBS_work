import pickle
from emp import Emp

# e1 = Emp(102, "dipesh", "DS", 450000)

# with open("corePython/Demos/FileHandlingEx/pickleDemo.txt", 'ab') as fp:
#     pickle.dump(e1, fp, protocol=pickle.HIGHEST_PROTOCOL)

dict1 = {1:"ram",2:"dipesh",3:"suraj"}

with open("corePython/Demos/FileHandlingEx/pickleDemo.txt", 'ab') as fp:
    pickle.dump(dict1, fp, protocol=pickle.HIGHEST_PROTOCOL)