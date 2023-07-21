

# result = reverse_string("Prabhu")

# print(result)

'''
Source:

Author: Raja CSP


'''


from flask import Flask,render_template, request
import random
import json


# Local import

from models import reverse_string 

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

if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)