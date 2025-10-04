from flask import render_template,request,redirect,session
import mysql.connector

con = mysql.connector.connect(host="localHost",user="root",password="asdf@123",database="mycake")



def homepage():
    sql = "select * from category"
    cursor = con.cursor()
    cursor.execute(sql)
    cats = cursor.fetchall()
    sql = "select * from cake"
    cursor = con.cursor()
    cursor.execute(sql)
    cakes = cursor.fetchall()
    return render_template("homepage.html",cats=cats,cakes=cakes)


def searchData():
    data = request.form.get("searchdata")
    data = data[:3]
    sql = f"select * from cake where cake_name like  '%{data}%'"
    cursor = con.cursor()
    cursor.execute(sql)
    cakes = cursor.fetchall()
    sql = "select * from category"
    cursor = con.cursor()
    cursor.execute(sql)
    cats = cursor.fetchall()
    return render_template("homepage.html",cakes=cakes,cats=cats)



def MakePayment():
    if request.method == "GET":
        return render_template("user/makePayment.html")
    else:
        cardno = request.form.get("cardno")
        cvv = request.form.get("cvv")
        expiry = request.form.get("expiry")
        sql = "select count(*) from Payment where cardno=%s and cvv=%s and expiry=%s"
        val = (cardno,cvv,expiry)
        cursor = con.cursor()
        cursor.execute(sql,val)
        count = cursor.fetchone()
        if count[0] == 1:
            # buyer update
            sql = "update payment set balance=balance-%s where cardno=%s and cvv=%s and expiry=%s"
            val = (session['total'],cardno,cvv,expiry)
            cursor.execute(sql,val)
            #seller update
            sql = "update payment set balance=balance+%s where cardno=%s and cvv=%s and expiry=%s"
            val = (session['total'],"222",'222','12/2030')
            cursor.execute(sql,val)
            con.commit()
            return redirect("/menu/all")
        else:
            return redirect("/makePayment")