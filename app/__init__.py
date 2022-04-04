from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def example():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/notfound')
def not_found():
    return render_template('not_found.html')

@app.route('/auth')
def auth():
    return render_template('auth.html')
