from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'this survey has super secret content'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods = ['POST'])
def confirmation():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route('/result')
def save_submission():

    return render_template('result.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comments'])

class Response:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_response(cls):
        is_valid = True
        if len(cls['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
            return is_valid



if __name__ == "__main__":
    app.run(debug=True)