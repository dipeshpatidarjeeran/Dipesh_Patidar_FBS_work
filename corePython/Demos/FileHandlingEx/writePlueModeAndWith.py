with open("corePython/Demos/FileHandlingEx/demo1.txt", "w+") as fp:
    fp.write("""Firstbit solutions is an educational institute.
    It provide IT courses with placement.""")
    print(fp.tell())
    fp.seek(0,0)
    content = fp.read()
    print("Content:",content)
    