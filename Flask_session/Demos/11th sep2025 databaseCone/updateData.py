import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')
    Id = int(input("enter the student id:-"))
    sname = input("update the name:-")

    sql = """update students set sname=%s where sid = %s"""
    val = (sname, Id)
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print("table created.....")