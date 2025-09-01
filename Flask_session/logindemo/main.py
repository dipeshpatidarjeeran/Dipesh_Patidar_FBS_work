from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/verify")
# def verify():
#     uname = request.args.get("uname")
#     pwd = request.args.get("pwd")
#     if uname == "dipesh" and pwd == "asdf@123":
#         return "Success"
#     else:
#         return "Failed"
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        if uname == "dipesh" and pwd == "asdf@123":
            return "Success"
        else:
            return "Failed"
        
@app.route("/calculate", methods=["GET","POST"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        
        num1 = float(request.form.get("first"))
        num2 = float(request.form.get("second"))
        opt = request.form.get("opt")

        if opt == "+":
            result = num1 + num2
        elif opt == "-":
            result = num1 - num2
        elif opt == "*":
            result = num1 * num2
        elif opt == "/":
            if num2 == 0:
                return "Division by zero not allowed"
            result = num1 / num2
        return f"{result}"
    
if __name__ == "__main__":
    app.run(debug=True)