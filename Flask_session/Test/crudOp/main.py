from flask import Flask,redirect,render_template,request
import mysql.connector


app = Flask(__name__)
con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')

# cursor = con.cursor()
# sql = "create table Book(bid int primary key auto_increment,bname varchar(20),price int,author varchar(20))"
# cursor.execute(sql)

@app.route("/addBook",methods=["GET","POST"])
def addBook():
    if request.method == "GET":
        return render_template("addBook.html")
    else:
        bname = request.form.get("bname")
        price = request.form.get("price")
        author = request.form.get("author")

        sql = "insert into book(bname,price,author) values(%s,%s,%s)"
        val = (bname,price,author)
        cursor = con.cursor()
        cursor.execute(sql,val)
        con.commit()
        return redirect("showAllBook")
    
@app.route("/showAllBook",methods=["GET","POST"])
def showAllBook():
    sql = "select * from book"
    cursor = con.cursor()
    cursor.execute(sql)
    books = cursor.fetchall()
    return render_template("showAllBooks.html",books=books)

@app.route("/deleteBook/<bid>",methods=["GET","POST"])
def deleteBook(bid):
    if request.method == "GET":
        return render_template("deleteConfirm.html")
    else:
        action = request.form.get("action")
        if action == "Yes":
            sql = "delete from book where bid=%s"
            val = (bid,)
            cursor = con.cursor()
            cursor.execute(sql,val)
            con.commit()
        return redirect("/showAllBook")
    
@app.route("/editBook/<bid>",methods=["GET","POST"])
def editBook(bid):
    if request.method == "GET":
        sql = "select * from book where bid=%s"
        val = (bid,)
        cursor = con.cursor()
        cursor.execute(sql,val)
        book = cursor.fetchone()
        return render_template("updateBook.html",book=book)
    else:
        bname = request.form.get("bname")
        price = request.form.get("price")
        author = request.form.get("author")

        sql = "update  book set bname=%s,price=%s,author=%s where bid=%s"
        val = (bname,price,author,bid)
        cursor = con.cursor()
        cursor.execute(sql,val)
        con.commit()
        return redirect("/showAllBook")

if __name__ == "__main__":
    app.run(debug=True)
