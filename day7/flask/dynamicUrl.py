from flask import Flask, redirect, url_for

# app object

app = Flask(__name__)


@app.route('/admin/')
def welcome():
    print("welcome")
    return 'Welcome To Teckat'


@app.route('/guest/<name>')
def guest(name):
    # return "Hello %s" % name
    return "hello guest {}".format(name)


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('guest', name=name))


if __name__ == "__main__":
    app.run(debug=True)
