from flask import Flask
app=Flask(__name__)
@app.route("/")
def a():
    return "oaaoa"
@app.route("/ac")
def abc():
    return "oa abcabcac"
