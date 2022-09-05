from flask import *

app = Flask(__name__)


@app.route("/login/<username>/<password>")
def login(username, password):
    if username == "admin" and password == "nimda":
        return render_template("welcome.html")
        # return redirect(url_for("welcome"))

    else:
        return render_template("error.html")
        # return redirect(url_for("error"))


@app.route("/welcome")
def welcome():
    return "Welcome admin on this page"


@app.route("/error")
def error():
    return "Invalid username or password"


if __name__ == "__main__":
    app.run(debug=True)
