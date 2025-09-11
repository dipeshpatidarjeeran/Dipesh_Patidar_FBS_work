import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')
    sname = input("enter the name:-")
    age = int(input("enter the age:-"))
    per = float(input("enter the percentage:-"))
    course = input("enter the course:-")

    sql = """insert into students(sname,age,percentage,course) values(%s,%s,%s,%s)"""
    val = (sname,age,per,course)
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print("table created.....")