import sqlite3

from flask import *

app = Flask(__name__)
app.secret_key = "rachit"

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("registration.html")


@app.route("/adduser",methods=["POST"])
def addUser():
    con = sqlite3.connect(r"C:\Users\pdc2b-training.pdc2b\myape.db")
    cr = con.cursor()
    username = request.form["username"]
    password = request.form["password"]
    gender = request.form["gender"]
    dob = request.form["dob"]
    address = request.form["address"]
    email = request.form["email"]
    mobile = request.form["mobile"]

    cr.execute("insert into register values(?,?,?,?,?,?,?)",(username,password,gender,dob,address,email,mobile))
    con.commit()
    return render_template("index.html")


@app.route("/books",methods=["POST","GET"])
def books():
    username = request.form["username"]
    password = request.form["password"]
    con = sqlite3.connect(r"C:\Users\pdc2b-training.pdc2b\myape.db")
    cr = con.cursor()
    cr.execute("select * from register where username = ? and password=?",(username, password))
    if len(cr.fetchall()) > 0:
        session["user"] = username
        cr.execute("select * from books")
        result = cr.fetchall()
        return render_template("book.html",data=result)
    else:
        render_template("index.html")

@app.route("/addToCart/<id>/<user>")
def addToCart(id,user):
    con = sqlite3.connect(r"C:\Users\pdc2b-training.pdc2b\myape.db")
    cr = con.cursor()
    cr.execute("update books set username=? where book_id=?",(user,id))
    cr.execute("update books set status=? where book_id=?", ("NA", id))
    con.commit()
    cr.execute("select * from books")
    result = cr.fetchall();
    return render_template("book.html",data=result)

@app.route("/cookies")
def cookiehome():
    return render_template("cookies.html")

@app.route("/setcookies",methods=["POST"])
def setcookies():
    username = request.form["nm"]
    resp = make_response(render_template("showcookies.html"))
    resp.set_cookie("username",username)
    return resp

@app.route("/show")
def showcookies():
    name = request.cookies.get("username")
    return "Cookies stored were "+name

@app.route("/session")
def sessionPage():
    return render_template("sessionForm.html")

@app.route("/setSession" ,methods=["post"])
def showsession():
    name = request.form["name"]
    city = request.form["city"]
    session["name"] = name
    session["city"] = city
    return "<html><h1>Data Stored in the session <a href=/getSession>Show Data</a></h1></html>"

@app.route("/getSession")
def getSession():
    if "name" in session:
        return render_template("showSession.html",sobject=session)

@app.route("/success",methods=["POST"])
def uploadFile():
    if request.method == "POST":
        f = request.files["file"]
        f.save(f.filename)
        return render_template("success.html",name=f.filename)

@app.route("/demoFlash",methods=["POST"])
def flashDemo():
    uname = request.form["uname"]
    upass = request.form["upass"]
    if uname == "admin" and upass=="nimda":
        return render_template("welcome.html")
    else:
        abort(401)

@app.route("/myindex")
def flashPage():
    return render_template("myindex.html")

if __name__ == '__main__':
    app.run(debug=True)
