from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/contact')
def contact():    
    return render_template('contact.html',title='Contact')
