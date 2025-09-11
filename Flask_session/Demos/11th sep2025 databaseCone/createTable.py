import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')
    # sql = """ALTER TABLE students ADD sid INT PRIMARY KEY AUTO_INCREMENT"""
    sql = """insert into students(sname,age,percentage,course) values("Ram",35,88,"java")"""
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("table created.....")