from flask import *

app = Flask(__name__)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html",uname=name)

@app.route("/age")
def ageCheck():
    age = 0
    fname = "text"
    lname = "text"
    dict = {"age": age, "fname": fname, "lname": lname}
    return render_template("formInterpolation.html",dict = dict)

@app.route("/agecheck", methods = ["POST"])
def age():
    if request.method == "POST":
        age = int(request.form["age"])
        fname = request.form["fname"]
        lname = request.form["lname"]
        dict = {"age":age,"fname":fname,"lname":lname}
        return render_template("formInterpolation.html",dict = dict)
    else:
        age = int(request.args.get("age"))
        fname = request.args.get("fname")
        lname = request.args.get("lname")
        dict = {"age": age, "fname": fname, "lname": lname}
        return render_template("formInterpolation.html", dict=dict)


if __name__== '__main__':
    app.run(debug=True)