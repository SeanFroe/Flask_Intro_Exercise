from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''Return a "Welcome" greeting'''
    html = "<html><body><h1>Welcome</h1></body></html>"
    
    return html

@app.route('/welcome/home')
def welcome_home():
    '''Return a "Welcome home" greeting'''
    html = "<html><body><h1>Welcome home</h1></body></html>"
    
    return html

@app.route('/welcome/back')
def welcome_back():
    '''Return a "Welcome back" greeting'''
    html = "<html><body><h1>Welcome back</h1></body></html>"
    
    return html