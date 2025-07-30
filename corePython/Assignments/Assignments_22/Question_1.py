# 1. Create a class Emp (eid,ename,basic)

class Emp:
    def __init__(self, eid, ename, dept, sal):
        self.eid = eid
        self.ename = ename
        self.dept = dept
        self.sal = sal

    def __str__(self):
        return f"{self.eid}, {self.ename}, {self.dept}, {self.sal}"
        

if __name__ == "__main__":
    e1 = Emp(1,"dipesh","DS",45000)
    print(e1)