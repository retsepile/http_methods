from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def log():
    return render_template('login1.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "Sam" and password == "10150":
        return "Welcome %s" % username + request.method
    else:
        return "Error in the logging in" + request.method


if __name__ == '__main__':
    app.run(debug=True)
