'''
Source:

Author: Bagiya

'''


from flask import Flask,render_template, request
import random
import json

# Local import
from models import reverse_string, addition, update_json

app  = Flask(__name__)
PORT = 3011

@app.route('/')
def main():
    return render_template('index.html')

@app.route("/reverse", methods= ['post'])
def sample():
     if request.method == 'POST':
        input_string = request.form['my_name']
        reversed_string = reverse_string(input_string)
        return render_template('results.html', org = input_string, reversed_string=reversed_string)

@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/add-result', methods= ['post'])
def add_result():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        result = addition(int(input1), int(input2))
        return render_template('add.html', result = result)
        
@app.route('/new-user')
def user_update():
    return render_template('user.html')

@app.route('/user-detail', methods= ['post'])
def user_detail():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        update_json(name, int(age), city)
        return render_template('user.html', msg = 'updated successfully!!!')




if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)