from flask import Flask,redirect,render_template,session,request

app = Flask(__name__)
app.secret_key = 'Firstbit'


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        
        if uname == "dipesh" and pwd == "asdf@123":
            session["uname"] = uname
            return redirect("/securedPage")
        else:
            return redirect("/login")
        
@app.route("/securedPage",methods=["GET","POST"])
def securedPage():
    if "uname" in session:
        return render_template("securedPage.html")
    else:
        return redirect("/login")
    

@app.route("/logout",methods=["GET","POST"])
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)