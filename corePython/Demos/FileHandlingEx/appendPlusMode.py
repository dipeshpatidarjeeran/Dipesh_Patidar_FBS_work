with open("corePython/Demos/FileHandlingEx/demo1.txt", "a+") as fp:
    print("Curser position:",fp.tell())

    fp.seek(0, 0)
    content = fp.read()
    print("Content:",content)

    print("Curser position:", fp.tell())
    fp.write("\nThis is last line")