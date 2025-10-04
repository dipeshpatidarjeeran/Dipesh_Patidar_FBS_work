import mysql.connector
from flask import render_template,redirect,request,session

con = mysql.connector.connect(host="localHost",user="root",password="asdf@123",database="mycake")

def login_required(fun): 
    def wrapper(): 
        if "uname" in session: 
            fun() 
        else: 
            return redirect("/adminLogin") 
    return wrapper


def adminLogin():
    if request.method == "GET":
        return render_template("adminLogin.html")
    else:
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        sql = "select count(*) from adminlogin where username=%s and password=%s"
        val = (uname,pwd)
        cursor = con.cursor()
        cursor.execute(sql,val)
        count = cursor.fetchone()
        if count[0] == 0:
            return redirect("/adminLogin")
        else:
            session['uname'] = uname
            return redirect("/adminDashboard")
        

def adminLogout():
    session.clear()
    return redirect("/adminLogin")

@login_required
def adminDashboard():
    return render_template("/adminDashboard.html")
    