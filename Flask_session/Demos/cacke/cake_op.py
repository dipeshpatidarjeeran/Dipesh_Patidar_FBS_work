import mysql.connector
from flask import render_template,redirect,request
from werkzeug.utils import secure_filename

con = mysql.connector.connect(host="localHost",user="root",password="asdf@123",database="mycake")

def addCake():
    if request.method == "GET":
        sql = "select * from category"
        cursor = con.cursor()
        cursor.execute(sql)
        cats = cursor.fetchall()
        return render_template("cates/addCake.html",cats=cats)
    else:
        cake_name = request.form.get("cake_name")
        price = request.form.get("price")
        description = request.form.get("description")
        cid = request.form.get("cid")

        f = request.files['image_url']
        filename = secure_filename(f.filename)
        print(filename)
        filename = "static/Images/"+f.filename
        print(filename)
        f.save(filename)

        filename = "Images/"+secure_filename(f.filename)

        sql = "insert into Cake (cake_name,price,description,image_url,cid) values (%s,%s,%s,%s,%s)"
        val = (cake_name,price,description,filename,cid)
        cursor = con.cursor()
        cursor.execute(sql,val)
        con.commit()
        return "Cake Added..."