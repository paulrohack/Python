<<<<<<< HEAD
from flask import Flask,request,render_template,redirect,url_for
import random,time
from random import randint

file1 = open('FLASK\VERSE.txt', 'r') 
Lines = file1.readlines() 


app = Flask(__name__)
@app.route("/")
def page():
    return redirect(url_for("login"))
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        return  redirect(url_for("profile",user=name.upper()))
    else:
        return render_template("base.html")
@app.route("/profile/<user>/")
def profile(user):
    verse = Lines[random.randint(0,len(Lines))]
    return render_template("index.html",name = user,promise = verse)
if __name__ == "__main__":
    app.run(debug=True)
    



=======
from flask import Flask,request,render_template,redirect,url_for
import random,time
from random import randint

file1 = open('FLASK\VERSE.txt', 'r') 
Lines = file1.readlines() 


app = Flask(__name__)
@app.route("/")
def page():
    return redirect(url_for("login"))
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        return  redirect(url_for("profile",user=name.upper()))
    else:
        return render_template("base.html")
@app.route("/profile/<user>/")
def profile(user):
    verse = Lines[random.randint(0,len(Lines))]
    return render_template("index.html",name = user,promise = verse)
if __name__ == "__main__":
    app.run(debug=True)
    



>>>>>>> 1716e3ac153e6b6805d02dd7397be643a7ac4293
    