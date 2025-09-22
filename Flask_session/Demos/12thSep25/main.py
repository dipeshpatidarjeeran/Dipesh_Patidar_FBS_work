from flask import Flask,redirect,render_template,request
import mysql.connector


app = Flask(__name__)
con = mysql.connector.connect(host="localhost",user="root",password="asdf@123",database='MyFlaskDb')


@app.route("/addStudent", methods=["GET", "POST"])
def addStudent():
    if request.method == "GET":
        return render_template("addStudent.html")
    else:
        sname = request.form.get("sname")
        age = request.form.get("age")
        per = request.form.get("per")
        course = request.form.get("course")

        sql = """insert into students(sname,age,percentage,course) values(%s,%s,%s,%s)"""
        val = (sname,age,per,course)
        cursor = con.cursor()
        cursor.execute(sql, val)
        con.commit()
        return redirect("/showAllStudent")

@app.route("/showAllStudent")
def showAllStudent():
    sql = "select * from students"
    cursor = con.cursor()
    cursor.execute(sql)
    studs = cursor.fetchall()
    return render_template("showAllStudent.html",studs=studs)


@app.route("/deleteStudent/<sid>",methods=["GET","POST"])
def deleteStudent(sid):
    if request.method == "GET":
        return render_template("deleteConfirm.html")
    else:
        action = request.form.get("action")
        if action == "Yes":
            sql = "delete from Students where sid=%s"
            val = (sid,)
            cursor = con.cursor()
            cursor.execute(sql,val)
            con.commit()
        return redirect("/showAllStudent")
    
    
@app.route("/editStudent/<sid>",methods=["GET","POST"])
def editStudent(sid):
    if request.method == "GET":
        sql = "select * from Students where sid=%s"
        val = (sid,)
        cursor = con.cursor()
        cursor.execute(sql,val)
        studs = cursor.fetchone()
        return render_template("editStudent.html",stud=studs)
    else:
        sname = request.form.get("sname")
        age = request.form.get("age")
        per = request.form.get("per")
        course = request.form.get("course")

        sql = """update students set sname=%s,age=%s,percentage=%s,course=%s where sid=%s"""
        val = (sname,age,per,course,sid)
        cursor = con.cursor()
        cursor.execute(sql, val)
        con.commit()
        return redirect("/showAllStudent")

if __name__ == "__main__":
    app.run(debug=True)


