from flask import Flask, render_template, redirect, request, make_response, session
from datetime import datetime,timedelta

app = Flask(__name__)
app.secret_key = 'Firstbit'

@app.route("/demohidden", methods=["GET","POST"])
def demoHidden():
    if request.method == "GET":
        return render_template("demoHidden.html")
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        uname = f"{fname} {lname}"
        return render_template("demoHidden.html",uname=uname)


@app.route("/demoClick", methods=["GET","POST"])
def demoClickCount():
    if request.method == "GET":
        no_of_count = 0
        return render_template("demoClickCount.html",no_of_count=no_of_count)
    else:
        count = int(request.form.get("no_of_count"))
        count += 1
        return render_template("demoClickCount.html",no_of_count=count)

@app.route("/queryDemo", methods=["GET","POST"])
def queryDemo():
    if request.method == "GET":
        return render_template("queryDemo.html")
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        url = f"/queryDisplay?fname={fname}&lname={lname}"
        return redirect(url)

@app.route("/queryDisplay")
def queryDisplay():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    return "<h1>Welcom dear "+fname+" "+lname+"</h1>"


@app.route("/register", methods=["GET","POST"])
def user_register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        age = request.form.get("age")
        url = f"/showVotingOp?name={name}&age={age}"
        return redirect(url)


@app.route("/showVotingOp", methods=["GET","POST"])
def showVotingOp():
    name = request.args.get("name")
    age = int(request.args.get("age"))

    if age < 18:
        return f"<h1>Dear {name}, are not eligible to vote</h1>"
    
    if request.method == "POST":
        opt = request.form.get("opt")
        return f"<h1>Dear {name}, you selected {opt} Thanks for your vote</h1>"
    
    return render_template("showVotingOp.html",name=name,age=age)


@app.route("/cookieDemo", methods=["GET","POST"])
def cookieDemo():
    if request.method == "GET":
        return render_template("cookieDemo.html")
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        bname = request.form.get("bname")
        resp = make_response("cookies created...")
        resp.set_cookie("fname",fname)
        resp.set_cookie("lname",lname)
        resp.set_cookie("bname",bname,expires=datetime.now()+ timedelta(days=5))
        return resp
    
@app.route("/displayCookie", methods=["GET","POST"])
def displayCookies():
    return render_template("cookieDisplay.html")


@app.route("/sessionDemo", methods=["GET","POST"])
def sessionDemo():
    if request.method == "GET":
        return render_template("sessionDemo.html")
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        # create session
        session['fname'] = fname
        session['lname'] = lname
        return "session created..."
    
@app.route("/displaySession", methods=["GET","POST"])
def displaySession():
    return render_template("displaySession.html")

if __name__ =="__main__":
    app.run(debug=True)