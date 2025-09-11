import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')
    Id = int(input("enter the student id:-"))

    sql = """delete from students where sid = %s"""
    val = (Id,)
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print("table created.....")