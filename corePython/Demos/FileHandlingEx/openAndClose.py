#channel reserved
fp = open("corePython/Demos/FileHandlingEx/user_details.txt", "r")

# dara read
content = fp.read()

# data print
print(content)

# channel released
fp.close()