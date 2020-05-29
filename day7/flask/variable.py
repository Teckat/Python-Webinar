from flask import Flask

# app object

app = Flask(__name__)


@app.route('/')
def welcome():
    print("welcome")
    return 'Welcome To Teckat'


@app.route('/user/<name>')
def user(name):
    # return "Hello %s" % name
    return "hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True)
