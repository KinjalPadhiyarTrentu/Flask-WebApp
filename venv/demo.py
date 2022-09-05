from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def greet():
    return "Good morning User"

@app.route("/helloName/<name>")
def greetName(name):
    return "Good morning User "+name

@app.route("/")
def home():
    return "Welcome to home page"

@app.route("/square/<int:n1>")
def square(n1):
    ans = str(n1*n1)
    return "The square of number is "+ans

@app.route("/sum/<int:n1>/<int:n2>")
def sum(n1,n2):
    ans = str(n1+n2)
    return "The sum of the number "+ans

if __name__=='__main__':
    app.run(debug=True,port=8085)