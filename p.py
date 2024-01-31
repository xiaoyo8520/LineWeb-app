from flask import Flask
app=Flask(_name_)

@app.route("/")
def a():
  return "oa oa"
@app.route("/abc")
def abc():
  return "oa abcabcabc"
  
