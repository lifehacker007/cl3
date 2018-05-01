#Read (read.md) file before executing the program
from flask import Flask
from flask import request
from flask import render_template
import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismDetected = stringComparison.PlagiarismChecker(text1,text2)
    if plagiarismDetected is True :
        return "<h1>Plagiarism Detected !</h1>"
    else :
        return "<h1>No Plagiarism Detected !</h1>"

if __name__ == '__main__':
    app.run()
