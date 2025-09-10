from flask import Flask

app = Flask(__name__)

@app.route("/display")
def displayMessage():
    return f"Welcome to Flask!"


@app.route("/login")
def login():
    return "login page!"

if __name__ == "__main__":
    app.run()