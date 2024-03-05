from flask import Flask, render_template, request
import re


app = Flask(__name__)
matched_strings = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST','GET'])
def regex():
    string = request.form.get('string')
    regex = request.form.get('regex')
    
    matched_strings = []
    try:
        matched_strings = re.findall(regex, string)
        error_message = None
    except re.error as e:
        matched_strings = []
        error_message = "Invalid regular expression: {}".format(e)
    
    return render_template('index.html', string=string, regex=regex, matched_strings=matched_strings, error_message=error_message)

@app.route('/email',methods=['GET','POST'])
def email():
    email = request.form.get('email')
    email_pattern = r'^[\w\.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        message = "Email is valid: {}".format(email)
    else:
        message = "Email is invalid: {}".format(email)
    return render_template('index.html', message=message)
if __name__ == '__main__':
    app.run(debug=True)
