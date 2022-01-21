from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    #route to homepage
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    #route to homepage
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    #route to homepage
    return "welcome back"