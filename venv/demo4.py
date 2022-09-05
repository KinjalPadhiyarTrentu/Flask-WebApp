from flask import *

app = Flask(__name__)

@app.route("/british")
def index():
    return render_template("index.html")

@app.route("/input",methods=["POST"])
def input():
    uname=request.form["uname"] #for get it is request.args.get('argument-name')
    lname=request.form["lname"] #for get it is request.args.get('argument-name')

    return "Welcome "+uname+" "+lname+" on this page"

@app.route("/books",methods=["post"])
def books():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "nimda":
        return render_template("book.html")
    else:
        return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/")
def default():
    return render_template("calculate.html")

@app.route("/calculate",methods=["POST"])
def addition():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    button_clicked = request.form["act"]

    if button_clicked == "add":
        result = str(num1+num2)
        return result
    elif button_clicked == "mul":
        result = str(num1*num2)
        return result
    elif button_clicked == "div":
        result = str(num1/num2)
        return result
    elif button_clicked == "sub":
        result = str(num1-num2)
        return result

if __name__ == '__main__':
    app.run(debug=True)