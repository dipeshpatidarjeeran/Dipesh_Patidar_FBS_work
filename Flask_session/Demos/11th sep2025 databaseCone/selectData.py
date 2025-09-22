import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')
    # Id = int(input("enter the student id:-"))
    
    sql = "select * from students where sid=3"
    cursor = con.cursor()
    cursor.execute(sql)
    record = cursor.fetchone()
    print("fetch one record:-",record)

    sql1 = "select * from students"
    cursor.execute(sql1)
    record = cursor.fetchall()
    print("fetch all record:-",record)
    print("table created.....")