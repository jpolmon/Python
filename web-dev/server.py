from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return "<p>These are my thoughts on blogs</p>"

@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog</p>"