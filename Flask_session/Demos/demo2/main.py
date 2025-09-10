from flask import Flask, render_template

app = Flask(__name__)


@app.route("/demoHtml")
def demoHtml():
    fname = "Ram"
    lname = "sharma"
    return render_template("demo.html",fname=fname, lname=lname)

@app.route("/demoList")
def demoList():
    data = ["Manoj","Ram","Dipesh","Suraj","Ganesh"]
    return render_template("demoList.html", data=data)

@app.route("/demoNestedList")
def demoNestedList():
    data = [[101,"Manoj",78],[102,"Sanoj",68],[103,"Mohan",58],[104,"Suraj",76]]
    return render_template("demoNestedList.html",data=data)

@app.route("/empDetails")
def empDetails():
    data = [[2101,"Raj",54000],[2102,"Dipesh",68000],[2103,"Ram",50000],[2104,"Suraj",70000]]
    return render_template("empDetails.html",data=data)

@app.route("/emp_stud")
def empStudDetails():
    data = [[2101,"Raj",54000],[2102,"Dipesh",68000],[2103,"Ram",50000],[2104,"Suraj",70000]]
    stu_data = [[101,"Manoj",78],[102,"Sanoj",68],[103,"Mohan",58],[104,"Suraj",76]]
    data = {"emp_data":data, "studnet":stu_data}
    
    return render_template("displayCombined.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)