import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(host="localhost",user="root",password="asdf@123")
    sql = "create database MyFlaskDb"
    cursor = con.cursor()
    cursor.execute(sql)
    print("databse created.....")