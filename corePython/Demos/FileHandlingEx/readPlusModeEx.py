fp = open("corePython/Demos/FileHandlingEx/demo1.txt", "r+")

# read corsor position
print("Curse position:", fp.tell())

# change cursor position to end
fp.seek(0,2)

#write data 
fp.write("This is another line.")

# change cursor position to beg
fp.seek(0,0)

# read data
content = fp.read()
print(content)
fp.close()